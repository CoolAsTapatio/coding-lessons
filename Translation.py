# Untitled.py
# Created by Kids on 4/7/22.
import translators as tranlate

if __name__ == "__main__":
	starting_eng = "You belong among the wildflowers, you belong in a boat out at sea. Sail away, kill off the hours, You belong somewhere you feel free. Run away, find you a lover, Go away somewhere all bright and new. I have seen no other Who compares with you. You belong among the wildflowers, You belong in a boat out at sea .You belong with your love on your arm, You belong somewhere you feel free"
	print(starting_eng + "\n")
	espanol = tranlate.google(starting_eng, 'en', 'es')
	arabic = tranlate.google(espanol, 'es', 'ar')
	hindi = tranlate.google(arabic, 'ar', 'hi')
	print(arabic)
	eng = tranlate.google(hindi, 'hi', 'en')
	print(eng)