import pandas as pd
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
from option import details

listingLinks = []


class Boost:
    def __init__(self, user, links):
        self.user = user
        self.links = links
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
        driver = webdriver.Chrome(
            details['chromePath'], chrome_options=options)
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
        for link in self.links:
            self.chromeWebdriver.get(link)
            try:
                # seeMoreBtn = self.chromeWebdriver.find_element_by_css_selector(
                #     'div[aria-label="See more"]')
                # seeMoreBtn.send_keys(Keys.ENTER)
                # time.sleep(.5)
                # seeMoreBtn = self.chromeWebdriver.find_element_by_css_selector(
                #     'div[aria-label="See more"]')
                # seeMoreBtn.send_keys(Keys.ENTER)
                # time.sleep(.5)
                # seeMoreBtn = self.chromeWebdriver.find_element_by_css_selector(
                #     'div[aria-label="See more"]')
                # seeMoreBtn.send_keys(Keys.ENTER)
                time.sleep(.5)
                listingDiv = self.chromeWebdriver.find_element_by_css_selector(
                    'div[style="max-width: 570px;"]')
                anchorTags = listingDiv.find_elements_by_tag_name('a')
                for link in anchorTags:
                    listingLinks.append(link.get_attribute('href'))
                    print(link.get_attribute('href'))
            except:
                pass
            finally:
                time.sleep(1)


def main(commereceLinks, user):
    user1 = Boost(user, commereceLinks)
    user1.loginFaceBook()
    user1.startBoosting()

    df = pd.DataFrame(listingLinks,
                      columns=['links'])
    return df


if __name__ == "__main__":
    main()
