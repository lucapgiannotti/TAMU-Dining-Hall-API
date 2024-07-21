from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_menu():
    url = 'https://dineoncampus.com/tamu/whats-on-the-menu/' 

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)
    wait = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-items"))
    )
    menu = driver.find_elements(By.CLASS_NAME, 'menu-items') 
    menu_items = []
    for element in menu:
        items = element.find_elements(By.TAG_NAME, 'strong')
        for item in items:
            menu_items.append(item.text)
    return menu_items
