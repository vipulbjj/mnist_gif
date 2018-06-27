import os
import pydub
import glob

mp3_files = glob.glob('./*.mp3')

for mp3_file in mp3_files:
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'
    sound = pydub.AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")
    os.remove(mp3_file)
print("Conversion Complete")
