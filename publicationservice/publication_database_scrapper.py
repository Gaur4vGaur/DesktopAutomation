import selenium.webdriver.chrome.service as service

from persistence.persist import read, update, PUB_READ_COUNT, LAST_COUNT, PERSISTENCE_PATH
from publicationservice.all_publications import ALL_PUBLICATIONS
from publicationservice.publication_detailer import publication_detailer
from util.BrowserUtil import Driver


def wait_to_load_elements(elem):
    text = elem.text
    i = 0
    while i < 50000 and text == "":
        text = elem.text
        i = i + 1

    print("elements now available")


def fetch_all_article_links(elem):
    a_tags_in_element = elem.find_elements_by_tag_name("a")
    # use dictionary instead of set to preserve insertion order
    tags = {a_tag.get_attribute('href'): 1 for a_tag in a_tags_in_element if
            a_tag.get_attribute('href') and 'pubs' in a_tag.get_attribute('href')}
    return list(tags.keys())


def recent_publications(element, svc, update_count):
    tags = fetch_all_article_links(element)
    publications = [publication_detailer(svc, publication) for publication in tags[0:update_count]]
    return publications


def persisted_publications(svc, read_count):
    all_publications = read(ALL_PUBLICATIONS)
    pubs_to_read = [pub.get("filename_html").replace(".html", "") for pub in
                    all_publications[read_count:read_count + 3]]
    publications = [publication_detailer(svc, f"https://research.google/pubs/{publication}")
                    for publication in pubs_to_read]
    return publications


def publication_updates(year):
    # test_pub_details()
    publications = []
    persisted_record = read(PERSISTENCE_PATH)

    svc = service.Service('../driver/chromedriver')
    svc.start()
    driver = Driver(svc, f"https://research.google/pubs/?year={year}")
    element = driver.driver.find_element_by_class_name("search__cards")
    wait_to_load_elements(element)
    last_count = int(driver.text_for_class_name("filter__option-count"))
    persisted_last_count = persisted_record.get(LAST_COUNT)
    update_count = last_count - persisted_last_count

    if last_count > persisted_last_count:
        publications = recent_publications(element, last_count, svc)
        persisted_record[LAST_COUNT] = last_count
    else:
        # push out previous papers
        publications = persisted_publications(svc, persisted_record.get(PUB_READ_COUNT))
    driver.quit()

    update(PERSISTENCE_PATH, persisted_record)
    return update_count, publications


def update_read_count(read_count):
    persisted_record = read(PERSISTENCE_PATH)
    print("persisted record", persisted_record)
    persisted_record[PUB_READ_COUNT] = persisted_record.get(PUB_READ_COUNT)+read_count
    print("updated record", persisted_record)
    update(PERSISTENCE_PATH, persisted_record)


if __name__ == "__main__":
    import datetime
    now = datetime.datetime.now()
    update_count, publications = publication_updates(now.year)
    print(update_count)
    for i in publications:
        print(i.pub_title)
