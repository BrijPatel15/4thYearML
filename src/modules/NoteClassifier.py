import pyaudio
import wave
import os

def matching_freq(freq):
    note=""
    if(freq>15 and freq<17.32):
        note= "C0"
        return note
    elif(freq>17.32 and freq<19.45):
        note="D0"
        return note
    elif(freq>19.45 and freq<20.8):
        note="E0"
        return note
    elif(freq>20.8 and freq<23.12):
        note="F0"
        return note
    elif(freq>23.12 and freq<25.96):
        note="G0"
        return note
    elif(freq>25.96 and freq<29.14):
        note="A0"
        return note
    elif(freq>29.14 and freq<31):
        note="B0"
        return note
    elif(freq>31 and freq<34.65):
        note="C1"
        return note
    elif(freq>34.65 and freq<38.89):
        note="D1"
        return note
    elif(freq>38.89 and freq<42):
        note="E1"
        return note
    elif(freq>42 and freq<46.25):
        note="F1"
        return note
    elif(freq>46.25 and freq<51.91):
        note="G1"
        return note
    elif(freq>51.91 and freq<58.27):
        note="A1"
        return note
    elif(freq>58.27 and freq<63):
        note="B1"
        return note
    elif(freq>63 and freq<69.30):
        note="C2"
        return note
    elif(freq>69.30 and freq<77.78):
        note="D2"
        return note
    elif(freq>77.78 and freq<85):
        note="E2"
        return note
    elif(freq>85 and freq<92.50):
        note="F2"
        return note
    elif(freq>92.50 and freq<103.83):
        note="G2"
        return note
    elif(freq>103.83 and freq<116.54):
        note="A2"
        return note
    elif(freq>116.54 and freq<126):
        note="B2"
        return note
    elif(freq>126 and freq<138.59):
        note="C3"
        return note
    elif(freq>138.59 and freq<155.56):
        note="D3"
        return note
    elif(freq>155.56 and freq<168):
        note="E3"
        return note
    elif(freq>168 and freq<185):
        note="F3"
        return note
    elif(freq>185 and freq<207.65):
        note="G3"
        return note
    elif(freq>207.65 and freq<233.08):
        note="A3"
        return note
    elif(freq>233.08 and freq<253):
        note="B3"
        return note
    elif(freq>253 and freq<277.18):
        note="C4"
        return note
    elif(freq>277.18 and freq<311.13):
        note="D4"
        return note
    elif(freq>311.13 and freq<338):
        note="E4"
        return note
    elif(freq>338 and freq<369.99):
        note="F4"
        return note
    elif(freq>369.99 and freq<415.3):
        note="G4"
        return note
    elif(freq>415.3 and freq<466.16):
        note="A4"
        return note
    elif(freq>466.16 and freq<500):
        note="B4"
        return note
    elif(freq>500 and freq<554.37):
        note="C5"
        return note
    elif(freq>554.37 and freq<622.25):
        note="D5"
        return note
    elif(freq>622.25 and freq<675):
        note="E5"
        return note
    elif(freq>675 and freq<740):
        note="F5"
        return note
    elif(freq>740 and freq<830):
        note="G5"
        return note
    elif(freq>830 and freq<932):
        note="A5"
        return note
    elif(freq>932 and freq<1000):
        note="B5"
        return note
    elif(freq>1000 and freq<1108):
        note="C6"
        return note
    elif(freq>1108 and freq<1244):
        note="D6"
        return note
    elif(freq>1244 and freq<1350):
        note="E6"
        return note
    elif(freq>1350 and freq<1480):
        note="F6"
        return note
    elif(freq>1480 and freq<1661.22):
        note="G6"
        return note
    elif(freq>1661.22 and freq<1864):
        note="A6"
        return note
    elif(freq>1864 and freq<2000):
        note="B6"
        return note
    elif(freq>2000 and freq<2217.46):
        note="C7"
        return note
    elif(freq>2217.46 and freq<2489.02):
        note="D7"
        return note
    elif(freq>2489.02 and freq<2700):
        note="E7"
        return note
    elif(freq>2700 and freq<2960):
        note="F7"
        return note
    elif(freq>2960 and freq<3322.4):
        note="G7"
        return note
    elif(freq>3322.4 and freq<3729):
        note="A7"
        return note
    elif(freq>3729.31 and freq<4040):
        note="B7"
        return note
    elif(freq>4040 and freq<4435):
        note="C8"
        return note
    elif(freq>4435 and freq<4978):
        note="D8"
        return note
    elif(freq>4978 and freq<5350):
        note="E8"
        return note
    elif(freq>5350 and freq<5919):
        note="F8"
        return note
    elif(freq>5919 and freq<6644):
        note="G8"
        return note
    elif(freq>6644 and freq<7458):
        note="A8"
        return note
    elif(freq>7458 and freq<8000):
        note="B8"
        return note


def note_detect(audio_file):

    #The following code comes from markjay4k as referenced below
    form_1 = pyaudio.paInt16
    chans=1
    samp_rate = 16000
    chunk = 4096
    record_secs = 1     #record time
    dev_index = 2
    wav_output_filename = 'test1.wav'


    audio = pyaudio.PyAudio()

    #setup audio input stream
    stream=audio.open(format = form_1,rate=samp_rate,channels=chans, input_device_index = dev_index, input=True, frames_per_buffer=chunk)

    print("recording")
    frames=[]

    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data=stream.read(chunk,exception_on_overflow = False)
        frames.append(data)

        data = np.divide(data, float(2**15))
        window = data * np.blackmanharris(len(sound))
        f = np.fft.fft(window)
        i_max = np.argmax(abs(f))
        print(i_max)
        freq = (i_max * fs)/len(sound)
        print(freq)
        Detected_Note = matching_freq(freq)
        print(Detected_Note)


    print("finished recording")

note_detect("")
    #
    # Detected_Note = []
    # length = audio_file.getnframes()
    # sound  = np.zeros(length)
    #
    # for i in range(length):
    #     data = audio_file.readframes(1)
    #     data = struct.unpack("<h", data)
    #     sound[i] = int(data[0])
    #
    # sound = np.divide(sound, float(2**15))
    # window = sound * np.blackmanharris(len(sound))
    # f = np.fft.fft(window)
    # i_max = np.argmax(abs(f))
    # print(i_max)
    # freq = (i_max * fs)/len(sound)
    # print(freq)
    # Detected_Note = matching_freq(freq)
    # return Detected_Note`
