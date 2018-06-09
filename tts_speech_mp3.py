import json
from gtts import gTTS
import time
import gc

def tts(string,i):
    tts = gTTS(string)
    tts.save("speech/speech_%d.mp3"%(i))
    print(str(i)+"of"+str(num)) 



#var1='vqa_raw_test.json'
num=500
# with open(var1) as json_data:
#    d = json.load(json_data)

#num_ques=len(d)

for i in range(1,num):
    # answer=d[i]['ans']
    # tts = gTTS(answer)
    # tts.save('../train2014_ans/'+str(d[i]['ques_id'])+'.mp3')
    # print(str(i)+"of"+str(num_ques))
    
    with open("sentences/sentence_%d.txt"%(i), 'r') as file: 
        string = file.read() 


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