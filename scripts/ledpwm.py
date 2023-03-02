#!/usr/bin/env python3
#####################################################################################
# Filename    : LogicAnalyzer_SoftwarePWM.py
# Description : Logic_Analyzer_With_Software_PWM
# Author      : Bob Fryer / Digital Shack
# modification: 22 Feb 2020
#####################################################################################

#####################################################################################
# Import the required Python Libraries
#####################################################################################

import RPi.GPIO as GPIO
import time

#####################################################################################
# Define the Variables Needed and the GPIO initialisation
#####################################################################################


global pwmobj                    # declare the pmwobj as a global variable
RPI_Pin = 18                     # define the RPI GPIO Pin we will use with PWM (PWM)
RPI_DutyCycle = 50               # define the Duty Cycle in percentage  (50%)
RPI_Freq = 500                   # define the frequency in Hz (500Hz)
RPI_LEDTime = 60                 # the time you want the LED to stay lit for (secs)
GPIO.setmode(GPIO.BCM)              # set actual GPIO BCM Numbers
GPIO.setup(RPI_Pin, GPIO.OUT)         # set RPI_PIN as OUTPUT mode
GPIO.output(RPI_Pin, GPIO.LOW)        # set RPI_PIN LOW to at the start
pwmobj = GPIO.PWM(RPI_Pin, RPI_Freq)  # Initialise instance and set Frequency
pwmobj.start(0)                       # set initial Duty cycle to 0 & turn on PWM

#####################################################################################
# Define our main task
#####################################################################################

def light():
    pwmobj.ChangeDutyCycle(RPI_DutyCycle)               # Set PWM Duty Cycle to 50%
    time.sleep(RPI_LEDTime)                             # Keep Led lit for 60 secs

#####################################################################################
# Define our DESTROY Function
#####################################################################################

def destroy():
    pwmobj.stop()                                               # stop PWM

#####################################################################################
# Finally the code for the MAIN program
#####################################################################################

if __name__ == '__main__':                                      # Program entry point
    print ('LED Turned on with Duty Cycle of ', RPI_DutyCycle)  # Print duty cycle
    try:
        light()                                                 # call light function
    except KeyboardInterrupt:                                   # Watches for Ctrl-C
        destroy()                                               # call destroy funct
    finally:
        destroy()                                               # call destroy funct