from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import tkinter as tk
import pygetwindow as gw
import keyboard as k
import schedule
import pyautogui
import time
import os

current_video = None
driver = None

def get_active_window():
    return gw.getActiveWindow()

current_window = get_active_window()
def now_playing():
    global current_video
    new_video = driver.current_url
    if new_video != current_video:
        clear_terminal()
        print(f"Now playing: {YouTube(new_video).title}")
        current_video = new_video

def play_song():
    search_query2 = input("Enter song or artist: ").replace(" ", "+")
    if not search_query2:
        search_query2 = "latest songs"
    print(f"Searching for: {search_query2}")
    driver.get(f'https://www.youtube.com/results?search_query={search_query2}')
    try:
        first_video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
        )
        first_video.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ytd-player[@id='ytd-player']"))
        )
        current_video = driver.current_url
        print(f"Now playing: {YouTube(current_video).title}")
    except Exception as e:
        print(f"Error during search or play: {e}")

def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def get_tkinter_window():
    return(gw.getActiveWindow())

def pause():
    # if get_active_window() == current_window or get_active_window() == get_tkinter_window:
        pause_element = driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button']")
        pause_element.click()
        return ()
    # else:
        pass

def play_next():
    # if get_active_window() == current_window or get_active_window() == get_tkinter_window:
        next_elem = driver.find_element(By.XPATH, '//a[@class="ytp-next-button ytp-button"]')
        next_elem.click()
    # else:
        pass

def incre_vol():
    if get_active_window() == current_window or get_active_window() == get_tkinter_window:
        pyautogui.press('volumeup')
    else:
        pass

def decre_vol():
    if get_active_window() == current_window or get_active_window() == get_tkinter_window:
        pyautogui.press('volumedown')
    else:
        pass

def quit_player():
    driver.close()


def mute():
    # if get_active_window() == current_window or get_active_window() == get_tkinter_window:    
        mute_elem = driver.find_element(By.XPATH, "//button[@class='ytp-mute-button ytp-button']")
        mute_elem.click()
    # else:
        # pass

def setup_driver():
    global driver
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    chromedriver_path = "C:\\chromedriver\\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

def main():
    setup_driver()
    play_song()
    print("Setting up driver...")
    tk_root = tk.Tk()
    # entry = tk.Entry(tk_root)
    button1 = tk.Button(tk_root, text="Pause/Play", command=pause)
    button2 = tk.Button(tk_root, text="Play Next", command=play_next)
    button3 = tk.Button(tk_root, text="Search", command=play_song)
    button4 = tk.Button(tk_root, text="Mute", command=mute)
    button5 = tk.Button(tk_root, text="Quit", command=quit_player)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    print("Setting up GUI...")
    schedule.every(5).seconds.do(now_playing)

    k.add_hotkey('space', pause)
    k.add_hotkey('shift+n', play_next)
    k.add_hotkey('up', incre_vol)
    k.add_hotkey('down', decre_vol)
    k.add_hotkey('shift+right', play_song)
    k.add_hotkey('shift+m', mute)
    k.add_hotkey('q', quit_player)

    print('mainloop starting')

    tk_root.mainloop()
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        if driver:
            driver.close()

if __name__ == "__main__":
    main()