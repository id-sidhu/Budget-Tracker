from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys as sk
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from pytube import YouTube
import pygetwindow as gw
import keyboard as k
import schedule
import pyautogui
import time
import os

def get_active_window():
    return gw.getActiveWindow()

def now_playing():
    global current_video
    new_video = driver.current_url
    if new_video != current_video:
        clear_terminal()
        print(f"Now playing: {YouTube(new_video).title}")
        current_video = new_video

def play_song():
    if get_active_window() == current_window:
        search_query2 = input("Enter song or artist name: ").replace(" ", "+")
        if search_query2 == "":
            search_query2 = "latest songs"
        driver.get(f'https://www.youtube.com/results?search_query={search_query2}')
        first_video = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
                )
        first_video.click()
    else: 
        pass


def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def pause():
    if get_active_window() == current_window:
        pause_element = driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button']")
        pause_element.click()
        return ()
    else:
        pass

def play_next():
    if get_active_window() == current_window:
        next_elem = driver.find_element(By.XPATH, '//a[@class="ytp-next-button ytp-button"]')
        next_elem.click()
    else:
        pass

def incre_vol():
    if get_active_window() == current_window:
        pyautogui.press('volumeup')
    else:
        pass

def decre_vol():
    if get_active_window() == current_window:
        pyautogui.press('volumedown')
    else:
        pass

def quit_player():
    driver.close()


def mute():
    if get_active_window() == current_window:    
        mute_elem = driver.find_element(By.XPATH, "//button[@class='ytp-mute-button ytp-button']")
        mute_elem.click()
    else:
        pass

current_window = get_active_window()

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
chromedriver_path = "C:\\chromedriver\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path

driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
tk_root = tk.Tk()

try:
    button1 = tk.Button(tk_root, text="Play", command=pause)
    button2 = tk.Button(tk_root, text="Play Next", command=play_next)
    button3 = tk.Button(tk_root, text="Search", command=play_song)
    button4 = tk.Button(tk_root, text="Mute", command=mute)
    button5 = tk.Button(tk_root, text="Quit", command=quit_player)
    entry = tk.Entry()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    entry.pack()

    # query_from_tk = entry.get()
    # print(query_from_tk)
    search_query = input("Enter song or artist name: ").replace(" ", "+")
    if search_query == "":
            search_query = "latest songs"
    driver.get(f'https://www.youtube.com/results?search_query={search_query}')
    first_video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
            )
    first_video.click()
    current_video = driver.current_url
    print(f"Now playing: {YouTube(current_video).title}")

    schedule.every(5).seconds.do(now_playing)

    k.add_hotkey('space', pause)
    k.add_hotkey('shift+n', play_next)
    k.add_hotkey('up', incre_vol)
    k.add_hotkey('down', decre_vol)
    k.add_hotkey('shift+right', play_song)
    k.add_hotkey('shift+m', mute)
    k.add_hotkey('q', quit_player)

    tk_root.mainloop()

    while True:
        schedule.run_pending()
        time.sleep(3)
finally:
    driver.close()