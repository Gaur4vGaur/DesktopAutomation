import selenium.webdriver.chrome.service as service

from util.BrowserUtil import Driver

if __name__ == "__main__":
    url = "https://research.google/pubs/pub49999/"
    svc = service.Service('../driver/chromedriver')
    svc.start()

    driver = Driver(svc, url)
    print(driver.text_for_class_name("hero__title"))
    print(driver.text_for_class_name("hero__content"))
    print(driver.second_text_for_class_name("content__body"))
    print(driver.text_for_class_name("bar__title"))

    driver.quit()
