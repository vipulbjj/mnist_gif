import os
import scipy.io.wavfile
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import gc
# def Diff(li1, li2):
#     return (list(set(li1) - set(li2)))

# directory1 = '/users/gpu/pandas/audio_vqa/data/OpenEnded_mscoco_train2014_questions/'
# directory2 = '/users/gpu/pandas/audio_vqa/data/OpenEnded_mscoco_train2014_questions_Spectrograms1/'
# lst1=[]
# lst2=[]

# for filename1 in os.listdir(directory1):
#     lst1.append(str(filename1[:-4]))
#     gc.collect()
# for filename2 in os.listdir(directory2):
#     lst2.append(str(filename2[:-4]))
#     gc.collect()
# count=0
# lst1.sort()
# lst2.sort()
# print(lst1)
# print(lst2)

# lst3=Diff(lst1,lst2)
# num_ques=len(lst3)
# print(num_ques)
# print(lst3)
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