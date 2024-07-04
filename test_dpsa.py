import time
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
screenshot_path = f"screenshot_{timestamp}.png"
indeed = 'https://za.indeed.com/'

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://za.indeed.com/")
        page.screenshot(path="screenshot.png", full_page=True)
        #page.get_by_placeholder("Job title, keywords, or").fill("kill all leftists")        
        #page.get_by_placeholder("City, state, zip code, or \"").fill("upington")
        #page.get_by_role("button", name="Find jobs").click()
        #page.goto("https://za.indeed.com/")
        browser.close()
