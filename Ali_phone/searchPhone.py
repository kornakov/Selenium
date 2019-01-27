from selenium import webdriver
import time


class Searching:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def check(self, elem, className):
        try:
            elem.find_element_by_class_name(className)
        except AssertionError:
            return False
        return True

    def main_page(self):
        self.driver.get('https://ru.aliexpress.com/')
        if self.check(self.driver, "close-layer"):
            self.driver.find_element_by_class_name("close-layer").click()
        self.driver.find_element_by_name("SearchText").send_keys("xiaomi mi 8")
        time.sleep(1)
        self.driver.find_element_by_class_name('search-button').click()

    def goods_page(self):
        phones = self.driver.find_elements_by_class_name('info')
        for phone in phones:
            if self.check(phone, "free-s"):
                phone.click()
                break

    def __del__(self):
        self.driver.quit()

    def run(self):
        self.main_page()
        time.sleep(2)
        self.goods_page()
        time.sleep(10)


searching = Searching()
searching.run()
del searching
