import pytest
import time  # Import the time module
from playwright.sync_api import sync_playwright

def test_plr1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        context1 = context.new_page()
        context2 = context.new_page()
        context3 = context.new_page()
        context4 = context.new_page()
         
        context1.goto('https://supabets.com/')
        context2.goto('https://supabets.com')
        context3.goto('https://supabets.com')
        context4.goto('https://supabets.com')
        
        events1 = context1.query_selector_all('.plr_1')  # Fixed variable names
        events2 = context2.query_selector_all('.plr_1')
        events3 = context3.query_selector_all('.plr_1')
        events4 = context4.query_selector_all('.plr_1')
        print(events1)
        print(events2)
        print(events3)
        print(events4)
        #event1 = events1[0]  # Fixed variable names
        #event2 = events2[1]
        #event3 = events3[2]
        #event4 = events4[3]

       # c1 = event1.inner_text  # Removed parentheses
       # c2 = event2.inner_text
       # c3 = event3.inner_text
        c4 = event4.inner_text
        
      #  print(c1)
       # print(c2)
     #   print(c3)
     #   print(c4)
        
        time.sleep(5)
        browser.close()
