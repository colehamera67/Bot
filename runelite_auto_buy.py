#!/usr/bin/env python3
"""
RuneLite Auto Buy Button Clicker
Automatically finds and clicks the active buy button in RuneLite
"""

import pyautogui
import time
import sys
from pathlib import Path

# Configure pyautogui
pyautogui.FAILSAFE = True  # Move mouse to corner to abort
pyautogui.PAUSE = 0.1  # Small pause between actions

# Paths to button images
SCRIPT_DIR = Path(__file__).parent
ACTIVE_BUTTON_IMG = SCRIPT_DIR / "Buying" / "buy_button_active.png"
INACTIVE_BUTTON_IMG = SCRIPT_DIR / "Buying" / "buy_button_inactive.png"

def find_active_button(confidence=0.8):
    """
    Searches for the active buy button on screen

    Args:
        confidence (float): Matching confidence level (0.0 to 1.0)

    Returns:
        tuple: (x, y) coordinates of button center, or None if not found
    """
    try:
        # Search for the active button
        location = pyautogui.locateOnScreen(str(ACTIVE_BUTTON_IMG), confidence=confidence)

        if location:
            # Get center coordinates
            center = pyautogui.center(location)
            return center
        return None
    except pyautogui.ImageNotFoundException:
        return None
    except Exception as e:
        print(f"Error finding button: {e}")
        return None

def click_buy_button():
    """
    Finds and clicks the active buy button

    Returns:
        bool: True if button was found and clicked, False otherwise
    """
    print("Searching for active buy button...")

    # Try to find the button
    button_pos = find_active_button()

    if button_pos:
        x, y = button_pos
        print(f"Found active button at ({x}, {y})")

        # Click the button
        pyautogui.click(x, y)
        print("Clicked buy button!")
        return True
    else:
        print("Active buy button not found on screen")
        return False

def continuous_mode(interval=1.0, max_clicks=None):
    """
    Continuously searches for and clicks the buy button

    Args:
        interval (float): Time in seconds to wait between searches
        max_clicks (int): Maximum number of clicks (None for unlimited)
    """
    print("\n" + "="*50)
    print("CONTINUOUS MODE ACTIVATED")
    print("="*50)
    print(f"Search interval: {interval}s")
    print(f"Max clicks: {'Unlimited' if max_clicks is None else max_clicks}")
    print("\nMove mouse to top-left corner to abort (FAILSAFE)")
    print("Press Ctrl+C to stop\n")

    clicks = 0

    try:
        while True:
            if max_clicks and clicks >= max_clicks:
                print(f"\nReached maximum clicks ({max_clicks}). Stopping.")
                break

            if click_buy_button():
                clicks += 1
                print(f"Total clicks: {clicks}\n")

            time.sleep(interval)

    except KeyboardInterrupt:
        print(f"\n\nStopped by user. Total clicks: {clicks}")
    except pyautogui.FailSafeException:
        print(f"\n\nFAILSAFE triggered! Total clicks: {clicks}")

def single_click_mode():
    """
    Searches once and clicks if found
    """
    print("\n" + "="*50)
    print("SINGLE CLICK MODE")
    print("="*50)

    if click_buy_button():
        print("\nSuccess!")
    else:
        print("\nFailed to find button.")
        sys.exit(1)

def main():
    """Main function"""

    # Check if image files exist
    if not ACTIVE_BUTTON_IMG.exists():
        print(f"ERROR: Active button image not found at {ACTIVE_BUTTON_IMG}")
        sys.exit(1)

    print("RuneLite Auto Buy Button Clicker")
    print("=" * 50)
    print("\nOptions:")
    print("1. Single click (find and click once)")
    print("2. Continuous mode (keep clicking)")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        single_click_mode()
    elif choice == "2":
        try:
            interval = float(input("Enter interval between searches (seconds, default 1.0): ").strip() or "1.0")
        except ValueError:
            interval = 1.0

        max_clicks_input = input("Enter max clicks (leave empty for unlimited): ").strip()
        max_clicks = int(max_clicks_input) if max_clicks_input else None

        continuous_mode(interval=interval, max_clicks=max_clicks)
    elif choice == "3":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice!")
        sys.exit(1)

if __name__ == "__main__":
    main()
