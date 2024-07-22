from playwright.sync_api import sync_playwright
from selectors import *
import time


        # Wait for all elements matching 'div.row.eventRow'
        

        # Get all elements matching 'div.row.eventRow'
        

        # Process each event element
        for element in event_elements:
            # Example: Extract text from each event element
            text = element.text_content()
def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://betway.co.za/sport/basketball")
        time.sleep(3)
        page.screenshot(path='shot1.png', full_page=True)
        page.wait_for_selector('div.row.eventRow')
        events = page.query_selector_all('div.row.eventRow')
        quarters = []
        for event in events:
            event.click()
            print("event")
            #qtrs = page.wait_for_selector('span[data-translate-key="Quarters"]')
            #qtrs.click()
            #time.sleep(3)
            #page.screenshot(path='shot2.png', full_page=True)
            #qoe1 = page.wait_for_selector('span[data-translate-key="1StQuarterOddEven"]')
            #qoe1.click()
            #page.screenshot(path='shot4.png', full_page=True)
            
            
        browser.close()
