#!/bin/bash
# close the pins 9 an 11 on the raspberry pi and unexport
# run as sudo

echo 9 > /sys/class/gpio/unexport
echo 11 > /sys/class/gpio/unexport
echo 10 > /sys/class/gpio/unexport

