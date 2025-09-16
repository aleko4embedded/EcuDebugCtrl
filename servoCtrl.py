#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  servoCtrl.py
#  
#  Copyright 2025  Aleko Embedded
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#  ENA PWM1 GPIO13
#  ENB PWM0 GPIO12
#  IN1 GPIO23
#  IN2 GPIO22
#  IN3 GPIO27
#  IN4 GPIO17

import RPi.GPIO as GPIO
import time
import curses

def set_angle(pwm, angle):
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)
    pwm.ChangeDutyCycle(0)

def init_servos(servo_pin,freq=50):
    #stdscr.nodelay(True)
    GPIO.setmode(GPIO.BCM)  # Or GPIO.BCM
    GPIO.setup(servo_pin, GPIO.OUT)  # Set pin 15 as an output
    pwm = GPIO.PWM(servo_pin,freq)
    pwm.start(0)
    print("pwm started")
    return pwm
    

def main(args):
    servo_pin = 18
    pwm=init_servos(servo_pin)
    set_angle(pwm,45)
    set_angle(pwm,0)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
