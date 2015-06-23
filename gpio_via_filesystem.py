#!/usr/bin/env python3
# pin9 toggle button
# pin10 led
# pin11 push button
import time

class gpio(object):

	def __init__(self, pin, direction, value):
		self.pin = pin
		self.direction = direction
		self.value = value
		self.open_gpio()


	def export_pin(self):
		export_file = open("/sys/class/gpio/export", "w")
		export_file.write(str(self.pin))
		export_file.close()

	def unexport_pin(self):
		unexport_file = open("/sys/class/gpio/unexport", "w")
		unexport_file.write(str(self.pin))
		unexport_file.close()

	def set_pin_irection(self):
		direction_file = open("/sys/class/gpio/gpio" + str(self.pin) + "/direction", "w")
		direction_file.write(self.direction) #in or out
		direction_file.close()

	def get_pin_direction(self):
		direction_file = open("/sys/class/gpio/gpio" + str(self.pin) + "/direction", "r")
		self.direction = direction_file.read(1)
		direction_file.close()
		return self.direction

	def set_pin_value(self,v):
		self.value = v
		value_file = open("/sys/class/gpio/gpio" + str(self.pin) + "/value", "w")
		value_file.write(str(self.value))
		value_file.close()

	def get_pin_value(self):
		value_file = open("/sys/class/gpio/gpio" + str(self.pin) + "/value", "r")
		self.value = value_file.read(1)
		value_file.close()
		return self.value

	def get_pin(self):
		return self.pin

	def open_gpio(self):
		self.export_pin()
		self.pin_direction()

	def close_gpio(self):
		self.unexport_pin()



pins = {9 : "in", 11 :"in", 10 :"out"}

gpioList = []
ledIndex = 1

for key, val in pins.items():
	gpioList.append(gpio(key,val,0))		

for x in range(1,10):
	gpioList[ledIndex].set_pin_value(1)
	time.sleep(2)
	gpioList[ledIndex].set_pin_value(0)
	time.sleep(2)

for i in gpioList:
	i.close_gpio()



