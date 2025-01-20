import whisper
import os

from pydub import AudioSegment
from pydub.utils import make_chunks

os.system("python3 -m pip freeze | grep whisper")
os.system("pip -V")

myaudio = AudioSegment.from_file("harvard.wav" , "wav") 
chunk_length_ms = 10000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 10 seconds

model = whisper.load_model("turbo")

for i, chunk in enumerate(chunks):
    chunk_name = "chunks/chunk{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")
    result = model.transcribe(chunk_name)
    print(result["text"])
