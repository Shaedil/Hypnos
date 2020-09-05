import os
from summa.summarizer import summarize
import speech_recognition as sr
import wave
import contextlib


def sumThis(text):
    result = ""
    n = 0.01
    while result == "":
        result = summarize(text, ratio=n)
        n += 0.01
        if n > 1:
            result = text
            break

    return result


def sample_recognize(fname):
    stream = os.popen('ffmpeg -i {} {}'.format(fname, fname+'.wav'))
    head, tail = os.path.split(fname)
    wavname = head + fname+'.wav'
    if 'ffmpeg: command not found' in wavname:
        return("ffmpeg is not installed")

    with contextlib.closing(wave.open(wavname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    seg = duration//10+1
    r = sr.Recognizer()
    aFile = sr.AudioFile(wavname)

    with aFile as source:
        # audio = r.record(source)
        audio = []
        work = True
        n = 0
        while work:
            # print(n)
            n += 1
            try:
                audio.append(r.record(source, duration=10))
            except:
                work = False
            if n >= seg:
                break
    text = ""
    for a in audio:
        try:
            text1 = r.recognize_google(a)
            # print(text1)
            text = text+" "+text1
        except:
            pass
    return text


def backend(file_path):
    script = sample_recognize(file_path)
    summaryScript = sumThis(script)
    return script, summaryScript


# print(backend("/home/shaedil/Downloads/recordings/Recording 1.wav"))
print(backend("/home/shaedil/Downloads/recordings/recording1.mp3"))
