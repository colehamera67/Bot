# RuneLite Buy Button Automation

This script automates the complete 6-step buying process in RuneLite:
1. Click the buy button
2. Click the 2nd step button
3. Click the 3rd step button (TWICE - 2nd attempt skips if not found after 3 tries)
4. Click the 4th step button
5. Press Enter key
6. Click the confirm button

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. **IMPORTANT**: Ensure all step images are in the `Buying` folder:
   - `buy_button_active.png` - Active buy button
   - `buy_button_inactive.png` - Inactive buy button
   - `2ndstep.png` - 2nd step button
   - `3rdstep.png` - 3rd step button (clicked TWICE)
   - `4thstep.png` - 4th step button
   - `5thstep.png` - Confirm button

   Each image should clearly show the button you want to click at each step.

## Usage

1. Open RuneLite and navigate to the buy interface
2. Run the script:
```bash
python buy_automation.py
```
3. The script will give you 3 seconds to position the RuneLite window
4. It will then automatically:
   - Find and click the buy button
   - Wait for the 2nd step to appear and click it
   - Wait for the 3rd step to appear and click it TWICE (2nd click skips if not found after 3 tries)
   - Wait for the 4th step to appear and click it
   - Press Enter key
   - Wait for confirm button to appear and click it

## Files

- `buy_automation.py` - Main automation script
- `requirements.txt` - Python dependencies
- `Buying/buy_button_active.png` - Image of the active buy button
- `Buying/buy_button_inactive.png` - Image of the inactive buy button
- `Buying/2ndstep.png` - Image of the 2nd step button
- `Buying/3rdstep.png` - Image of the 3rd step button (clicked twice)
- `Buying/4thstep.png` - Image of the 4th step button
- `Buying/5thstep.png` - Image of the confirm button

## Troubleshooting

- **Button not found**: Make sure the RuneLite window is visible and not minimized
- **Wrong button clicked**: Adjust the `CONFIDENCE` value in the script (0.0 to 1.0)
- **Script too fast**: Increase the `WAIT_TIME` value in the script
- **Step 3 fails or clicks wrong button**: Step 3 button is clicked TWICE and has unique shading:
  - 1st click: Full retry logic with 50 attempts at VERY HIGH confidence (0.95 → 0.9 → 0.85 → 0.8)
  - 2nd click: Only 3 tries at 0.95 confidence, skips if not found (this is normal if button disappears)
  - Waits 4 seconds before 1st click, 2 seconds before 2nd click
  - Higher confidence = more exact match = only clicks button WITH shading
  - Confidence 0.95 requires almost pixel-perfect match
  - If clicking wrong button, recapture 3rdstep.png with ONLY the shaded button (very precise)
  - Make sure 3rdstep.png shows the button with the shading (not without it)
  - If 1st click fails, increase `THIRD_STEP_WAIT` to 6 or 8 seconds
- **Step 4 fails**: Step 4 has very aggressive special handling:
  - Waits 6 seconds (much longer than other steps)
  - Uses 50 total retries with confidence levels 0.6 → 0.5 → 0.4 → 0.3
  - Wait times between retries: 1.5s → 2.0s → 2.5s → 3.0s
  - If still failing, increase `FOURTH_STEP_WAIT` to 8 or 10 seconds
  - Make sure the "Set to Copilot price" button is clearly visible and not obscured
  - The button image might need to be recaptured if colors/styling differ

## Configuration

You can adjust these settings in `buy_automation.py`:
- `CONFIDENCE`: Image matching confidence (default: 0.7)
- `WAIT_TIME`: Seconds to wait between actions for steps 1-2 (default: 2.5)
- `THIRD_STEP_WAIT`: Seconds to wait before step 3 (default: 4.0, longer because button is very small)
- `FOURTH_STEP_WAIT`: Seconds to wait before step 4 (default: 6.0, much longer because step 4 loads very slowly)
