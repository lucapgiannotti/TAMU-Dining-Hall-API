import sched
import time
from threading import Thread
from dining_hall_scraper import dining_hall_web_scraper

menu_data = {
    "commons": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    },
    "sbisa": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    },
    "duncan": {
        "breakfast": [],
        "lunch": [],
        "dinner": []
    },
}

scheduler = sched.scheduler(time.time, time.sleep)

def scrape_and_store():
    menu_data["commons"]["breakfast"] = dining_hall_web_scraper("commons", "Breakfast")
    menu_data["commons"]["lunch"] = dining_hall_web_scraper("commons", "Lunch")
    menu_data["commons"]["dinner"] = dining_hall_web_scraper("commons", "Dinner")
    
    # menu_data["sbisa"]["breakfast"] = dining_hall_web_scraper("sbisa", "")
    menu_data["sbisa"]["lunch"] = dining_hall_web_scraper("sbisa", "Lunch")
    # menu_data["sbisa"]["dinner"] = dining_hall_web_scraper("sbisa", "")
    
    # menu_data["duncan"]["breakfast"] = dining_hall_web_scraper("duncan", "")
    # menu_data["duncan"]["lunch"] = dining_hall_web_scraper("duncan", "")
    # menu_data["duncan"]["dinner"] = dining_hall_web_scraper("duncan", "")

    scheduler.enter(1800, 1, scrape_and_store) # 1800 seconds = 30 minutes

scrape_and_store()
Thread(target=scheduler.run).start()

def breakfast_menu(dining_hall):
    if dining_hall == "commons":
        return menu_data["commons"]["breakfast"]
    if dining_hall == "sbisa":
        return menu_data["sbisa"]["breakfast"]
    if dining_hall == "duncan":
        return menu_data["duncan"]["breakfast"]
    else:
        return "Internal server error", 500
    
def lunch_menu(dining_hall):
    if dining_hall == "commons":
        return menu_data["commons"]["lunch"]
    if dining_hall == "sbisa":
        return menu_data["sbisa"]["lunch"]
    if dining_hall == "duncan":
        return menu_data["duncan"]["lunch"]
    else:
        return "Internal server error", 500

def dinner_menu(dining_hall):
    if dining_hall == "commons":
        return menu_data["commons"]["dinner"]
    if dining_hall == "sbisa":
        return menu_data["sbisa"]["dinner"]
    if dining_hall == "duncan":
        return menu_data["duncan"]["dinner"]
    else:
        return "Internal server error", 500