# RuneLite Auto Buy Button Clicker

Automatically finds and clicks the active buy button in RuneLite, regardless of its position on screen.

## Features

- **Image Recognition**: Uses computer vision to locate the active buy button
- **Position Independent**: Works even when the button changes position
- **Two Modes**:
  - Single Click: Find and click once
  - Continuous Mode: Keep searching and clicking at regular intervals
- **Safety Features**:
  - FAILSAFE: Move mouse to top-left corner to abort
  - Customizable click intervals and limits

## Installation

1. Install Python 3.7 or higher
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the script:

```bash
python runelite_auto_buy.py
```

### Interactive Menu:

The script will present you with options:
1. **Single click**: Searches once and clicks if found
2. **Continuous mode**: Keeps searching and clicking (you can set interval and max clicks)
3. **Exit**: Quit the program

### Safety:

- Move your mouse to the **top-left corner** of the screen to trigger FAILSAFE and abort
- Press **Ctrl+C** to stop continuous mode

## How It Works

1. The script uses the images in `Buying/` folder:
   - `buy_button_active.png` - The button to click
   - `buy_button_inactive.png` - For reference (not currently used)

2. PyAutoGUI scans your screen to find the active button image
3. When found, it clicks the center of the button
4. In continuous mode, it repeats at your specified interval

## Requirements

- Windows/Linux/Mac with Python 3.7+
- RuneLite must be visible on screen
- The buy button must match the image in `Buying/buy_button_active.png`

## Troubleshooting

**Button not found?**
- Make sure RuneLite is open and visible
- Check that the button looks exactly like `buy_button_active.png`
- The script uses 80% confidence matching by default

**Script too slow/fast?**
- Adjust the interval in continuous mode
- Modify `pyautogui.PAUSE` in the script for faster/slower actions

## Notes

- This script is for educational/automation purposes
- Use responsibly and in accordance with game rules
- The script only clicks when it finds the active button image
