USB Temperature Sensor
======================

This is a USB temperature sensor based on the [Atmega32u4 Breakout+](http://www.ladyada.net/products/atmega32u4breakout/) board of Adafruit Industries.  I used the [Adafruit thermistor guide](http://learn.adafruit.com/thermistor/using-a-thermistor) and the [LUFA library](http://www.fourwalledcubicle.com/LUFA.php) to make this project happen.

Schematic
---------

    ---------------+
                5v o------+
              AREF o------+
    A           F0 o      |
    T b         F1 o   10K ohm
    m r         F4 o  thermistor 
    e e         F5 o      |
    g a         F6 o      |
    a k  F7 (ADC7) o------+
    3 o         C7 o      |
    2 u         C6 o      |
    u t         B7 o     10K
    4           B6 o   resistor
                B5 o      |
                B4 o      |
               GND o------+
    ---------------+

Installation
------------

The following `make` directives are available:
* `build` (default): Fetch LUFA, copy the firmware source into its directory tree and build the firmware.
* `program`: Upload the firmware to the board.
* `clean`: Clean up the intermediate files that were created during the build process.

Place `90-temperature-sensor.rules` into `/etc/udev/rules.d` so that udev will create the `dev/temperature-sensor` symlink every time the sensor gets plugged in.

Usage
-----

After building and uploading the firmware use `host-utils/get-temperature.py` to retrieve the temperature value.

Photos
------

![Diagonal view](photos/diagonal-view.png)

![Side view](photos/side-view.png)

![Top view](photos/top-view.png)
