from playwright.sync_api import sync_playwright
import time
from thefuzz import fuzz
from thefuzz import process

def test_web1():
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")
        page.wait_for_selector('div[title="SOCCER"]').click()
        time.sleep(5)

        
        sub_events = page.query_selector_all('.subEvent')

        home_team = page.query_selector('.plr_1')
        away_team = page.query_selector('.plr_2')

        h2h_1 = page.query_selector(
            "//div[@class='oddType' and contains(text(), 'Home')]
)
        print(home_win)
        print(h2h_1)


   
       # home_names =  [home_team.inner_text() for home_team in home_teams[:3]]
      #  away_names =  [away_team.inner_text() for away_team in away_teams[:3]]

       # odds_values = [odd.inner_text() for odd in odds[:11]]  # Extracting only the first ten odds



      #  home_one = home_names[0]
      #  home_two = home_names[1]
     #   away_one = away_names[0]
     #   away_two = away_names[1]
      #  game_one = home_one + " v " + away_one
      #  game_two = home_two + " v " + away_two
        #games = {'eventId': game_one, 'home': odd_home, 'draw': odd_draw, 'away': odd_away}

      #  str1 = game_one
     #   str2 = game_two
     #   if fuzz.ratio(str1, str2) > 80:
      #      print("Strings are similar")
     #   else: 
     #       print("Strings don't match")
        
      #  print(" ")
      #  print("yeah motherfucker")

        browser.close()


#FC Augsburg v VfB Stuttgart

# Assume str1 and str2 are the strings to be compared
# str1 = game_one
# str2 = "Augsburg vs Stuttgart"

# Example of using fuzzywuzzy within a guarded clause
#if fuzz.ratio(str1, str2) > 80:
#    print("Strings are similar")
#else:
#    print("Strings are not similar")

