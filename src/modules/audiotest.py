import pyaudio
import wave
import os

#The following code comes from markjay4k as referenced below
form_1 = pyaudio.paInt16
chans=1
samp_rate = 16000
chunk = 4096
record_secs = 10     #record time
dev_index = 0
wav_output_filename = 'test1.wav'


audio = pyaudio.PyAudio()

#setup audio input stream
stream=audio.open(format = form_1,rate=samp_rate,channels=chans, input_device_index = dev_index, input=True, frames_per_buffer=chunk)
print("recording")
frames=[]

for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data=stream.read(chunk,exception_on_overflow = False)
    frames.append(data)

print("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

#creates wave file with audio read in
#Code is from the wave file audio tutorial as referenced below
wavefile=wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

#plays the audio file
os.system("aplay test1.wav")