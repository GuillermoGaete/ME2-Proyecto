import pyvisa as visa

import numpy as np

import matplotlib.pyplot as plt

import math

import traceback

import sys

import serial

import serial.tools.list_ports as list_ports

from tempfile import TemporaryFile


serialArduino = serial.Serial('/dev/ttyACM0', 9600)

readedLine=serialArduino.readline()

print(readedLine.decode().rstrip())
order="r"


serialArduino.write(b'r')

responseSerial=""

    

while(responseSerial!="finish"):
    readedLine=serialArduino.readline()
    responseSerial = readedLine.decode().rstrip()
    print(responseSerial)