import pytest_subtests
import softest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pageObjects.loginPage import Loginpage
import time
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations as VE


class Testaction():
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()

    def test_action3_1(self, setup):
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
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14516")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        #click assign to me no hapening
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[1]/a[1]"))).click()

        self.driver.switch_to.default_content()
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        user = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[1]/span")))
        assert user.text == "QA Robot"
        self.driver.close()

    def test_action3_2(self, setup):
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

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]/div[2]"))).click()

        input = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("Kenth Doan").send_keys(Keys.ENTER).perform()

        time.sleep(1)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(edit)
        actions.perform()

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))

        self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span/a[1]").click()

        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='assignedTo']/div[1]/div[1]/div[1]/div[2]").click()

        time.sleep(2)
        input = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("QA Robot").send_keys(Keys.ENTER).perform()

        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()
        #check the name of the user shown on assigned to field
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        user = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[1]/span")))
        assert user.text == "QA Robot"

        self.driver.switch_to.default_content()
        #click x or done modal close
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        # check modal close
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        self.driver.close

    def test_action3_3(self, setup):
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

        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        #3.3 click on the update button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[1]/a[2]"))).click()
        time.sleep(2)
        user = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li[1]").value_of_css_property("background-color")
        grb = Color.from_string(user).hex
        assert grb == "#00b0f2"

        x = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/a")
        assert x.is_displayed()

        save = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/button")
        assert save.is_displayed() and save.text == "SAVE"
        #3.3.1 click on the x button
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/a").click()
        user = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul//*[@class='contact']")))
        if user:
            #the search field is shown
            type = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/input")
            # assert type.get_attribute("placeholder") == "Type to find contacts..."
            assert type.get_attribute("placeholder") == "Type to find contacts..."
        else:
            raise ValueError("user not remove")

        #3.3.2 click on the save button
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/button"))).click()
        type = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/input")
        soft_assert(type.get_attribute("placeholder") == "Type to find contacts...")
        # input not match
        input = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/input")
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("dasdasdasas").perform()

        time.sleep(2)
        menu_autocomplete = len(self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul"))
        for i in range(menu_autocomplete):
            if i > 0:
                raise ValueError("dropdown show")
            else:
                assert True

        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.DELETE)
        # input match
        input = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/input")
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("d").perform()

        menu_auto = self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul/li")
        for i in menu_auto:
            assert i.is_displayed()

        # select user
        menu_auto = self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul/li")
        for i in menu_auto:
            if i.text == "Annie Admin":
                i.click()
                break
        user = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li[1]")
        assert user.get_attribute("_name") == "Annie Admin"
        time.sleep(2)
        user = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li[1]").value_of_css_property("background-color")
        grb = Color.from_string(user).hex
        assert grb == "#00b0f2"

        x = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/div/div/ul/li/a")
        assert x.is_displayed()

        # click save
        self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[1]/div[3]/span/span[2]/button").click()
        self.driver.switch_to.default_content()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div/div[1]/div[1]/div[2]").click()
        time.sleep(4)
        input = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("Annie Admin").send_keys(Keys.ENTER).perform()

        time.sleep(1)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(edit)
        actions.perform()
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        txt = "[QA Robot reassigned this ticket to Annie Admin]"
        time.sleep(2)
        check = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div//*[@class='col-md-12']/table/tbody/tr[1]/td[2]")
        assert check.text == txt

        self.driver.switch_to.default_content()
        # check x and done
        # click x
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@class='modal-header']/button").click()
        # check close modal
        modal = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True
        # click done
        time.sleep(2)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        actions.move_to_element(menu)
        actions.click(edit)
        actions.perform()

        self.driver.find_element(By.XPATH, "//*[@class='modal-footer']/button").click()
        # check close modal
        modal = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        soft_assert(modal == True)
        self.driver.close()




