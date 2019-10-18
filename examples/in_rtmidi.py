"""
####################################
# Simple midi monitor using rtmidi #
####################################

  Florian Dupeyron
  October 2019

  See https://github.com/SpotlightKid/python-rtmidi/blob/master/examples/basic/midiin_callback.py

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE" (Revision 42):
 <florian.dupeyron@mugcat.fr> wrote this file. As long as you retain this notice
 you can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return !
 ----------------------------------------------------------------------------
"""

import rtmidi
import midi
import time

in_port = rtmidi.MidiIn()

def callback(ev, data=None):
    msg,deltaT=ev

    print("%s -- " % (
        " ".join( "0x{:02X}".format(x) for x in msg )
    ), end="")

    try:
        parsed = midi.from_bytes(bytes(msg))
        print( parsed )

    except: print( "Uknown message" )

with in_port.open_virtual_port("MIDI monitor"):
    in_port.set_callback( callback   )
    in_port.ignore_types( sysex=True,timing=True,active_sense=True )

    try:
        print("Hello world !")
        while True : time.sleep(1)
    except KeyboardInterrupt:pass
