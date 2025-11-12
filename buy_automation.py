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
THIRD_STEP_BUTTON = os.path.join(BUYING_DIR, "3rdstep.png")
FOURTH_STEP_BUTTON = os.path.join(BUYING_DIR, "4thstep.png")

# Configuration
CONFIDENCE = 0.7  # Image matching confidence (0.0 to 1.0) - lowered for better matching
WAIT_TIME = 2.5   # Seconds to wait between actions - increased for 2nd step to load
SECOND_STEP_RETRIES = 10  # More retries for 2nd step button


def find_and_click(image_path, button_name, retries=3, confidence=None, wait_between=0.5):
    """
    Find an image on screen and click it.

    Args:
        image_path: Path to the button image
        button_name: Name of the button for logging
        retries: Number of times to retry finding the button
        confidence: Override confidence level (uses CONFIDENCE if None)
        wait_between: Seconds to wait between retry attempts

    Returns:
        True if clicked successfully, False otherwise
    """
    if confidence is None:
        confidence = CONFIDENCE

    for attempt in range(retries):
        try:
            print(f"Looking for {button_name}... (attempt {attempt + 1}/{retries}) [confidence: {confidence}]")

            # Check if image file exists
            if not os.path.exists(image_path):
                print(f"ERROR: Image file not found: {image_path}")
                return False

            location = pyautogui.locateOnScreen(image_path, confidence=confidence)

            if location:
                # Get the center of the button
                center = pyautogui.center(location)
                print(f"✓ Found {button_name} at position: {center}")

                # Click the button
                pyautogui.click(center)
                print(f"✓ Clicked {button_name} successfully!")
                return True
            else:
                print(f"✗ {button_name} not found on screen (attempt {attempt + 1}/{retries})")

        except Exception as e:
            print(f"✗ Error finding {button_name}: {e}")

        if attempt < retries - 1:
            print(f"  Waiting {wait_between}s before retry...")
            time.sleep(wait_between)

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

    # Try to find and click the 2nd step button with more retries and lower confidence
    print(f"Attempting to find 2nd step button ({SECOND_STEP_RETRIES} retries)...")

    # First try with normal confidence
    if find_and_click(SECOND_STEP_BUTTON, "2nd Step Button",
                     retries=SECOND_STEP_RETRIES,
                     confidence=CONFIDENCE,
                     wait_between=1.0):
        return True

    # If that fails, try with even lower confidence
    print("\n⚠ First attempt failed. Trying with lower confidence (0.6)...")
    if find_and_click(SECOND_STEP_BUTTON, "2nd Step Button (Low Confidence)",
                     retries=5,
                     confidence=0.6,
                     wait_between=1.0):
        return True

    # Final attempt with very low confidence
    print("\n⚠ Second attempt failed. Final try with very low confidence (0.5)...")
    if find_and_click(SECOND_STEP_BUTTON, "2nd Step Button (Very Low Confidence)",
                     retries=3,
                     confidence=0.5,
                     wait_between=1.5):
        return True

    print("\n❌ ERROR: Could not find 2nd step button on screen after all attempts!")
    print("Troubleshooting tips:")
    print("  1. Make sure the 2nd step dialog/window is visible")
    print("  2. Check that 2ndstep.png matches the button on screen")
    print("  3. Try taking a new screenshot of the button")
    print("  4. Make sure the button is not obscured or off-screen")
    return False


def click_third_step_button():
    """
    Clicks the 3rd step button after the 2nd step has been clicked.
    """
    print("\n=== Step 3: Clicking 3rd Step Button ===")

    if not os.path.exists(THIRD_STEP_BUTTON):
        print(f"ERROR: 3rdstep.png not found at: {THIRD_STEP_BUTTON}")
        print("Please add the 3rdstep.png image to the Buying folder.")
        return False

    # Give the interface time to transition to the 3rd step
    print(f"Waiting {WAIT_TIME} seconds for 3rd step to appear...")
    time.sleep(WAIT_TIME)

    # Try to find and click the 3rd step button with more retries and lower confidence
    print(f"Attempting to find 3rd step button ({SECOND_STEP_RETRIES} retries)...")

    # First try with normal confidence
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button",
                     retries=SECOND_STEP_RETRIES,
                     confidence=CONFIDENCE,
                     wait_between=1.0):
        return True

    # If that fails, try with even lower confidence
    print("\n⚠ First attempt failed. Trying with lower confidence (0.6)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button (Low Confidence)",
                     retries=5,
                     confidence=0.6,
                     wait_between=1.0):
        return True

    # Final attempt with very low confidence
    print("\n⚠ Second attempt failed. Final try with very low confidence (0.5)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button (Very Low Confidence)",
                     retries=3,
                     confidence=0.5,
                     wait_between=1.5):
        return True

    print("\n❌ ERROR: Could not find 3rd step button on screen after all attempts!")
    print("Troubleshooting tips:")
    print("  1. Make sure the 3rd step dialog/window is visible")
    print("  2. Check that 3rdstep.png matches the button on screen")
    print("  3. Try taking a new screenshot of the button")
    print("  4. Make sure the button is not obscured or off-screen")
    return False


