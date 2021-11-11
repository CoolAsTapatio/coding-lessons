# Untitled.py
# Created by Kids on 2/6/21.

class Ukulele:
	def __init__(self, soundboard_wood, body_wood, neck_wood, fretboard_wood, size, inlays):
		self.physical_properties = Woods(soundboard_wood, body_wood, neck_wood, fretboard_wood)
		self.size = size
		self.inlay = inlays
		self.price = 0
class Woods:
	def __init__(self, soundboard, body, neck, fretboard):
		self.soundboard = soundboard
		self.body = body
		self.neck = neck
		self.fretboard = fretboard
		