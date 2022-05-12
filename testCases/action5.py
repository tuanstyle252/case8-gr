from selenium.webdriver import ActionChains, Keys
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

    def test_action2_1(self, setup):
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

        time.sleep(5)
        # change page
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        input = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        ActionChains(self.driver).move_to_element(input).click(input).send_keys("QA").send_keys(Keys.ENTER).perform()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/div/ul/li"))).click()

        #check color
        time.sleep(2)
        user = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li[1]").value_of_css_property("background-color")
        grb = Color.from_string(user).hex
        assert grb == "#00b0f2"

        #check shown x
        x = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li[1]/a")
        assert x.is_displayed()

        # click x
        self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        time.sleep(2)
        user = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul//*[@class='contact']")))
        assert user == True

        time.sleep(1)
        # check Type to find contacts...
        type = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        assert type.get_attribute("placeholder") == "Type to find contacts..."

        time.sleep(1)
        # check save
        save = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/button")
        assert save.is_displayed() and save.text == "SAVE"
        self.driver.close()

    def test_action2_2(self, setup):
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

        time.sleep(5)
        # change page
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        input = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        ActionChains(self.driver).move_to_element(input).click(input).send_keys("asdasdasdasdasdasdassa").send_keys(Keys.ENTER).perform()
        #input data that does not match
        time.sleep(2)
        menu_autocomplete = len(self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul"))
        for i in range(menu_autocomplete):
            if i > 0:
                raise ValueError("dropdown show")
            else:
                assert True
        self.driver.close()

    def test_action2_3(self, setup):
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
        edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        time.sleep(5)
        # change page
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        input = self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        ActionChains(self.driver).move_to_element(input).click(input).send_keys("b").send_keys(Keys.ENTER).perform()

        menu_auto = self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul/li")
        for element in menu_auto:
            assert element.is_displayed()

        self.driver.close()

    def test_action2_4(self, setup):
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

        time.sleep(5)
        # change page
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        input = self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        ActionChains(self.driver).move_to_element(input).click(input).send_keys("b").perform()

        # select user
        menu_auto = self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul/li")
        for i in menu_auto:
            if i.text == "Chris Mobile":
                i.click()
                break

        time.sleep(2)
        x = self.driver.find_elements(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/a")
        for i in x:assert i.text == " x "
        # click x
        self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        time.sleep(2)
        user = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul//*[@class='contact'][1]")))
        assert user == True

    def test_action2_5_6(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        # login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # process group
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
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("14516")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        time.sleep(5)
        # change page
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "embed-responsive-item"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        input = self.driver.find_element(By.XPATH,
                                         "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li/input")
        ActionChains(self.driver).move_to_element(input).click(input).send_keys("b").perform()

        # select user
        menu_auto = self.driver.find_elements(By.XPATH, "//*[@class='contact-autocomplete']/ul/li")
        for i in menu_auto:
            if i.text == "Chris Mobile":
                i.click()
                break

        self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/button").click()
        # check wat
        user = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span/span")))
        assert user.text == "Chris Mobile"

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[1]/a"))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[1]/span/span[2]/button").click()

        self.driver.switch_to.default_content()
        #check modal close
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        self.driver.close()