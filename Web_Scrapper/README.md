# Brave YouTube Music Player

This project is a custom music player that uses Selenium with the Brave browser to search and play YouTube videos based on user input. It also provides a simple GUI using `tkinter` and uses keyboard hotkeys for controlling the player. The player features options to search for songs, pause/play, mute, change volume, and play the next video.

## Features

- **Search and Play YouTube Videos**: Search for a song or artist and play the first result on YouTube.
- **Simple GUI Control**: A `tkinter` GUI allows you to pause/play, mute, play the next video, and quit the player.
- **Keyboard Shortcuts**: Hotkeys for quick controls without using the GUI.
    - **Space**: Pause/Play
    - **Shift+N**: Play Next Video
    - **Up Arrow**: Increase Volume
    - **Down Arrow**: Decrease Volume
    - **Shift+Right Arrow**: Search for a new song
    - **Shift+M**: Mute/Unmute
    - **Q**: Quit Player
- **Auto-Display Current Video**: The terminal will automatically display the title of the currently playing video.

## Requirements

- **Python 3.x**
- **Brave Browser**: You must have Brave browser installed. Set the `brave_path` to its location.
- **Chromedriver**: Download the ChromeDriver that matches your Chrome version and set the `chromedriver_path`.
- **Libraries**:
    - `selenium`: Web automation tool
    - `pytube`: For extracting video titles
    - `tkinter`: GUI for player controls
    - `pygetwindow`: To get the active window
    - `keyboard`: To listen for keyboard events
    - `schedule`: For scheduling background tasks
    - `pyautogui`: For volume control

You can install the necessary libraries using:
pip install selenium pytube keyboard schedule pygetwindow pyautogui

## Setup and Configuration

1. **Download and Install Brave Browser**: Make sure Brave is installed on your machine.
2. **Download Chromedriver**: Download [Chromedriver](https://chromedriver.chromium.org/downloads) and set the path in the `chromedriver_path` variable.
3. **Update File Paths**: Set the `brave_path` to the correct location of your Brave browser's executable.

## How to Use

1. **Run the Script**: Execute the script using Python:
python3 adfree_music.py
2. **Search for a Song or Artist**: Once the program runs, it will prompt you to enter a song or artist to search for on YouTube.
3. **Control the Player**: Use the GUI buttons or the keyboard hotkeys to control the playback.

## Known Issues

- If there are issues with the search or playing videos, the terminal will display an error message.
- Hotkeys may not work if the active window is not the terminal or the `tkinter` GUI.

## Contributing

Feel free to fork this repository and make any improvements or add new features! Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
