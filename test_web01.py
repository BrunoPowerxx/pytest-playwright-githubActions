from playwright.sync_api import sync_playwright
import time


def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")

        # Wait for the soccer tab to appear and click on it
        page.wait_for_selector('div[title="SOCCER"]').click()
        time.sleep(5)
        # Wait for the subEvents to load and count the number of games
        sub_events = page.query_selector_all('.subEvent')
        num_games = len(sub_events)
        print(f"Number of games found: {num_games}")
        print("yeah motherfucker") 
        browser.close()
