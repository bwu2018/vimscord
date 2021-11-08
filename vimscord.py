from CREDENTIALS import *

from os import system, name
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from typing import List

driver = webdriver.Chrome()

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def main():
    driver.get("https://discord.com/login")

    driver.find_element_by_name("email").send_keys(EMAIL)
    driver.find_element_by_name("password").send_keys(PASSWORD)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)

    while True:
        unread_badges = driver.find_elements_by_xpath("//div[contains(@class, 'numberBadge')]")
        n_unreads = []
        for badge in unread_badges:
            n_unreads.append(int(badge.text))

        unread_users = driver.find_elements_by_xpath("//a[contains(@aria-label, 'unread')]")
        usernames = []
        links = []
        for user in unread_users:
            usernames.append(user.get_attribute("aria-label").split()[1])
            links.append(user.get_attribute("href"))

        for n_unread, username, link in zip(n_unreads, usernames, links):
            driver.get(link)
            time.sleep(3)
            print(f"======== {username}({n_unread}) ========")
            # Gets 50 messages
            messages = driver.find_elements_by_xpath("//div[contains(@class, 'messageContent-2qWWxC')]")
            for message in messages[-n_unread:]:
                print(message.text)
            # Mark as read
            driver.find_element_by_xpath(f"//a[contains(@aria-label, '{username}')]").click()
            print()
            print()
        driver.get("https://discord.com/channels/@me")
        time.sleep(5)
        

    # Text area: slateTextArea-1Mkdgw

if __name__ == "__main__":
    main()