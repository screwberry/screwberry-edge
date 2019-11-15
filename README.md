# screwberry-edge

This part of the Screwberry project sets up a [Raspberry Pi](https://www.raspberrypi.org/) to act as a gateway between edge devices ([RuuviTags](https://ruuvi.com/manuals/tag/what-is-ruuvitag/)) and cloud (Azure IoT Hub).

## Use screwberry-edge

Follow these steps to start sending RuuviTag sensor data to the cloud from your Raspberry Pi.

### Prerequisites

* One or more RuuviTags
* Raspberry Pi with Linux (e.g. Raspbian) running on it and connected to the Internet

### Install

1. Clone this repo to your Raspberry Pi.
2. Rename `config.py.example` as `config.py`.
3. Copy-paste your connection string from IoT Hub to the CONNECTION variable in `config.py`.

### Configure (optional)

TBA: This section will be added later.

### Run

Run `python3 screwberry.py` to start sending sensor data to IoT Hub.

## Acknowledgements
* Raspberry Pi is a trademark of the Raspberry Pi Foundation.
