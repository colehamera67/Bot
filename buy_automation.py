"""
RuneLite Buy Button Automation Script
Clicks the buy button and then clicks the 2nd step button
"""
import pyautogui
import time
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BUYING_DIR = os.path.join(SCRIPT_DIR, "Buying")

# Image paths
BUY_BUTTON_ACTIVE = os.path.join(BUYING_DIR, "buy_button_active.png")
BUY_BUTTON_INACTIVE = os.path.join(BUYING_DIR, "buy_button_inactive.png")
SECOND_STEP_BUTTON = os.path.join(BUYING_DIR, "2ndstep.png")

# Configuration
CONFIDENCE = 0.8  # Image matching confidence (0.0 to 1.0)
WAIT_TIME = 1.0   # Seconds to wait between actions


def find_and_click(image_path, button_name, retries=3):
    """
    Find an image on screen and click it.

    Args:
        image_path: Path to the button image
        button_name: Name of the button for logging
        retries: Number of times to retry finding the button

    Returns:
        True if clicked successfully, False otherwise
    """
    for attempt in range(retries):
        try:
            print(f"Looking for {button_name}... (attempt {attempt + 1}/{retries})")
            location = pyautogui.locateOnScreen(image_path, confidence=CONFIDENCE)

            if location:
                # Get the center of the button
                center = pyautogui.center(location)
                print(f"Found {button_name} at position: {center}")

                # Click the button
                pyautogui.click(center)
                print(f"Clicked {button_name} successfully!")
                return True
            else:
                print(f"{button_name} not found on screen")

        except Exception as e:
            print(f"Error finding {button_name}: {e}")

        if attempt < retries - 1:
            time.sleep(0.5)

    return False


def click_buy_button():
    """
    Clicks the buy button (tries both active and inactive versions).
    """
    print("\n=== Step 1: Clicking Buy Button ===")

    # Try to find the active buy button first
    if find_and_click(BUY_BUTTON_ACTIVE, "Buy Button (Active)"):
        return True

    # If not found, try the inactive version
    if find_and_click(BUY_BUTTON_INACTIVE, "Buy Button (Inactive)"):
        return True

    print("ERROR: Could not find buy button on screen!")
    return False


def click_second_step_button():
    """
    Clicks the 2nd step button after the buy button has been clicked.
    """
    print("\n=== Step 2: Clicking 2nd Step Button ===")

    if not os.path.exists(SECOND_STEP_BUTTON):
        print(f"ERROR: 2ndstep.png not found at: {SECOND_STEP_BUTTON}")
        print("Please add the 2ndstep.png image to the Buying folder.")
        return False

    # Give the interface time to transition to the 2nd step
    print(f"Waiting {WAIT_TIME} seconds for 2nd step to appear...")
    time.sleep(WAIT_TIME)

    # Try to find and click the 2nd step button
    if find_and_click(SECOND_STEP_BUTTON, "2nd Step Button"):
        return True

    print("ERROR: Could not find 2nd step button on screen!")
    return False


def main():
    """
    Main automation workflow.
    """
    print("="*50)
    print("RuneLite Buy Button Automation")
    print("="*50)

    # Step 1: Click the buy button
    if not click_buy_button():
        print("\n[FAILED] Could not complete Step 1")
        return

    # Step 2: Click the 2nd step button
    if not click_second_step_button():
        print("\n[FAILED] Could not complete Step 2")
        return

    print("\n" + "="*50)
    print("[SUCCESS] Automation completed successfully!")
    print("="*50)


if __name__ == "__main__":
    # Add a small delay to give user time to position windows
    print("Starting in 3 seconds... Position your RuneLite window now!")
    time.sleep(3)
    main()
