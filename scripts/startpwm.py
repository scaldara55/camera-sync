#!/usr/bin/env python3
#####################################################################################
# Filename    : pwm.py
# Description : Logic_Analyzer_With_Software_PWM
# Author      : Steve Caldara
# Based on    : Script by Bob Fryer / Digital Shack
# Modification: 01 Mar 2023
#####################################################################################

#####################################################################################
# Import the required Python Libraries
#####################################################################################

import RPi.GPIO as GPIO
import time

#####################################################################################
# Define the Variables Needed and the GPIO initialisation
#####################################################################################


global pwmobj                         # declare the pmwobj as a global variable
RPI_Pin = 18                          # define the RPI GPIO Pin we will use with PWM (PWM)
RPI_DutyCycle = 10                    # define the Duty Cycle in percentage  (10%)
RPI_Freq = 30                         # define the frequency in Hz (30Hz)
RPI_PWMTime = 60                      # the time you want the PWM to stay active (secs)
GPIO.setmode(GPIO.BCM)                # set actual GPIO BCM Numbers
GPIO.setup(RPI_Pin, GPIO.OUT)         # set RPI_PIN as OUTPUT mode
GPIO.output(RPI_Pin, GPIO.LOW)        # set RPI_PIN LOW to at the start
pwmobj = GPIO.PWM(RPI_Pin, RPI_Freq)  # Initialise instance and set Frequency
pwmobj.start(0)                       # set initial Duty cycle to 0 & turn on PWM

#####################################################################################
# Define our main task
#####################################################################################

def activate():
    pwmobj.ChangeDutyCycle(RPI_DutyCycle)               # Set PWM Duty Cycle to 10%
    time.sleep(RPI_PWMTime)                             # Keep PWM on for 60 secs

#####################################################################################
# Define our DESTROY Function
#####################################################################################

def destroy():
    pwmobj.stop()                                               # stop PWM

#####################################################################################
# Finally the code for the MAIN program
# Eliminate the destroy()s to see if the HW PWM will run forever even after
# the program executes
#####################################################################################

if __name__ == '__main__':                                      # Program entry point
    print ('PWM Turned on with Duty Cycle of ', RPI_DutyCycle)  # Print duty cycle
    try:
        activate()                                              # Start the PWM
    except KeyboardInterrupt:                                   # Watches for Ctrl-C
#        destroy()                                               # call destroy funct
        pass
    
    finally:
#        destroy()                                               # call destroy funct
        pass
