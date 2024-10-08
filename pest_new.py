from playwright.sync_api import sync_playwright
from collections import namedtuple
#from selectors import *
import time

bw_url = "https://betway.co.za"
sb_url = "https://supabets.co.za"

bws_hl = "button#synapse_highlights"
#sb_tl = "a[data-istestfield='tabs-topleagues']"
#sb_tl = "div.TopLeagues"
sb_site = "Supabets"
bw_site = "Betway"

sb_sport = "li > a.sport"
bw_sport = "span[data-translate-key='Sport']"

sb_soccer = "div[title='SOCCER']"
bw_soccer = "li[data-translate-key='Soccer']"

bw_match = "div.row.eventRow label.ellips.theOtherFont"
sb_match = "plr_1.ng-binding"
sb_away = "plr_2.ng-binding"

#bw_event =
#sb_yt = ("div", has_text="Yes (GG)")
sb_yv = "div.oddValue:right-of(div[has_text='Yes (GG)'])"

bw_yt = "div[data-markettitle='Both Teams To Score'] span[data-translate-key='Yes']"
bw_yv = "div[data-markettitle='Both Teams To Score']:right-of(bw_yt)"

#sb_nt = ("div", has_text="No (NG)")
sb_nv = "div.oddValue:right-of(div[has_text='No (NG)'])"

bw_nt = "div[data-markettitle='Both Teams To Score'] span[data-translate-key='No']"
bw_nv = "div[data-markettitle='Both Teams To Score']:right-of(bw_nt)"

# takes inner text of odds as input
# calculates odds %% distribution
# percentages tuple in weight var 
# weight = ( , , )
Event = namedtuple('Event', ['site', 'GG', 'NG'])

def test_sb():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        page.screenshot(path='shot_one.png', full_page=True)
        #page.wait_for_selector(sb_sport).click()
        time.sleep(3)
        #sb_live.click()
        #page.wait_for_selector(sb_soccer).click()
        #page.wait_for_selector(sb_tl).click()
        page.screenshot(path='shot_two.png', full_page=True)
        #page.wait_for_selector(sb_match)
        fixtures = page.query_selector_all(sb_match)
        sb = []
        with open('output.txt', 'w') as file:
            for index, fixture in enumerate(fixtures):
                fixture.click()
                
                # Generate a unique filename for the screenshot
                screenshot_filename = f'shot_{index + 1}.png'
                page.screenshot(path=screenshot_filename, full_page=True)
                
                # Wait and retrieve values
                yes_val = page.wait_for_selector(sb_yv).inner_text()
                no_val = page.wait_for_selector(sb_nv).inner_text()
                
                # Create namedtuple and append to list
                game = Event(sb_site, yes_val, no_val)
                sb.append(game)
                
                # Write the game namedtuple attributes to the file
                file.write(f'Site: {game.site}\n')
                file.write(f'Yes Value: {game.GG}\n')
                file.write(f'No Value: {game.NG}\n')
                file.write('\n')  # Blank line for separation
        
        browser.close()
