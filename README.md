# YouTube Automation with PyAutoGUI

This is a small Python automation script that can open and run any YouTube video automatically.  
It’s a learning project where I explored how to use the **[pyautogui](https://pyautogui.readthedocs.io/en/latest/)** library to control the mouse and keyboard for automation.  

---

## 📌 About the Project

I have been learning **AI Agents** and experimenting with **LangGraph** for automating workflows.  
Before jumping into complex AI workflows, I wanted to try something simple with Python automation.  

That’s where **pyautogui** comes in.  
- It can move the mouse, click, type, and press keyboard keys programmatically.  
- This script uses it to open a YouTube link and make sure the video starts playing.  

---

## ⚙️ Features
- Opens any YouTube URL you provide.  
- Waits for the browser to load.  
- Starts the video automatically using keystrokes.  
- Adds delays (`time.sleep`) to sync actions with the browser load time.  

---

## 🚀 How to Use

### 1. Clone the Repository
'''bash
git clone https://github.com/vikramlingam/pyautogui_youtube.git
cd pyautogui_youtube

---

### 2. Install Dependencies
Make sure you have Python 3.x installed. Then install the required package:

'''bash
pip install pyautogui

---

### 3. Run the Script
'''bash
python agent_1.py

---

You’ll be asked to enter a YouTube URL. The script will:
Open the link in your default browser.
Wait a few seconds for the page to load.
Use pyautogui to press play and run the video.

## 🖥️ Example
Enter the YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
The script will automatically open the browser and start the video.

### What’s Next
This project is just the first step.
In the next version, I’ll be exploring AI Agents that can:
Listen to context,
Decide on actions dynamically,
And perform tasks using LLMs and agentic workflows.
Stay tuned for that! 
