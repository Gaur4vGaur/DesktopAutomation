from selenium import webdriver


class Driver:
    def __init__(self, svc, url):
        self.driver = webdriver.Remote(svc.service_url)
        self.driver.get(url)

    def text_for_class_name(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        return element.text

    def second_text_for_class_name(self, class_name):
        elements = self.driver.find_elements_by_class_name(class_name)
        text = "could not find text"
        if len(elements) > 2:
            text = elements[1].text

        return text

    def quit(self):
        self.driver.quit()
