from option import details
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
from datetime import datetime, date, timedelta
import urllib
import requests
import os
import sys
import pyautogui
import pyperclip


class Facebook:
    def __init__(self, userInfo, postCodeList, folder, listingCount):
        self.userInfo = userInfo
        self.count = 1
        self.folder = folder
        self.filePath = f"{details['path']}\\{folder}\\M-{self.count}.jpg"
        self.title = details['title']
        self.tags = details['tags']
        self.description = details['description']
        self.price = details['price']
        self.postCodeList = postCodeList
        self.listingCount = listingCount
        self.chromePath = details['chromePath']
        self.chromeWebdriver = self.setupChrome()

    def setupChrome(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('windows-size=1200X600')
        # Add your ChromeWebdriver Path
        driver = webdriver.Chrome(self.chromePath, chrome_options=options)
        params = {
            "latitude": 51.507351,
            "longitude": -0.127758,
            "accuracy": 100
        }
        driver.execute_cdp_cmd("Emulation.clearGeolocationOverride", params)
        return driver

    def loginFaceBook(self, user, p):
        try:
            self.chromeWebdriver.get(
                'https://en-gb.facebook.com/marketplace/london')
            time.sleep(1.5)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[1]/label/input').send_keys(user)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/label/input').send_keys(p)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[3]/div/div/div[1]/div/span/span').click()
            time.sleep(1.5)
        except:
            self.chromeWebdriver.get(
                'https://en-gb.facebook.com/marketplace/london')
            time.sleep(1.5)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[1]/label/input').send_keys(user)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/label/input').send_keys(p)
            self.chromeWebdriver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[3]/div/div/div[1]/div/span/span').click()
            time.sleep(1.5)

    def addPicture(self):
        try:
            div = self.chromeWebdriver.find_elements_by_css_selector(
                'input[type="file"]')
            self.chromeWebdriver.execute_script(
                "arguments[0].setAttribute('class', 'visible')", div[0])
            time.sleep(2)
        except:
            div = self.chromeWebdriver.find_elements_by_css_selector(
                'input[type="file"]')
            self.chromeWebdriver.execute_script(
                "arguments[0].setAttribute('class', 'visible')", div[0])
            time.sleep(2)
        finally:
            div[0].send_keys(self.filePath)

    def createListing(self, postCode):
        self.chromeWebdriver.get(
            'https://www.facebook.com/marketplace/create/item')
        time.sleep(3)
        self.addPicture()
        div = self.chromeWebdriver.find_elements_by_css_selector(
            "div[aria-label=Marketplace]")
        text = div[0].find_elements_by_css_selector(
            "input[aria-invalid=false]")
        text[0].send_keys(self.title)
        text[1].send_keys(self.price)
        text[3].send_keys(Keys.CONTROL, 'a')
        text[3].send_keys(Keys.BACKSPACE)
        text[3].send_keys(postCode)
        time.sleep(1.5)
        text[3].send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        selectCity = self.chromeWebdriver.find_elements_by_css_selector(
            'li[aria-selected="false"]')
        description = div[0].find_elements_by_css_selector(
            "textarea[aria-invalid=false]")
        description[0].send_keys(self.description)
        time.sleep(1.5)
        try:
            availability = div[0].find_elements_by_css_selector(
                "label[aria-label='Availability']")
            availability[0].send_keys(Keys.ENTER, Keys.DOWN, Keys.ENTER)
        except:
            pass
        tags = div[0].find_elements_by_css_selector("textarea[rows='1']")
        tags[0].send_keys(self.tags)
        category = div[0].find_elements_by_css_selector(
            "label[aria-label=Category]")
        category[0].send_keys(Keys.ENTER, Keys.TAB, Keys.ENTER)
        condition = div[0].find_element_by_css_selector(
            "label[aria-label='Condition']")
        condition.send_keys(Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
        nextBtn = self.chromeWebdriver.find_element_by_css_selector(
            "div[aria-label='Next']")
        nextBtn.send_keys(Keys.ENTER)
        time.sleep(2.5)
        try:
            publishBtn = self.chromeWebdriver.find_element_by_css_selector(
                'div[aria-label="Publish"]')
            publishBtn.send_keys(Keys.ENTER)
        except:
            print(
                f"Listing did not publish for {postCode} with picture {self.filePath}")
            pass
        finally:
            if self.count >= 50:
                self.count = 1
            else:
                self.count += 1

            self.filePath = f"{details['path']}\\{self.folder}\\M-{self.count}.jpg"

    def logOutFacebook(self):
        self.chromeWebdriver.close()

    def publistListings(self):
        self.loginFaceBook(self.userInfo[0], self.userInfo[1])
        for postCode in self.postCodeList:
            if self.count <= self.listingCount:
                self.createListing(postCode)
            else:
                break
        self.logOutFacebook()
