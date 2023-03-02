# camera-sync
 Synchronize two cameras over WiFi network

The goal of this project is to have two global shutter cameras each individually connected to a separate Raspberry Pi.  These two Pi/Camera modules are connected to a third Raspberry Pi (Master) acting as a WiFi access point which is connected to the internet. The two Pi/Camera modules synchronize their timing to the Master over WiFi.  The Master is the only one connected to the internet and is clock synchronized to a network clock.

The two Pi/Camera modules use PWM to generate clock module triggers at a nominal 30 fps.

Validate that the two separate clock module triggers do not drift with respect to one another.
Validate that the clock module triggers are resilient to interruptions and network outages.

Make use of the pigpio library

	The pigpio library

	sudo apt install pigpio   # Install pigpio library
	sudo pigpiod              # Start the pigpio daemon
	cd pigpio
	./gpiotest.sh             # Run the gpio test

