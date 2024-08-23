<div align="center">

# RSSICheck 📡

<img src="https://i.ibb.co/SBbPmj3/rssicheck.png" alt="RSSICheck Logo" width="200"/>

RSSICheck is a Python-based tool that leverages the `Bleak` library to scan and classify the signal strengths (RSSI) of nearby Bluetooth devices. This script provides a detailed analysis of each detected device's signal quality, helping users to understand the strength and reliability of their Bluetooth connections.

[Features](#-features) •
[Requirements](#-requirements) •
[Installation](#-installation) •
[Usage](#-usage) •
[Example Output](#-example-output) •
[License](#-license)

</div>

## 🌟 Features

- Real-time Bluetooth Scanning: Continuously scans for Bluetooth devices within range.
- RSSI Classification: Classifies signal strength into categories: Excellent, Good, Fair, Weak, Very Weak, and Unusable.
- Detailed Output: Displays the device name, address, RSSI value, and signal quality in real-time.
- Summary Report: Provides a summary of all detected devices and their signal qualities after the scan.

## 🛠️ Requirements

- Python 3.7+
- Bleak library

## 📥 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/boshyxd/RSSICheck.git
   cd RSSICheck
   ```
2. Install the required dependencies:
   ```sh
   pip install bleak
   ```

## 🚀 Usage

Run the script to start scanning for Bluetooth devices:

```sh
python RSSICheck.py
```

The script will scan for 10 seconds and output the RSSI and signal quality of each detected device.

## 📊 Example Output

```bash
Scanning for Bluetooth devices...
Device: Unknown, Address: 00:1A:7D:DA:71:13, RSSI: -55 dBm, Signal Quality: Good
Device: Bluetooth Speaker, Address: 24:62:AB:F2:4D:7E, RSSI: -67 dBm, Signal Quality: Fair
Summary of detected devices:
Address: 00:1A:7D:DA:71:13, RSSI: -55 dBm, Signal Quality: Good
Address: 24:62:AB:F2:4D:7E, RSSI: -67 dBm, Signal Quality: Fair
```

## 📄 License

This project is licensed under the MIT License.

<div align="center">

---

Made with ❤️ by [boshyxd](https://github.com/boshyxd)

</div>
