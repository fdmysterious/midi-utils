"""
#########################################
# How to output MIDI using python-rtmidi#
#########################################

  Florian Dupeyron
  October 2019

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE" (Revision 42):
 <florian.dupeyron@mugcat.fr> wrote this file. As long as you retain this notice
 you can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return !
 ----------------------------------------------------------------------------
"""

import rtmidi
import time
import midi

bpm     = 90
T_pause = 0.1 # time in s of pause between each note

# First element of tuple is not number
# Second element is duration in beats
notes = [
    (64,1/2),
    (64,1/2),
    (64,1/2),
    (66,1/2),
    (68,1),
    (66,1),

    (64,1/2),
    (68,1/2),
    (66,1/2),
    (66,1/2),
    (64,2)
]

if __name__=="__main__":
    midi_out = rtmidi.MidiOut(name="Song Player")

    with midi_out.open_virtual_port(name="out"):
        T_beat = 60. / bpm # Time for one beat

        while True:
            for num,dur in notes:
                midi_out.send_message( list(midi.note_on(1,num,64).bytes()  ) )
                time.sleep(dur * T_beat - T_pause)
                midi_out.send_message( list(midi.note_off(1,num,64).bytes() ) )
                time.sleep(T_pause)
