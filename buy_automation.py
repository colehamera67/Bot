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
THIRD_STEP_WAIT = 4.0  # Longer wait for 3rd step (small button, harder to detect)
FOURTH_STEP_WAIT = 6.0  # Longer wait for 4th step (takes much longer to load)


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
    Note: Step 3 button has shading - needs VERY HIGH confidence for exact match.
    """
    print("\n=== Step 3: Clicking 3rd Step Button ===")

    if not os.path.exists(THIRD_STEP_BUTTON):
        print(f"ERROR: 3rdstep.png not found at: {THIRD_STEP_BUTTON}")
        print("Please add the 3rdstep.png image to the Buying folder.")
        return False

    # Give the interface MORE time to transition to the 3rd step
    print(f"Waiting {THIRD_STEP_WAIT} seconds for 3rd step to appear (longer wait)...")
    time.sleep(THIRD_STEP_WAIT)

    # Try to find and click the 3rd step button with VERY HIGH confidence for exact match
    print(f"Attempting to find 3rd step button with very high confidence (exact match only)...")

    # First try with very high confidence (0.95) - button has unique shading, need exact match
    print("Attempt 1: Trying with confidence 0.95 (very exact match, 20 retries)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button",
                     retries=20,
                     confidence=0.95,
                     wait_between=1.5):
        return True

    # Second attempt with high confidence
    print("\n⚠ First attempt failed. Trying with confidence 0.9 (15 retries)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button (Very High Confidence)",
                     retries=15,
                     confidence=0.9,
                     wait_between=2.0):
        return True

    # Third attempt with medium-high confidence
    print("\n⚠ Second attempt failed. Trying with confidence 0.85 (10 retries)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button (High Confidence)",
                     retries=10,
                     confidence=0.85,
                     wait_between=2.5):
        return True

    # Final attempt with standard high confidence
    print("\n⚠ Third attempt failed. Final try with confidence 0.8 (5 retries)...")
    if find_and_click(THIRD_STEP_BUTTON, "3rd Step Button (Standard High Confidence)",
                     retries=5,
                     confidence=0.8,
                     wait_between=3.0):
        return True

    print("\n❌ ERROR: Could not find 3rd step button on screen after all attempts!")
    print("Troubleshooting tips:")
    print("  1. Make sure the 3rd step dialog/window is visible and fully loaded")
    print("  2. The button with SHADING should be visible (that's the correct one)")
    print("  3. Make sure 3rdstep.png has the shading and matches EXACTLY")
    print("  4. Make sure the button is not obscured or off-screen")
    print("  5. Recapture 3rdstep.png with ONLY the shaded button (very precise)")
    print("  6. Try increasing THIRD_STEP_WAIT to 6 or 8 seconds if it loads slowly")
    return False


def click_fourth_step_button():
    """
    Clicks the 4th step button after the 3rd step has been clicked.
    Note: Step 4 has a longer wait time as it takes longer to load.
    """
    print("\n=== Step 4: Clicking 4th Step Button ===")

    if not os.path.exists(FOURTH_STEP_BUTTON):
        print(f"ERROR: 4thstep.png not found at: {FOURTH_STEP_BUTTON}")
        print("Please add the 4thstep.png image to the Buying folder.")
        return False

    # Give the interface MORE time to transition to the 4th step (it's slower)
    print(f"Waiting {FOURTH_STEP_WAIT} seconds for 4th step to appear (longer wait)...")
    time.sleep(FOURTH_STEP_WAIT)

    # Try to find and click the 4th step button with very aggressive settings
    print(f"Attempting to find 4th step button with very aggressive retry logic...")

    # First try with low confidence (0.6) - 4th button is smaller and harder to detect
    print("Attempt 1: Trying with confidence 0.6 (20 retries)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button",
                     retries=20,
                     confidence=0.6,
                     wait_between=1.5):
        return True

    # Second attempt with lower confidence
    print("\n⚠ First attempt failed. Trying with lower confidence (0.5, 15 retries)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button (Low Confidence)",
                     retries=15,
                     confidence=0.5,
                     wait_between=2.0):
        return True

    # Third attempt with very low confidence
    print("\n⚠ Second attempt failed. Trying with very low confidence (0.4, 10 retries)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button (Very Low Confidence)",
                     retries=10,
                     confidence=0.4,
                     wait_between=2.5):
        return True

    # Final desperate attempt with extremely low confidence
    print("\n⚠ Third attempt failed. Final try with extremely low confidence (0.3, 5 retries)...")
    if find_and_click(FOURTH_STEP_BUTTON, "4th Step Button (Extremely Low Confidence)",
                     retries=5,
                     confidence=0.3,
                     wait_between=3.0):
        return True

    print("\n❌ ERROR: Could not find 4th step button on screen after all attempts!")
    print("Troubleshooting tips:")
    print("  1. Make sure the 4th step dialog/window is visible and fully loaded")
    print("  2. Check that 4thstep.png matches the 'Set to Copilot price' button on screen")
    print("  3. Try taking a new screenshot of the button (make sure it's clear and exact)")
    print("  4. Make sure the button is not obscured or off-screen")
    print("  5. The button might have different colors/styling - try capturing it again")
    print("  6. Try increasing FOURTH_STEP_WAIT to 8 or 10 seconds if it loads very slowly")
    return False


def press_enter_key():
    """
    Presses the Enter key after step 4 is completed.
    """
    print("\n=== Step 5: Pressing Enter Key ===")

    # Small wait before pressing Enter
    print("Waiting 1 second before pressing Enter...")
    time.sleep(1.0)

    # Press Enter key
    print("Pressing Enter key...")
    pyautogui.press('enter')
    print("✓ Enter key pressed successfully!")

    return True


def main():
    """
    Main automation workflow.
    """
    print("="*50)
    print("RuneLite Buy Button Automation v3.5")
    print("="*50)
    print(f"Configuration:")
    print(f"  - Confidence: {CONFIDENCE}")
    print(f"  - Wait time (steps 1-2): {WAIT_TIME}s")
    print(f"  - Wait time (step 3): {THIRD_STEP_WAIT}s (longer)")
    print(f"  - Wait time (step 4): {FOURTH_STEP_WAIT}s (much longer)")
    print(f"  - Step 3: VERY HIGH confidence (0.95-0.8) for exact match with shading")
    print(f"  - Step 4: LOW confidence (0.6-0.3) for small button")
    print(f"  - Total steps: 5 (Buy → 2nd → 3rd → 4th → Enter)")
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

    # Step 5: Press Enter key
    if not press_enter_key():
        print("\n❌ [FAILED] Could not complete Step 5 - Enter key not pressed")
        return

    print("\n✓ Step 5 completed successfully!")
    print("\n" + "="*50)
    print("✓ [SUCCESS] All 5 steps completed successfully!")
    print("="*50)


if __name__ == "__main__":
    # Add a small delay to give user time to position windows
    print("Starting in 3 seconds... Position your RuneLite window now!")
    time.sleep(3)
    main()
