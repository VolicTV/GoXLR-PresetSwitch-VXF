# GoXLR Preset Switcher

A Python script for automating preset changes on the GoXLR audio interface.

## Features

- Connects to GoXLR device
- Sets specific audio effect presets
- Easy to customize for different presets
- Includes a mock mode for testing without hardware

## Requirements

- Python 3.7+
- GoXLR Python module (installation instructions TBD)
- GoXLR hardware device (for non-mock mode)

## Installation

1. Clone this repository
2. Install required packages:
   `
   pip install -r requirements.txt
   `

## Usage

1. Ensure GoXLR software is running (for non-mock mode)
2. Connect GoXLR device (for non-mock mode)
3. Set USE_MOCK = False in config.py to use real hardware
4. Run python Chipmunk On.py

## Customization

Modify setPresetSqueaks function in Chipmunk On.py to adjust preset parameters.

## Troubleshooting

If you encounter connection issues:
- Ensure GoXLR App is running
- Check USB connection
- Verify firewall settings
- Try running as Administrator
- Update GoXLR firmware
- Reinstall GoXLR Python module

## Contributing

Contributions are welcome! Please test with actual GoXLR hardware before submitting PRs.

## Disclaimer

This is a work in progress. Some features may require adjustment based on the actual GoXLR Python API.
