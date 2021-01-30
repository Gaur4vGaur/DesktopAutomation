from selenium import webdriver


class Driver:
    def __init__(self, svc, url):
        self.driver = webdriver.Remote(svc.service_url)
        self.driver.get(url)

    def text_for_class_name(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        return element.text

    def quit(self):
        self.driver.quit()
