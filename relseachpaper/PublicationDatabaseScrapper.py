import selenium.webdriver.chrome.service as service
from selenium import webdriver


def wait_to_load_elements(elem):
    text = elem.text
    i = 0
    while i < 50000 and text == "":
        text = elem.text
        i = i + 1

    print("elements now available")


def fetch_all_article_links(elem):
    a_tags_in_element = elem.find_elements_by_tag_name("a")

    tags = {a_tag.get_attribute('href') for a_tag in a_tags_in_element if
            a_tag.get_attribute('href') and 'pubs' in a_tag.get_attribute('href')}
    return tags


if __name__ == "__main__":
    svc = service.Service('../driver/chromedriver')
    svc.start()
    driver = webdriver.Remote(svc.service_url)
    driver.get("https://research.google/pubs/?year=2021")
    element = driver.find_element_by_class_name("search__cards")
    wait_to_load_elements(element)
    tags = fetch_all_article_links(element)
    print(type(tags))
    print(tags)

    driver.quit()
