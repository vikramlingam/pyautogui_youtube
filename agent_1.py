#import necessary libraries for this automation
import pyautogui
import webbrowser
import urllib.parse
import time

class YouTubeAgent:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 1
        
    def play_youtube_video(self, query):
        """Direct YouTube search and play"""
        try:
            # Create YouTube search URL
            search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            
            print(f"Opening: {search_url}")
            webbrowser.open(search_url)
            
            # Wait for page to load
            time.sleep(4)
            
            # Click on first video
            # You may need to adjust these based on your screen resolution
            first_video_x = 360
            first_video_y = 290
            
            pyautogui.click(first_video_x, first_video_y)
            print(f"Playing: {query}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def control_playback(self, action):
        """Control YouTube playback"""
        if action == "pause" or action == "play":
            pyautogui.press('space')  
        elif action == "fullscreen":
            pyautogui.press('f')
        elif action == "volume_up":
            pyautogui.press('up')
        elif action == "volume_down":
            pyautogui.press('down')

# Simple usage
if __name__ == "__main__":
    agent = YouTubeAgent()
    
    # Example: play a video on youtube - update this to anything you want this code to action
    agent.play_youtube_video("virat kohli last over vs pakistan")
    
    # Wait for few seconds
    time.sleep(5)
    agent.control_playback("pause")
