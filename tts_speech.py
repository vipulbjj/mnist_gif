import json
from gtts import gTTS
import time
import gc
import os

def tts(string,i):
    #answer=d[i]['ans']
    tts = gTTS(string)
    tts.save("speech/speech_%d.mp3"%(i))
    print(str(i)+"of"+str(num)) 



#var1='vqa_raw_test.json'

# with open(var1) as json_data:
#    d = json.load(json_data)

num=500
i=0
#sentences_list=os.listdir("sentences/")
for filename in os.listdir("sentences/"):
    #print(filename)
    #filename=str(sentences_list[i])+".txt"
    
    i=i+1
    with open("sentences/"+filename, 'r') as file: 
        string = file.read() 

    # answer=d[i]['ans']
    # tts = gTTS(answer)
    # tts.save('../train2014_ans/'+str(d[i]['ques_id'])+'.mp3')
    # print(str(i)+"of"+str(num_ques))
    try:
        tts(string,i)
    except Exception as e:
        print('i am sleeping')
        time.sleep(5)
        tts(string,i)

    else:
        pass
    finally:
        pass



    gc.collect()
    # time.sleep(5)
    # if (i % 2000)==0:
    #     # Wait for 5 seconds
    #     print('i am sleeping')
    #     time.sleep(50)
    # except 'gtts.tts.gTTSError' :
    #     print("Got this error gTTSError.--- handling this")
    #     time.sleep(150)
    #     answer=d[i]['ans']
    #     tts = gTTS(answer)
    #     tts.save('../train2014_ans/'+str(d[i]['ques_id'])+'.mp3')
    #     print(str(i)+"of"+str(num_ques)) 
    #     gc.collect()