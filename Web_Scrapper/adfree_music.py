from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import os

def now_playing():
    new_video = driver.current_url
    if new_video != current_video:
        clear_terminal()
        print(f"Now playing: {YouTube(new_video).title}")
    else:
        print(f"Now playing: {YouTube(current_video).title}")

def clear_terminal():
    if os.name() == "nt":
        os.system('cls')
    else:
        os.system('clear')
try:
    brave_path = "/opt/brave.com/brave/brave"
    chromedriver_path = "/usr/local/bin/chromedriver"

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path

    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)


    search_query = (input("Enter the title of song or singer name: "))
    if search_query == "":
        search_query = "latest songs"

    driver.get("https://youtube.com")

    search_box = driver.find_element('name', 'search_query')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
    )
    first_video.click()

    current_video = driver.current_url

    now_playing()

    input("Press any key to quit...")
finally:
    driver.quit()