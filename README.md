# RuneLite Buy Button Automation

This script automates clicking the buy button and then the 2nd step button in RuneLite.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. **IMPORTANT**: Add the `2ndstep.png` image to the `Buying` folder:
   - Take a screenshot of the 2nd step button
   - Save it as `2ndstep.png` in the `Buying` folder
   - The image should clearly show the button you want to click

## Usage

1. Open RuneLite and navigate to the buy interface
2. Run the script:
```bash
python buy_automation.py
```
3. The script will give you 3 seconds to position the RuneLite window
4. It will then:
   - Find and click the buy button
   - Wait for the 2nd step to appear
   - Find and click the 2nd step button

## Files

- `buy_automation.py` - Main automation script
- `Buying/buy_button_active.png` - Image of the active buy button
- `Buying/buy_button_inactive.png` - Image of the inactive buy button
- `Buying/2ndstep.png` - Image of the 2nd step button (YOU NEED TO ADD THIS)

## Troubleshooting

- **Button not found**: Make sure the RuneLite window is visible and not minimized
- **Wrong button clicked**: Adjust the `CONFIDENCE` value in the script (0.0 to 1.0)
- **Script too fast**: Increase the `WAIT_TIME` value in the script

## Configuration

You can adjust these settings in `buy_automation.py`:
- `CONFIDENCE`: Image matching confidence (default: 0.8)
- `WAIT_TIME`: Seconds to wait between actions (default: 1.0)
