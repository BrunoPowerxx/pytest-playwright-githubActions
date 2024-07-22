from playwright.sync_api import sync_playwright
from selectors import *
import time



def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://betway.co.za/sport/basketball")
        time.sleep(3)
        page.screenshot(path='shot1.png', full_page=True)
        events = page.query_selector_all("label[data-translate-type='event' and data-translate-set='Basketball']")
        quarters = []
        for event in events:
            event.click()
            qtrs = page.wait_for_selector('span[data-translate-key="Quarters"]')
            qtrs.click()
            time.sleep(3)
            page.screenshot(path='shot2.png', full_page=True)
            qoe1 = page.wait_for_selector('span[data-translate-key="1StQuarterOddEven"]')
            qoe1.click()
            page.screenshot(path='shot4.png', full_page=True)
            
            
        browser.close()
