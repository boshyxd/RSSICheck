## RSSICheck

### Overview

**RSSICheck** is a Python-based tool that leverages the `Bleak` library to scan and classify the signal strengths (RSSI) of nearby Bluetooth devices. This script provides a detailed analysis of each detected device's signal quality, helping users to understand the strength and reliability of their Bluetooth connections.

### Features

- **Real-time Bluetooth Scanning**: Continuously scans for Bluetooth devices within range.
- **RSSI Classification**: Classifies signal strength into categories: Excellent, Good, Fair, Weak, Very Weak, and Unusable.
- **Detailed Output**: Displays the device name, address, RSSI value, and signal quality in real-time.
- **Summary Report**: Provides a summary of all detected devices and their signal qualities after the scan.

### Requirements

- Python 3.7+
- Bleak library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/RSSICheck.git
    cd RSSICheck
    ```

2. Install the required dependencies:
    ```sh
    pip install bleak
    ```

### Usage

Run the script to start scanning for Bluetooth devices:
```sh
python RSSICheck.py
