from util.BrowserUtil import driver, wait_to_load_elements


def fetch_all_article_links(elem):
    a_tags_in_element = elem.find_elements_by_tag_name("a")

    tags = {a_tag.get_attribute('href') for a_tag in a_tags_in_element if
            a_tag.get_attribute('href') and 'pubs' in a_tag.get_attribute('href')}
    return tags


def publication_url(year):
    return f"https://research.google/pubs/?year={year}"


if __name__ == "__main__":
    driver = driver()
    # print(date.today())

    driver.get(publication_url("2021"))
    element = driver.find_element_by_class_name("search__cards")
    wait_to_load_elements(element)
    tags = fetch_all_article_links(element)
    print(type(tags))
    print(tags)

    driver.quit()
