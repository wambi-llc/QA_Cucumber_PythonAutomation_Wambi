from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import *
from utilities.settings import settings
from selenium.webdriver.common.action_chains import ActionChains as Action_Chains
from selenium.webdriver.common.keys import *

# wait = WebDriverWait(driver, 2)

class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None
    browser = None
    driver = webdriver.Chrome()
    #actions = ActionChains(driver)


    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        # nodeUrl = '/usr/bin/chromedriver'
        print('---------' + settings.browser + '---------')
        #self.driver == webdriver.Chrome()

        if settings.browser == "chrome":
            self.driver == webdriver.Chrome()
            self.driver.maximize_window()

        #
        #     #self.driver = webdriver.Remote(command_executor=nodeUrl,
        #                                    #desired_capabilities={'browserName': 'chrome',
        #                                                          'javascriptEnabled': True})
        elif settings.browser == "IE":
            self.driver == webdriver.Ie()
        #     self.driver = webdriver.Remote(command_executor=nodeUrl,
        #                                    desired_capabilities={'browserName': 'firefox',
        #                                                          'javascriptEnabled': True})

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)

    def navigateToMaps(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def waitOnElement(self, elemXpath):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, elemXpath)))

    def waitFor(self, timeInSec):
        self.driver.implicitly_wait(timeInSec)

    def elementClick(self, elemXpath):
        return self.driver.find_element_by_xpath(elemXpath).click()

    def elementLocation(self, elemXpath):
         return self.driver.find_element_by_xpath(elemXpath)


    def clearElement(self, elemXpath):
        return self.driver.find_element_by_xpath(elemXpath).clear()

    def enterValues(self, elemXpath, value):
        return self.driver.find_element_by_xpath(elemXpath).send_keys(value)



    def getTextForElement(self, element):
        return self.driver.find_element_by_xpath(element).text



    def getElements(self, element):
        return self.driver.find_elements_by_xpath(element)

    def getSelectedElements(self,element):
        return Select(self.driver.find_element_by_xpath(element))

    def pressTab(self):
        actions = Action_Chains(self.driver)
        return actions.send_keys(Keys.TAB).perform()

    def pressEnter(self):
        actions = Action_Chains(self.driver)
        return actions.send_keys(Keys.ENTER).perform()

    def pressKeyDown(self):
        actions = Action_Chains(self.driver)
        return actions.send_keys(Keys.ARROW_DOWN)

    def moveToElement(self,element):
        actions = Action_Chains(self.driver)
        return actions.move_to_element(self.driver.find_element_by_xpath(element)).perform()

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def zoomWindow(self):
        self.driver.execute_script("document.body.style.zoom = '150%'")

    def tagAttributes(self, elemXpath,attrvalue):
        return self.driver.find_element_by_tag_name(elemXpath).get_attribute(attrvalue)


    def closeBrowser(self):
        self.driver.quit()

driver = Driver.get_instance()