import selenium.webdriver.chrome.service as service
from selenium import webdriver


def driver():
    svc = service.Service('C:/Users/Admin/Downloads/softwares/chromedriver')
    svc.start()
    return webdriver.Remote(svc.service_url)


# The method is only used to wait and loop until elements are loaded
def wait_to_load_elements(elem):
    text = elem.text
    i = 0
    while i < 50000 and text == "":
        text = elem.text
        # print(i)
        i = i + 1

    print("elements now available")