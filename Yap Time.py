import pystray
import time
import datetime
import os
from PIL import Image

def on_exit(icon):
    icon.stop()
    os._exit(0)


def create_tray_icon():
    # Create the icon
    icon_image = Image.open(r'E:\Projects\Yap Time\money.png')
    
    # Create menu items
    menu = pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    )
    
    # Create the icon with menu
    icon = pystray.Icon(
        name="YapTime",
        icon=icon_image,
        title="Yap Time Reminder",
        menu=menu
    )
    
    return icon

def notify(message):
    # Existing notify code...
    print('\n' * 2)
    print('=' * 50)
    print(message)
    print('=' * 50)
    print('\n' * 2)

def main(icon):
    while True:
        now = datetime.datetime.now()
        
        # Check for 2 PM
        if now.hour == 14 and now.minute == 0:
            notify("🐦 Time to Yap! It's 2:00 PM!")
            time.sleep(60)
            
        # Check for 6 PM
        if now.hour == 18 and now.minute == 0:
            notify("🐦 Time to Yap! It's 6:00 PM!")
            time.sleep(60)
            
        time.sleep(30)

if __name__ == "__main__":
    print("Tweet reminder started! You'll be notified at 2 PM and 6 PM.")
    print("Keep this script running to receive notifications.")
    print("Press Ctrl+C to stop")
    
    icon = create_tray_icon()
    
    # Run the icon in a separate thread
    icon.run_detached()
    
    try:
        main(icon)
    except KeyboardInterrupt:
        icon.stop()
        print("\nTweet reminder stopped!")