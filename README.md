# Testing the use of Pyportal + GitHub actions

![MIT License](https://img.shields.io/static/v1.svg?label=📜%20License&message=MIT&color=informational) 

:construction: Please note that everything contained in this repo is experimental at the moment :construction:

## Table of contents
- [Testing the use of Pyportal + GitHub actions](#testing-the-use-of-pyportal--github-actions)
  - [Table of contents](#table-of-contents)
  - [:robot: :snake: About PyPortal and CircuitPython](#--about-pyportal-and-circuitpython)
  - [:package: Dependencies and Libraries](#-dependencies-and-libraries)
    - [Configuring Wifi and Adafruit IO](#configuring-wifi-and-adafruit-io)
      - [Wifi](#wifi)
      - [Adafruit IO](#adafruit-io)
    - [Libraries](#libraries)

## :robot: :snake: About PyPortal and CircuitPython

This code is meant to run on a PyPortal.

An [Adafruit PyPortal](https://www.adafruit.com/product/4116) is an wifi-enabled microcontroller device featuring a 3" capacitive touchscreen and CircuitPython baked in.

It can be programmed with [CircuitPython](https://circuitpython.org/), a variant of Python that can be used to program microcontrollers, originally forked from [MicroPython](https://github.com/micropython/micropython).

## :package: Setup and dependencies

Please note that in addition to the Pyportal you will also need a data + power USB cable. Make sure this is the case as not all the USB cables allow for data transfer.

### Configuring Wifi and Adafruit IO

The PyPortal needs to connect to wifi to fetch the time from the internet using Adafruit IO.

First, rename `secrets.py.sample` to `secrets.py`.

#### Wifi

Update `secrets.py` with the SSID and password for your own wifi network.

Set `ssid` and `password` for your network in the `secrets` dictionary in `secrets.py`.

#### Adafruit IO

If you don't have one already, create a new account on [Adafruit IO](https://io.adafruit.com/).

Set your `aio_username` and `aio_key` in the `secrets` dictionary in `secrets.py`.

**:lock: Tip: make sure not to commit your `secrets.py` file to source control. To avoid this from happening you can add it to your .gitignore file.**

### Libraries

The following libraries, compatible with CircuitPython 4.0.1 are required to be present in the `lib` directory. [Download the library bundle](https://circuitpython.org/libraries).

 - `adafruit_bus_device`
 - `adafruit_bitmap_font`
 - `adafruit_display_text`
 - `neopixel`
 - `adafruit_pyportal`
 - `adafruit_touchscreen`
 - `adafruit_esp32spi`
 - `adafruit_sdcard`
 - `adafruit_io`