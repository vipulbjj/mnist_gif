import json
import os
import argparse



#sentences_list=os.listdir("/sentences")
#gifs_list
#The project folder contains this file as well as 4 folders : sentences, images, text, speech
def main(params):
	list = []
	for i in range(params[count]):

		with open("sentences/sentence_%d.txt"%(i), 'r') as file: 
        	     string = file.read() 
            
        sentence = string
        unique_id = i
        gif_path = 'gifs/gif_%d.npy'%(i)
            #gif is in the npy format
        speech_path = 'speech/speech_%d.png'%(i)
        text_path = 'text/text_%d.npy'%(i)

        list.append({'unique_id': i, 'gif_path': gif_path, 'sentence': sentence, 'speech_path': speech_path, 'text_path': text_path })



	print 'Training sample %d' %(len(list))
	json.dump(list, open('multimodal.json', 'w'))	



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    
    parser.add_argument('--count', default=500, type=int, help='Number of gifs you want in your json')
    
  
    args = parser.parse_args()
    params = vars(args)
    print 'parsed input parameters:'
    print json.dumps(params, indent = 2)
    main(params)
