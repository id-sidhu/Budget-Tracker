from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

brave_path = "/opt/brave.com/brave/brave"
chromedriver_path = "/usr/local/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = brave_path

driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

try:
    search_query = (input("Enter the title of song or singer name: "))
    driver.get("https://youtube.com")

    search_box = driver.find_element('name', 'search_query')

    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
    )
    first_video.click()
    input("Press any key to quit the browser...")
finally:
    driver.quit()