def click_fourth_step_button():
    """
    Clicks the 4th step button after the 3rd step has been clicked.
    """
    print("\n=== Step 4: Clicking 4th Step Button ===")

    if not os.path.exists(FOURTH_STEP_BUTTON):
        print(f"ERROR: 4thstep.png not found at: {FOURTH_STEP_BUTTON}")
        print("Please add the 4thstep.png image to the Buying folder.")
        return False

    # Give the interface time to transition to the 4th step
    print(f"Waiting {WAIT_TIME} seconds for 4th step to appear...")
    time.sleep(WAIT_TIME)

    # Try to find and click the 4th step button with more retries and lower confidence
    print(f"Attempting to find 4th step button ({SECOND_STEP_RETRIES} retries)...")

    # First try with normal confidence
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button",
                     retries=SECOND_STEP_RETRIES,
                     confidence=CONFIDENCE,
                     wait_between=1.0):
        return True

    # If that fails, try with even lower confidence
    print("\n⚠ First attempt failed. Trying with lower confidence (0.6)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button (Low Confidence)",
                     retries=5,
                     confidence=0.6,
                     wait_between=1.0):
        return True

    # Final attempt with very low confidence
    print("\n⚠ Second attempt failed. Final try with very low confidence (0.5)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button (Very Low Confidence)",
                     retries=3,
                     confidence=0.5,
                     wait_between=1.5):
        return True

    print("\n❌ ERROR: Could not find 4th step button on screen after all attempts!")
    print("Troubleshooting tips:")
    print("  1. Make sure the 4th step dialog/window is visible")
    print("  2. Check that 4thstep.png matches the button on screen")
    print("  3. Try taking a new screenshot of the button")
    print("  4. Make sure the button is not obscured or off-screen")
    return False


def main():
    """
    Main automation workflow.
    """
    print("="*50)
    print("RuneLite Buy Button Automation v3.0")
    print("="*50)
    print(f"Configuration:")
    print(f"  - Confidence: {CONFIDENCE}")
    print(f"  - Wait time: {WAIT_TIME}s")
    print(f"  - Step retries: {SECOND_STEP_RETRIES}")
    print(f"  - Total steps: 4 (Buy → 2nd → 3rd → 4th)")
    print("="*50)

    # Step 1: Click the buy button
    if not click_buy_button():
        print("\n❌ [FAILED] Could not complete Step 1 - Buy button not clicked")
        return

    print("\n✓ Step 1 completed successfully!")

    # Step 2: Click the 2nd step button
    if not click_second_step_button():
        print("\n❌ [FAILED] Could not complete Step 2 - 2nd step button not clicked")
        print("\n💡 Make sure:")
        print("   - The 2ndstep.png file exists in the Buying folder")
        print("   - The 2nd step window/dialog is visible on screen")
        print("   - The button image in 2ndstep.png matches what's on screen")
        return

    print("\n✓ Step 2 completed successfully!")

    # Step 3: Click the 3rd step button
    if not click_third_step_button():
        print("\n❌ [FAILED] Could not complete Step 3 - 3rd step button not clicked")
        print("\n💡 Make sure:")
        print("   - The 3rdstep.png file exists in the Buying folder")
        print("   - The 3rd step window/dialog is visible on screen")
        print("   - The button image in 3rdstep.png matches what's on screen")
        return

    print("\n✓ Step 3 completed successfully!")

    # Step 4: Click the 4th step button
    if not click_fourth_step_button():
        print("\n❌ [FAILED] Could not complete Step 4 - 4th step button not clicked")
        print("\n💡 Make sure:")
        print("   - The 4thstep.png file exists in the Buying folder")
        print("   - The 4th step window/dialog is visible on screen")
        print("   - The button image in 4thstep.png matches what's on screen")
        return

    print("\n✓ Step 4 completed successfully!")
    print("\n" + "="*50)
    print("✓ [SUCCESS] All 4 steps completed successfully!")
    print("="*50)


if __name__ == "__main__":
    # Add a small delay to give user time to position windows
    print("Starting in 3 seconds... Position your RuneLite window now!")
    time.sleep(3)
    main()
