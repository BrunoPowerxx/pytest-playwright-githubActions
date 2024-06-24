from playwright.sync_api import sync_playwright
import time
from thefuzz import fuzz
from thefuzz import process

def test_web1():
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://betway.co.za")
        page.wait_for_selector('div[title="SOCCER"]').click()
        time.sleep(5)

        
        
        
        print(" ")
        print("yeah motherfucker")

        browser.close()
