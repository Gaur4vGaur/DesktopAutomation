import selenium.webdriver.chrome.service as service

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


if __name__ == "__main__":
    svc = service.Service('../driver/chromedriver')
    svc.start()
    driver = Driver(svc, "https://research.google/pubs/?year=2021")
    element = driver.driver.find_element_by_class_name("search__cards")
    wait_to_load_elements(element)
    print(driver.text_for_class_name("filter__option-count"))
    tags = fetch_all_article_links(element)
    # tags.sort(reverse=True)

    print(tags)
    # pub = list(tags)[0]
    # pub_details = publication_detailer(svc, pub)
    # https://stackoverflow.com/questions/27913261/python-storing-data

    driver.quit()
