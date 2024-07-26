from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time




def dining_hall_web_scraper(dining_hall, meal):
    start_time = time.time()

    url = 'https://dineoncampus.com/tamu/whats-on-the-menu/'
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("window-size=1920x1080")

    driver_path = ChromeDriverManager().install()
    if driver_path:
        driver_name = os.path.basename(driver_path)
        if driver_name != "chromedriver.exe":
            driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
            
    driver = webdriver.Chrome(service=ChromeService(driver_path), options=chrome_options)

    driver.get(url)
    
           
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
    except:
        return "Menu not available; error finding dining hall", 404
    
    try:    
        wait = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, meal))  
        )
        
        button = driver.find_element(By.LINK_TEXT, meal)
        button.click()
        
        try:
            WebDriverWait(driver, 2).until( # Redneck engineering solution to ensure the page loads before it scrapes
            EC.staleness_of(button) #   Ideally there should be a better way, but this will do for now
            )
        except:
            pass
    except:
        return "Menu not available; error finding meal type (breakfast/lunch/dinner)", 404
        
    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "menu-items"))
        )
    except:
        return "Menu not available; error finding menu", 404
    menu = driver.find_elements(By.CLASS_NAME, 'menu-items') 
    menu_items = list(map(lambda element: element.find_elements(By.TAG_NAME, 'strong'), menu))
    menu_items = [item.text for sublist in menu_items for item in sublist]
    
    execution_time = round(time.time() - start_time, 4)
            
    return menu_items, f"{execution_time} seconds to scrape"


current_os = os.name
print(current_os)