from selenium import webdriver
from selenium.webdriver.safari import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Odev:
    def login_user_pass_error(self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("")
        Pass.send_keys("")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(10)

    def login_pass_error(self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("kullanıcı")
        Pass.send_keys("")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(10)

    def user_locked(self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("locked_out_user")
        Pass.send_keys("secret_sauce")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(10)

    def X (self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("")
        Pass.send_keys("")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(2)
        xBtn = log.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        xBtn.click()
        sleep(10)

    def inventor(self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("standard_user")
        Pass.send_keys("secret_sauce")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(10)

    def urun_adet(self):
        log = webdriver.WebDriver()
        log.maximize_window()
        log.get("https://www.saucedemo.com/")
        sleep(2)
        Uname = log.find_element(By.XPATH,"//*[@id='user-name']")
        Pass = log.find_element(By.XPATH,"//*[@id='password']")
        sleep(2)
        Uname.send_keys("standard_user")
        Pass.send_keys("secret_sauce")
        sleep(2)
        logBtn = log.find_element(By.XPATH,"//*[@id='login-button']")
        logBtn.click()
        sleep(2)
        urun = log.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Toplam da {len(urun)} adet var.")
        
        while True:
            continue


deneme101 = Odev()
deneme101.login_user_pass_error()
deneme101.login_pass_error()
deneme101.user_locked()
deneme101.X()
deneme101.inventor()
deneme101.urun_adet()