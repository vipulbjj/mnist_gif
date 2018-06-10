import os
import scipy.io.wavfile
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import gc

for i in range(1):
    # c=str(lst3[i])
    # # print(c)
    # b=c+'.mp3'
    # # print(b)
    # a=os.path.join(directory1,b)
    # print(a)
    a="/home/bajaj/Desktop/speech_1.mp3"
    
    signal, sample_rate = librosa.load(a,sr = 16000)
    plt.specgram(signal, Fs=sample_rate,xextent=(0,100))
    plt.axis('off')
    plt.savefig('/home/bajaj/Desktop/spec_mp3.png')
    #print(str(i)+"of"+str(num_ques)) 
    plt.close()
    gc.collect()
