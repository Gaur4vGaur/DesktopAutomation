from publicationservice.publication_details import PublicationDetails

from util.BrowserUtil import Driver


def publication_detailer(svc, url, year):
    driver = Driver(svc, url)
    publication_details = PublicationDetails(
        driver.text_for_class_name("hero__title"),
        driver.text_for_class_name("hero__content"),
        driver.second_text_for_class_name("content__body"),
        driver.text_for_class_name("bar__title"),
        url,
        year
    )

    driver.quit()
    return publication_details
