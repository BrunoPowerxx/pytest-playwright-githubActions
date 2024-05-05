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
        home_teams = page.query_selector_all('.plr_1')
        team_names =  [home_team.inner_text() for home_team in home_teams[:3]]
        game_one = team_names[0]
        game_two = team_names[1]
        game_three = team_names[2]
        
        odds = page.query_selector_all('.oddValue')
        odds_values = [odd.inner_text() for odd in odds[:3]]  # Extracting only the first three odds
        odd_home = odds_values[0]
        odd_draw = odds_values[1]
        odd_away = odds_values[2]

        print(game_one)
        print(game_two)
        print(game_three)
        print(" ")
        print("yeah motherfucker") 
        browser.close()
