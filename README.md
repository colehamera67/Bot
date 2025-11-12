# RuneLite Buy Button Automation

This script automates the complete 4-step buying process in RuneLite:
1. Click the buy button
2. Click the 2nd step button
3. Click the 3rd step button
4. Click the 4th step button

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. **IMPORTANT**: Ensure all step images are in the `Buying` folder:
   - `buy_button_active.png` - Active buy button
   - `buy_button_inactive.png` - Inactive buy button
   - `2ndstep.png` - 2nd step button
   - `3rdstep.png` - 3rd step button
   - `4thstep.png` - 4th step button

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
   - Wait for the 3rd step to appear and click it
   - Wait for the 4th step to appear and click it

## Files

- `buy_automation.py` - Main automation script
- `requirements.txt` - Python dependencies
- `Buying/buy_button_active.png` - Image of the active buy button
- `Buying/buy_button_inactive.png` - Image of the inactive buy button
- `Buying/2ndstep.png` - Image of the 2nd step button
- `Buying/3rdstep.png` - Image of the 3rd step button
- `Buying/4thstep.png` - Image of the 4th step button

## Troubleshooting

- **Button not found**: Make sure the RuneLite window is visible and not minimized
- **Wrong button clicked**: Adjust the `CONFIDENCE` value in the script (0.0 to 1.0)
- **Script too fast**: Increase the `WAIT_TIME` value in the script

## Configuration

You can adjust these settings in `buy_automation.py`:
- `CONFIDENCE`: Image matching confidence (default: 0.8)
- `WAIT_TIME`: Seconds to wait between actions (default: 1.0)
