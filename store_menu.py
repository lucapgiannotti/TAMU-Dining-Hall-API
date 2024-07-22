import sched
import time
from threading import Thread
from web_scraper import web_scraper

menu_data = {
    "breakfast": [],
    "lunch": [],
    "dinner": []
}

scheduler = sched.scheduler(time.time, time.sleep)

def scrape_and_store():
    menu_data["breakfast"] = web_scraper("__BVID__217___BV_tab_button__")
    menu_data["lunch"] = web_scraper("__BVID__222___BV_tab_button__")
    menu_data["dinner"] = web_scraper("__BVID__227___BV_tab_button__")
    scheduler.enter(1800, 1, scrape_and_store)

scrape_and_store()
Thread(target=scheduler.run).start()

def breakfast_menu():
    return menu_data["breakfast"]

def lunch_menu():
    return menu_data["lunch"]

def dinner_menu():
    return menu_data["dinner"]