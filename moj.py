import pyautogui
import time
import keyboard
import sys



#Taxonomy on 01 July 2021
# Do not set U and P  as shortcuts.
# Comedy / Romance / Motivation / Attitude / Sadness / Anger / Kindness	Romance & Heartbreak	Romantic Songs	Couple (BF + GF) Romance
# Comedy / Romance / Motivation / Attitude / Sadness / Anger / Kindness	Romance & Heartbreak	Romantic Songs	Husband Wife Romance
# Comedy / Romance / Motivation / Attitude / Sadness / Anger / Kindness	Romance & Heartbreak	Romantic Songs	One Sided Love
# Comedy / Romance / Motivation / Attitude / Sadness / Anger / Kindness	Romance & Heartbreak	Romantic Songs	Break up & Betrayal 



def key(a,b,c,d,e,f):
	keyboard.press(a) #It will select No 
	time.sleep(0.1)
	keyboard.press(b) #L0
	time.sleep(0.1)
	keyboard.press(c) #L1
	time.sleep(0.1)
	keyboard.press(d) #L2
	time.sleep(0.1)
	keyboard.press(e) #L3
	time.sleep(0.1)
	keyboard.press(f) #L4
	time.sleep(0.1)
	




def check(a):
	if keyboard.is_pressed(a):
		if a == 'q':
			key('1','2','2','3','2','-') #Rom_song_gf_bf
			check(keyboard.read_key())
			

		if a == 'w':
			key('1','2','2','3','3','-') #rom_song_husband_wife
			check(keyboard.read_key())
			

		if a == 'e':
			key('1','2','2','3','4','-') #rom_song_one_side
			check(keyboard.read_key())
			

		if a == 'r':
			key('1','2','2','3','5','-') #rom_song_brkup
			check(keyboard.read_key())
			




		if a == 'k':
			key('1','8','1','1','5','3') #kids
			check(keyboard.read_key())
			

		if a == 'j':
			key('1','8','1','1','5','4') #baby
			check(keyboard.read_key())
			
		if a == 'm':
			key('1','8','1','1','1','-') #mother
			check(keyboard.read_key())
			


		if a == 'l':
			key('1','2','1','5','6','-') #Kids_humour
			check(keyboard.read_key())
			

		if a == 'f':
			key('1','2','1','5','8','-') #other_funny_act
			check(keyboard.read_key())
			


		if a == 't':
			key('1','4','4','1','6','-') #travel
			check(keyboard.read_key())
			

		if a == 'c':
			key('1','4','8','2','3','-') #cow_ox_buffalo
			check(keyboard.read_key())
			

		if a == 's':
			key('1','4','8','2','6','-') #other_street_animal
			check(keyboard.read_key())
			


		if a == 'd':
			key('1','5','2','1','-','-') #Devotion_name_choice
			check(keyboard.read_key())
			

		if a == 'o':
			key('1','5','2','1','0','-') #other_devotional
			check(keyboard.read_key())
			

		if a == 'h':
			key('1','5','2','2','0','-') #hindu_place of worship
			check(keyboard.read_key())
			

		if a == 'b':
			key('1','2','4','2','2','-') #boy_attitude_actr
			check(keyboard.read_key())
			

		if a == 'n':
			key('1','2','4','3','2','-') #attitude_actr
			check(keyboard.read_key())
			

		if a == 'y':
			key('1','2','2','2','-','-') #rom_act
			check(keyboard.read_key())
			

		if a == '+':
			key('1','2','2','4','-','-') #other_rom
			check(keyboard.read_key())
			


		if a == '*':

			time.sleep(15)
			check(keyboard.read_key())
			
			
			

	





while True:
	
	
	check(keyboard.read_key())
	
	





