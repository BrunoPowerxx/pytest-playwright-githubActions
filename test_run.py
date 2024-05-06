from playwright.sync_api import sync_playwright
import time


def test_web1():
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")
        page.wait_for_selector('div[title="SOCCER"]').click()
        time.sleep(5)

        
        sub_events = page.query_selector_all('.subEvent')

        home_teams = page.query_selector_all('.plr_1')
        away_teams = page.query_selector_all('.plr_2')

        odds = page.query_selector_all('.oddValue')



        home_names =  [home_team.inner_text() for home_team in home_teams[:3]]
        away_names =  [away_team.inner_text() for away_team in away_teams[:3]]

        odds_values = [odd.inner_text() for odd in odds[:3]]  # Extracting only the first three odds



        home_one = home_names[0]
        home_two = home_names[1]
        home_three = home_names[2]

        away_one = away_names[0]
        away_two = away_names[1]
        away_three = away_names[2]

        odd_home = odds_values[0]
        odd_draw = odds_values[1]
        odd_away = odds_values[2]



        print(home_one)
        print(" v ")
        print(away_one)
        print(" ")

        print(home_two)
        print(" v ")
        print(away_two)
        print(" ")

        print(home_three)
        print(" v ")
        print(away_three)
        
        print(" ")
        print("yeah motherfucker")

        browser.close()
