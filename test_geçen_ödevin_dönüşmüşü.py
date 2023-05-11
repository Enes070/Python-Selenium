from selenium import webdriver
from selenium.webdriver.safari import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Odev:
    def setup_method(self):
        self.log = webdriver.WebDriver()
        self.log.maximize_window()
        self.log.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.log.quit()
    
    def initializerLog(self):
        logBtn = self.log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        return self.log
    
    def test_lupe(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"")
        actions.send_keys_to_element(Pass,"")
        actions.perform()
        errorMessage = self.log.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.log.save_screenshot(self.folderPath+"/test-lupe.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    def test_lpe(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"kullanıcı")
        actions.send_keys_to_element(Pass,"")
        actions.perform()
        self.log.save_screenshot(self.folderPath+"/test-lpe.png")

    def test_ul(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"locked_out_user")
        actions.send_keys_to_element(Pass,"secret_sauce")
        actions.perform()
        self.log.save_screenshot(self.folderPath+"/test-ul.png")

    def test_X(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"")
        actions.send_keys_to_element(Pass,"")
        actions.perform()
        errorMessage = self.log.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.log.save_screenshot(self.folderPath+"/test-X.png")
        assert errorMessage.text == "Epic sadface: Username is required"

        xBtn = log.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        xBtn.click()

    #@pytest.mark.parametrize("username, password",["standard_user","secret_sauce"])
    def test_inventor(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"standard_user")
        actions.send_keys_to_element(Pass,"secret_souce")
        actions.perform()
        Btn = log.find_element(By.XPATH,"//*[@id='login-button']")
        Btn.click()
        self.log.save_screenshot(self.folderPath+"/test-inventor.png")

    def test_ua(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"standard_user")
        actions.send_keys_to_element(Pass,"secret_souce")
        actions.perform()
        self.log.save_screenshot(self.folderPath+"/test-ua.png")

        urun = log.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Toplam da {len(urun)} adet var.")

    def test_shop(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"standard_user")
        actions.send_keys_to_element(Pass,"secret_sauce")
        actions.perform()
        sBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        sBtn.click()
        addBtn = log.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")
        addBtn.click()
        self.log.save_screenshot(self.folderPath+"/test-shop.png")

    def test_shop_remove(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"standard_user")
        actions.send_keys_to_element(Pass,"secret_sauce")
        actions.perform()
        sBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        sBtn.click()
        addBtn = log.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")
        addBtn.click()
        removBtn = log.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        removBtn.click()
        rmvBtn = log.find_element(By.XPATH,"//*[@id='remove-sauce-labs-backpack']")
        rmvBtn.click()
        self.log.save_screenshot(self.folderPath+"/test-shop-remove.png")
    
    def test_burger_menu(self):
        log = self.initializerLog()
        self.waitForElementVisible((By.XPATH,"//*[@id='user-name']"))
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        self.waitForElementVisible((By.XPATH,"//*[@id='password']"))
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        actions = ActionChains(log)
        actions.send_keys_to_element(Uname,"standard_user")
        actions.send_keys_to_element(Pass,"secret_sauce")
        actions.perform()
        Btn = log.find_element(By.XPATH,"//*[@id='login-button']")
        Btn.click()
        burgBtn = log.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']")
        burgBtn.click()
        self.log.save_screenshot(self.folderPath+"/test-burger-menu.png")
        

    def waitForElementVisible(self,locator):
        WebDriverWait(self.log,5).until(ec.visibility_of_element_located(locator))