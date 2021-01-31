import selenium.webdriver.chrome.service as service

from persistence.persist import read, update
from publicationservice.all_publications import ALL_PUBLICATIONS
from publicationservice.publication_detailer import publication_detailer
from util.BrowserUtil import Driver

PUBLICATION_PATH = "publication_update.data"


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


def test_pub_details():
    update(PUBLICATION_PATH, {'last_count': 95})


def publication_updates(year):
    test_pub_details()
    publications = []

    svc = service.Service('../driver/chromedriver')
    svc.start()
    driver = Driver(svc, f"https://research.google/pubs/?year={year}")
    element = driver.driver.find_element_by_class_name("search__cards")
    wait_to_load_elements(element)
    last_count = int(driver.text_for_class_name("filter__option-count"))
    persisted_last_count = read(PUBLICATION_PATH).get('last_count')
    update_count = last_count - persisted_last_count

    if last_count > persisted_last_count:
        tags = fetch_all_article_links(element)
        print(tags[0:update_count])
        publications = [publication_detailer(svc, publication) for publication in tags[0:update_count]]

        update(PUBLICATION_PATH, {'last_count': last_count})
    else:
        # push out previous papers
        publications = read(ALL_PUBLICATIONS)
        print(len(publications))

        print("no updates")
    driver.quit()

    return update_count, publications


if __name__ == "__main__":
    import datetime
    now = datetime.datetime.now()
    print(publication_updates(now.year))
