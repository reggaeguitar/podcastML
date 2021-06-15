from os import path
from pydub import AudioSegment

#AudioSegment.converter = "C:/p/ffmpeg/bin/ffmpeg.exe"

# files                                                                         
src = "C:/p/PodcastML/20190404_AVeryOffensiveRomCom.mp3"
dst = "C:/p/PodcastML/20190404_AVeryOffensiveRomCom.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")