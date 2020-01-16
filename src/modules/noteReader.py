import string
import binascii
import chord

def findDeltaTime(first_byte,second_byte):
	if first_byte>=128:
		first_byte-=128
	if second_byte>=128:
		second_byte-=128
	return first_byte<<7|second_byte

def nextByte():
	raw_byte=mid.read(1)
	if raw_byte==b'':
		return ''
	return int(str(binascii.hexlify(raw_byte),'ascii'),16)

def nameNote(pitch):
	while pitch-12>=0:
		pitch-=12
	return noteNames[pitch]
	
notePackage=[]
noteDict={}

while True:
	filename=input('Enter the name of the MIDI file to be read: ')
	if filename=='quit':
		break
	byte='not null'
	noteNames=['C    ','C#/Db','D    ','D#/Eb','E    ','F    ','F#/Gb','G    ','G#/Ab','A    ','A#/Bb','B    ']
	lookingForDeltaTime=False
	mid=open(filename,'rb')
	mid.seek(14,1)
	current_byte=14+16
	track='TRACK_ERROR'
	action='ACTION_ERROR'
	passed_first_note=False
	#print('Found MIDI header and skipped 14 bytes')

	while byte!='':
		current_byte+=1
		byte=nextByte()

		if byte=='':
			break

		#print('byte is',byte,'and lfdt =',lookingForDeltaTime)

		if byte==77:
			if str(binascii.hexlify(mid.read(3)),'ascii')=='54726b': #track header
				print('Found track header at line',current_byte/16)
				mid.seek(4,1)
				current_byte+=7
				timestamp=0
			else:
				pitch=byte
				mid.seek(1,1)
				current_byte+=1
				print('Track',track,'|',action,'| Note =',nameNote(pitch),'| Pitch =',pitch,'| Time =',timestamp)
			lookingForDeltaTime=True

		else:
			if lookingForDeltaTime:
				if byte!=0:
					if byte>=128:
						second_byte=nextByte()
						deltaTime=findDeltaTime(byte,second_byte)
					else:
						deltaTime=findDeltaTime(0,byte)
					timestamp+=deltaTime
				lookingForDeltaTime=False
			else:
				if byte==255:
					mid.seek(1,1)
					bytes_to_skip=nextByte()
					#print('Found meta-command and skipped',bytes_to_skip,'bytes')
					mid.seek(bytes_to_skip,1)
					current_byte+=bytes_to_skip+2

				else:
					if byte>=160:
						if byte>=224: #Ex
							mid.seek(2,1)
							current_byte+=2
						else:
							if byte>=192: #Cx or Dx
								mid.seek(1,1)
								current_byte+=1
							else: #Ax or Bx
								mid.seek(2,1)
								current_byte+=2
					else:
						if byte>=128:
							if byte>=144:
								track=byte-144
								action='NOTE_ON  '
								if not passed_first_note:
									passed_first_note=True
							else:
								track=byte-128
								action='NOTE_OFF '
							pitch=nextByte()
							current_byte+=1
						else:
							if passed_first_note:
								pitch=byte
							else:
								continue
								print('tried to escape')
						mid.seek(1,1)
						current_byte+=1

						print('Track',track,'|',action,'| Note =',nameNote(pitch),'| Pitch =',pitch,'| Time =',timestamp)

						if noteDict.get(timestamp)==None:
								noteDict[timestamp]=[[],[]]
						if action=='NOTE_ON  ':
								noteDict[timestamp][0].append(pitch)
						if action=='NOTE_OFF ':
								noteDict[timestamp][1].append(pitch)

				lookingForDeltaTime=True


	mid.close()

	note_set=set()
	for key in noteDict:
		for note in noteDict[key][0]:
			note_set.add(note)
		for note in noteDict[key][1]:
			note_set.discard(note)
			


		if len(note_set)>0:
			print(chord.find_triad(list(note_set))+' at '+str(key))

	#for key in noteDict:
		#print(chord.find_triad(noteDict[key])+' at '+str(key))