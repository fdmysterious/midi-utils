"""
##################################################
# Example to show how to construct midi messages #
##################################################

  Florian Dupeyron
  October 2019

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE" (Revision 42):
 <florian.dupeyron@mugcat.fr> wrote this file. As long as you retain this notice
 you can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return !
 ----------------------------------------------------------------------------
"""
import midi

print( midi.note_off(12, 64, 69) )
print( midi.note_on (12, 64, 69) )
print( midi.aftouch (12, 64, 22) )
print( midi.cc      (12, 43, 38) )
print( midi.pc      (12, 64 )    )
print( midi.aftouchc(12, 83 )    )
print( midi.pitchb  (12, 0.5)    )
print("--------------------------")
print( midi.from_bytes(bytes([0x90,29,38])) )
print( midi.from_bytes( midi.pitchb(15, 0).bytes() ) )
