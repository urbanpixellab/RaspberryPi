#!/bin/bash
# open the pins 9 an 11 on the raspberry pi and export them as input
# run as sudo!!

echo 9 > /sys/class/gpio/export
#set the direction of the gpio in or out
echo in > /sys/class/gpio/gpio9/direction
cat /sys/class/gpio/gpio9/value

echo 11 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio11/direction
cat /sys/class/gpio/gpio11/value

##the led
echo 10 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio10/direction
cat /sys/class/gpio/gpio10/value

#dont forget to unexport the gpios after use!
# to set the value use 
# sudo echo 1 >/sys/class/gpio/gpio23/value
