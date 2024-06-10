import asyncio
from bleak import BleakScanner

def classify_rssi(rssi):
    if rssi >= -50:
        return "Excellent"
    elif rssi >= -60:
        return "Good"
    elif rssi >= -70:
        return "Fair"
    elif rssi >= -80:
        return "Weak"
    elif rssi >= -90:
        return "Very Weak"
    else:
        return "Unusable"

async def scan():
    devices_found = {}

    def detection_callback(device, advertisement_data):
        if device.address not in devices_found:
            rssi = advertisement_data.rssi
            signal_quality = classify_rssi(rssi)
            devices_found[device.address] = (rssi, signal_quality)
            print(f"Device: {device.name or 'Unknown'}, Address: {device.address}, RSSI: {rssi} dBm, Signal Quality: {signal_quality}")

    scanner = BleakScanner(detection_callback=detection_callback)
    
    print("Scanning for Bluetooth devices...")
    await scanner.start()
    await asyncio.sleep(10.0)
    await scanner.stop()

    print("\nSummary of detected devices:")
    for address, (rssi, signal_quality) in devices_found.items():
        print(f"Address: {address}, RSSI: {rssi} dBm, Signal Quality: {signal_quality}")

if __name__ == "__main__":
    asyncio.run(scan())
