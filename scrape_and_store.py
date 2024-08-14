import sched, time, os
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def initalize_driver():
    current_os = os.name    
    url = 'https://dineoncampus.com/tamu/whats-on-the-menu/'
    
    chrome_options = Options()
    if current_os == "nt":
        driver_path = ChromeDriverManager().install()
        if driver_path:
            driver_name = os.path.basename(driver_path)
            if driver_name != "chromedriver.exe":
                driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
    else:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920x1080")
        driver_path = ChromeDriverManager().install()
            
    driver = webdriver.Chrome(service=ChromeService(driver_path), options=chrome_options)
    driver.get(url)

    return driver

def switch_window_and_scrape(driver, dining_hall, meal):
	start_time = time.time()
	wait = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, "menu-location-selector__BV_toggle_"))
	)
	menu_location_selector_button = driver.find_element(By.ID, "menu-location-selector__BV_toggle_")
	menu_location_selector_button.click()

	def click_dining_hall_button(dining_hall_name):
		xpath = f"//button[contains(text(), '{dining_hall_name}')]"
		wait = WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, xpath))
		)
		button = driver.find_element(By.XPATH, xpath)
		button.click()

	try:
		if dining_hall == "commons":
			click_dining_hall_button("The Commons Dining Hall (South Campus)")
		
		elif dining_hall == "sbisa":
			click_dining_hall_button("Sbisa Dining Hall (North Campus)")
		
		elif dining_hall == "duncan":
			click_dining_hall_button("Duncan Dining Hall (South Campus/Quad)")
	except Exception as e:
		print(f"Error finding dining hall: {e}")
		return "Menu not available; error finding dining hall", 404

	try:    
		wait = WebDriverWait(driver, 3).until(
			EC.element_to_be_clickable((By.LINK_TEXT, meal))  
		)
		
		button = driver.find_element(By.LINK_TEXT, meal)
		button.click()
            

	except Exception as e:
		print(f"Error finding meal type: {e}")
		return "Menu not available; error finding meal type (breakfast/lunch/dinner)", 404
		
	try:
		WebDriverWait(driver, 2).until( # Redneck engineering solution to ensure the page loads before it scrapes
		EC.staleness_of(button) #   Ideally there should be a better way, but this will do for now
			)
	except:
		pass

	try:
		wait = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.CLASS_NAME, "menu-items"))
		)
	except Exception as e:
		print(f"Error finding menu: {e}")
		return "Menu not available; error finding menu", 404

	menu = driver.find_elements(By.CLASS_NAME, 'menu-items')
	if not menu:
		print("No menu items found")
	else:
		print(f"Found {len(menu)} menu items")

	menu_items = list(map(lambda element: element.find_elements(By.TAG_NAME, 'strong'), menu))
	if not menu_items:
		print("No strong tags found in menu items")
	else:
		print(f"Found {len(menu_items)} strong tags in menu items")

	menu_items = [item.text for sublist in menu_items for item in sublist]
	if not menu_items:
		print("No text found in menu items")
	else:
		print(f"Extracted text from menu items: {menu_items}")

	execution_time = round(time.time() - start_time, 4)
			
	return menu_items, f"{execution_time} seconds to scrape"


def scrape_and_store():
    driver = initalize_driver()
    dining_halls = ["commons", "sbisa", "duncan"]
    meal_types = ["breakfast", "lunch", "dinner"]

    for dining_hall in dining_halls:
        for meal_name in meal_types:
            if meal_name == "breakfast":
                meal = "Breakfast"
            elif meal_name == "lunch":
                meal = "Lunch"
            elif meal_name == "dinner":
                meal = "Dinner"
                
            menu_data[dining_hall][meal_name] = switch_window_and_scrape(driver, dining_hall, meal)

    driver.quit()
    scheduler.enter(1800, 1, scrape_and_store)  # 1800 seconds = 30 minutes

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