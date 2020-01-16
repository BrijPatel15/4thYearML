import string
import random
import time

possible_keys={-4,-3,-2,-1,0,1,2,3,4,5,6,7}
note_log=[]
chosen_key=random.sample(possible_keys,1)[0]

key_probs={7:1/12,6:1/12,5:1/12,4:1/12,3:1/12,2:1/12,1:1/12,0:1/12,-1:1/12,-2:1/12,-3:1/12,-4:1/12}

note_count=[0,0,0,0,0,0,0,0,0,0,0,0]

key_profiles={}
key_profiles[7]={0,1,3,5,6,8,10} #same as -5
key_profiles[6]={1,3,5,6,8,10,11} #same as -6
key_profiles[5]={1,3,4,6,8,10,11} #same as -7
key_profiles[4]={1,3,4,6,8,9,11}
key_profiles[3]={1,2,4,6,8,9,11}
key_profiles[2]={1,2,4,6,7,9,11}
key_profiles[1]={0,2,4,6,7,9,11}
key_profiles[0]={0,2,4,5,7,9,11}
key_profiles[-1]={0,2,4,5,7,9,10}
key_profiles[-2]={0,2,3,5,7,9,10}
key_profiles[-3]={0,2,3,5,7,8,10}
key_profiles[-4]={0,1,3,5,7,8,10}

chord_profiles={}
chord_profiles['maj']={0,4,7}
chord_profiles['min']={0,3,7}
chord_profiles['aug']={0,4,8}
chord_profiles['dim']={0,3,6}
chord_profiles['sus4']={0,5,7}
chord_profiles['maj7']={0,4,7,11}
chord_profiles['min7']={0,3,7,10}
chord_profiles['7']={0,4,7,10}

key_name={}
key_name[7]='C# / A#m'
key_name[6]='F# / D#m'
key_name[5]='B / G#m'
key_name[4]='E / C#m'
key_name[3]='A / F#m'
key_name[2]='D / Bm'
key_name[1]='G / Em'
key_name[0]='C / Am'
key_name[-1]='F / Dm'
key_name[-2]='Bb / Gm'
key_name[-3]='Eb / Cm'
key_name[-4]='Ab / Fm'

note_name={}
note_name[0]='C'
note_name[1]='C# / Db'
note_name[2]='D'
note_name[3]='D# / Eb'
note_name[4]='E'
note_name[5]='F'
note_name[6]='F# / Gb'
note_name[7]='G'
note_name[8]='G# / Ab'
note_name[9]='A'
note_name[10]='A# / Bb'
note_name[11]='B'

def chord_name(chord):

	possible_chords=set()

	reduced_chord=set()
	for note in chord:
		reduced_chord.add(reduce(note))

	for root in reduced_chord:
		for key in chord_profiles:
			flag=True
			shifted_chord=set()
			for note in chord_profiles[key]:
				shifted_chord.add(reduce(note+root))
			if reduced_chord==shifted_chord:
				possible_chords.add(note_name[root]+key)

	return str(possible_chords)

def find_key_bayesian(note):
	global chosen_key
	global key_probs
	global note_count

	note_count[reduce(note)]+=1

	for key in key_probs:

		if reduce(note) in key_profiles[key]:
			note_prob_given_key=0.9
		else:
			note_prob_given_key=0.1

		key_probs[key]*=note_prob_given_key*sum(note_count)/note_count[note]

	best_key=0

	for key in key_probs:
		if key_probs[key]>key_probs[best_key]:
			best_key=key

	chosen_key=best_key




def find_key(note):
	'''(int) -> None
 	Updates the current key with respect to the latest note.'''
	global chosen_key
	note_set={note}
	marked=set()
	note_log.append(note)
	for key in possible_keys:
		if note_set.isdisjoint(key_profiles[key]):
			marked.add(key)
	for key in marked:
		possible_keys.discard(key)
	while len(possible_keys)==0:
		note_log.pop(0)
		note_set=set(note_log)
		for key in key_profiles:
			if note_set.issubset(key_profiles[key]):
				possible_keys.add(key)
	if not chosen_key in possible_keys:
		chosen_key=random.sample(possible_keys,1)[0]

def in_key(root,profile):
	'''(int,set) -> boolean
 	Checks if a chord is in the current key.'''
	for note in profile:
		if reduce(root+note) not in key_profiles[chosen_key]:
			return False
	return True

def reduce(pitch): 
	'''(int) -> int
 	Lowers a note value to the first octave.'''
	temp=pitch
	while temp>=12:
		temp-=12
	return temp

def fill_chord(notes,chord): 

	'''(set,set) -> set
 	Returns a harmonizing set of notes given the current notes and previous chord.'''

	 #returns the old chord if the notes still fit
	if reduced_set(notes).issubset(reduced_set(chord)):
		return chord.difference(notes)

	#finds a new chord when the notes don't fit the old chord
	else:
		good_chords=[]
		for root in key_profiles[chosen_key]: #iterates through all in-key roots
			for chord_key in chord_profiles: #iterates through all chord types

				#appends the chord to a list of acceptable chords if it matches the notes and is in-key
				if in_key(root,chord_profiles[chord_key]) and in_profile(root,chord_profiles[chord_key],notes):
					raised_set=set()
					for note in chord_profiles[chord_key]:
						raised_set.add(reduce(note+root))
					good_chords.append(raised_set)

		#chooses and returns an acceptable chord
		if len(good_chords)>0:
			return good_chords[random.randint(0,len(good_chords)-1)]
		return set()

def in_profile(root,profile,notes):
	'''(int,set,set) -> bool
 	Checks if a chord includes a set of notes.'''
	shifted_set=set()
	for note in profile:
		shifted_set.add(note+root)
	return reduced_set(notes).issubset(reduced_set(shifted_set))

def reduced_set(notes):
	'''(set) -> set
 	Returns a note set with all notes lowered to the first octave.'''
	new_set=set()
	for note in notes:
		new_set.add(reduce(note))
	return new_set


