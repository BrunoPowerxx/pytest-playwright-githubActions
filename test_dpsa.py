import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

#timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")
        page.screenshot(path='shot_one.png', full_page=True)
        # highlight and fill job title input
        page.screenshot(path='shot_two.png', full_page=True)
        # highlight and fill location input
        page.screenshot(path='shot_three.png', full_page=True)
        browser.close()







#page.get_by_placeholder("Job title, keywords, or").fill("kill all leftists")        
#page.get_by_placeholder("City, state, zip code, or \"").fill("upington")
#page.get_by_role("button", name="Find jobs").click()
#page.goto("https://za.indeed.com/")
