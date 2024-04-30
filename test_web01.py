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
        team_home = page.query_selector('.plr_1').inner_text()
        team_away = page.query_selector('.plr_2').inner_text()
        odds = page.query_selector_all('.oddValue')
        odds_values = [odd.inner_text() for odd in odds[:3]]  # Extracting only the first three odds
        odd_home = odds_values[0]
        odd_draw = odds_values[1]
        odd_away = odds_values[2]

        print(team_home)
        print(odd_home)
        print(" ")
        print(team_away)
        print(odd_away)
        print(" ")
        print("draw")
        print(odd_draw)
        print(" ")
        print("yeah motherfucker") 
        browser.close()
