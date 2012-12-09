import serial
import sys
import math

VCC = 5.0       # Supplied voltage in volts
R0 = 10000.0    # Nominal resistance of the thermistor in ohms
T0_C = 25.0     # Temperature for nominal resistance in Celsius (almost always 25)
BETA = 3950.0   # Beta coefficient of the thermistor
R_FIX = 9650.0  # Resistance of the fixed resistor of the voltage divider circuit in ohms

def get_adc():
    ser = serial.Serial('/dev/temperature-sensor')
    ser.write('c')
    (adc_symbol, adc_value) = ser.readline().strip().split()

    if adc_symbol != 'c':
        raise Exception('The received measurement symbol is not "c" !')

    return float(adc_value)

def get_smoothed_adc(number_of_samples=5):
    adc_sum = 0;
    for i in range(number_of_samples):
        adc = get_adc()
        print adc
        adc_sum += adc
    return adc_sum / number_of_samples

def get_temperature():
    adc = get_smoothed_adc()
    KELVIN_DIFF = 273.15
    T0_K = T0_C + KELVIN_DIFF
    voltage = adc*VCC/1023
    resistance = R_FIX*VCC/voltage - R_FIX
    temperature_k = 1 / (1/T0_K + 1/BETA * math.log(resistance/R0))
    temperature_c = temperature_k - KELVIN_DIFF
    return temperature_c
