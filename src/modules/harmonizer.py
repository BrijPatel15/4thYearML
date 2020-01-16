from mido import MidiFile, Message, MidiTrack, second2tick
import chord
import random
import time

LONGEST_RUN=0

def harmonize(filename):

# filename=input('Enter the midi file to be harmonized: ')
	mid=MidiFile(filename)

	new_track=MidiTrack()
	mid.tracks.append(new_track)

	note_set=set()
	timestamp=0
	current_chord={}
	waiting_for_note_on=False
	for msg in mid:
		#print(msg)

		if msg.type=='note_on':
			chord.find_key(chord.reduce(msg.note))
			#print('KEYS -> ',chord.possible_keys,' CHOSEN_KEY -> ',chord.chosen_key)

		if not waiting_for_note_on:
			if msg.type=='set_tempo': #finds tempo message and records tempo
				tempo=msg.tempo
				continue

			if msg.time==0: #the message occurs in the old timestamp
				if msg.type=='note_on': #adds the note to the set
					note_set.add(msg.note)
			else: #the message is the first in a new timestamp

				#print('played ',note_set,' with timestamp ',timestamp)

				TIME_0=time.time()

				current_chord=chord.fill_chord(note_set,current_chord)

				TIME_1=time.time()-TIME_0

				if TIME_1>LONGEST_RUN:
					LONGEST_RUN=TIME_1
				
				if len(current_chord)>0:
					new_track.append(Message('note_on',note=random.sample(current_chord,1)[0],velocity=100,time=int(second2tick(timestamp,mid.ticks_per_beat,tempo))))
					#for note in current_chord:
						#if note!=min(current_chord):
							#new_track.append(Message('note_on',note=note,velocity=100,time=0))

				if len(current_chord)==0:
					timestamp+=msg.time
				else:
					timestamp=msg.time

				current_chord=current_chord.union(note_set) #adds note_set to current_chord

				if msg.type=='note_on':
					note_set={msg.note}
				if msg.type=='note_off':
					note_set.clear()
					waiting_for_note_on=True


		else:
			if msg.type=='note_on':
				note_set.add(msg.note)
				timestamp+=msg.time
				waiting_for_note_on=False
			if msg.type=='note_off':
				timestamp+=msg.time

	mid.save('output.mid')
	#print('Successfully harmonized ',filename,' and saved to output.mid')
	print('Longest execution of chord.fill_chord() took ',LONGEST_RUN*1000,' milliseconds.')


