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
import pandas as pd
import linkGrabber
from option import details


class Boost:
    def __init__(self, user, links):
        self.user = user
        self.links = links
        self.path = details['chromePath']
        self.chromeWebdriver = self.setupChrome()

    def setupChrome(self):
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        options = webdriver.ChromeOptions()
        #options.add_experimental_option("mobileEmulation", mobile_emulation)
        # options.add_argument('headless')
        options.add_argument('windows-size=800*600')
        # Add your ChromeWebdriver Path
        driver = webdriver.Chrome(self.path, chrome_options=options)
        params = dict({
            "latitude": 51.507351,
            "longitude": -0.127758,
            "accuracy": 100
        })
        driver.execute_cdp_cmd("Emulation.clearGeolocationOverride", params)
        return driver

    def loginFaceBook(self,):
        self.chromeWebdriver.get(
            'https://en-gb.facebook.com/marketplace/london')
        time.sleep(1.5)
        self.chromeWebdriver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[1]/label/input').send_keys(self.user[0])
        self.chromeWebdriver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/label/input').send_keys(self.user[1])
        self.chromeWebdriver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[3]/div/div/div[1]/div/span/span').click()
        time.sleep(1.5)

    def startBoosting(self):
        for link in self.links['links']:
            self.chromeWebdriver.get(link)
            try:
                clickBtn = self.chromeWebdriver.find_element_by_css_selector(
                    'div[aria-label="Send"]')
                SaveBtn = self.chromeWebdriver.find_element_by_css_selector(
                    'div[aria-label="Save"]')
                self.chromeWebdriver.execute_script(
                    "arguments[0].click();", SaveBtn)
                time.sleep(.5)
                self.chromeWebdriver.execute_script(
                    "arguments[0].click();", clickBtn)
            except Exception as e:
                print(e)
                # clickBtn.send_keys(Keys.ENTER)
                pass
            finally:
                time.sleep(1.5)


def main(users, links):
    linkGrabber.main(links, users[0])
    df = pd.read_csv('boostinglinks.csv')
    for user in users:
        userObj = Boost(user, df)
        userObj.loginFaceBook()
        userObj.startBoosting()
        userObj.chromeWebdriver.close()
