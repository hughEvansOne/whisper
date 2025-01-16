import whisper

model = whisper.load_model("turbo")
result = model.transcribe("harvard.wav")
print(result["text"])
