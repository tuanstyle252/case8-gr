from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import Loginpage
import time
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Testaction:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()

    def test_action1_1_2(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14495")

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='status']/div[1]/div[1]/div[1]/div[2]"))).click()
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        check_reopen = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[1]/span[2]/a").text

        if check_reopen == "REOPEN":
            self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[1]/span[2]/a").click()
            self.driver.switch_to.default_content()
            time.sleep(5)
            menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[8]")
            edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")

            actions = ActionChains(self.driver)
            actions.move_to_element(menu)
            actions.click(edit)
            actions.perform()

            self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))

            check_text = ["Open", "RESOLVE"]

            check_status__ = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[1]/span[1]").text
            for text in check_text:
                if text in check_status__:
                    assert check_status__, check_text
                else:
                    assert False
        else:
            pass
            self.driver.close()
        self.driver.quit()