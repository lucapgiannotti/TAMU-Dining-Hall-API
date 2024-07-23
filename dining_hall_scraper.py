from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def dining_hall_web_scraper(dining_hall, meal):
    url = 'https://dineoncampus.com/tamu/whats-on-the-menu/'
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("window-size=1920x1080")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

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
    
    if dining_hall == "commons":
        click_dining_hall_button("The Commons Dining Hall (South Campus)")
    
    elif dining_hall == "sbisa":
        click_dining_hall_button("Sbisa Dining Hall (North Campus)")
    
    elif dining_hall == "duncan":
        click_dining_hall_button("Duncan Dining Hall (South Campus/Quad)")
        
    wait = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, meal))  
    )
    
    button = driver.find_element(By.LINK_TEXT, meal)
    button.click()
    
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-items"))
    )
    menu = driver.find_elements(By.CLASS_NAME, 'menu-items') 
    menu_items = []
    for element in menu:
        items = element.find_elements(By.TAG_NAME, 'strong')
        for item in items:
            menu_items.append(item.text)
    return menu_items