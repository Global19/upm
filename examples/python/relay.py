#!/usr/bin/env python
from __future__ import print_function
# Author: Sarah Knepper <sarah.knepper@intel.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
from upm import pyupm_relay as upmrelay

def main():
    # Create the relay switch object using GPIO pin 0
    relay = upmrelay.Relay(0)

    # Close and then open the relay switch 3 times,
    # waiting one second each time.  The LED on the relay switch
    # will light up when the switch is on (closed).
    # The switch will also make a noise between transitions.
    for i in range (0,3):
        relay.on()
        if relay.isOn():
            print(relay.name(), 'is on')
        time.sleep(1)
        relay.off()
        if relay.isOff():
            print(relay.name(), 'is off')
        time.sleep(1)

    # Delete the relay switch object
    del relay

if __name__ == '__main__':
    main()
