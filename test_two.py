import pytest
from playwright.sync_api import sync_playwright

def test_web1():
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")
        page.wait_for_timeout(10000)  # Wait for 3 seconds

    # Click on the soccer option
        page.wait_for_selector('div[title="SOCCER"]').click()
        page.wait_for_timeout(10000)  # Wait for 3 seconds

    # Get and print home team text content
        home_team = page.query_selector('.plr_1')
        print("Home Team:", home_team.inner_text())

    # Click on the home team
        home_team.click()
        page.wait_for_timeout(10000)  # Wait for 3 seconds

    # Wait for the back button to appear
        page.wait_for_selector('span.btnBack')
        print("Back button text:", page.query_selector('span.btnBack').inner_text())

    # Click on the back button
        page.click('span.btnBack')
        page.wait_for_timeout(10000)  # Wait for 3 seconds

    # Print content of the soccer option button again
        print("Content of the soccer option button:", page.query_selector('div[title="SOCCER"]').inner_text())
