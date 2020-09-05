from summa.summarizer import summarize
import speech_recognition as sr
import wave
import contextlib


def sumThis(text):
    result = ""
    n = 0.01
    while result == "" and n < 1:
        result = summarize(text, ratio=n)
        n += 0.01
        if n > 1:
            result = text
            break

    return result


def sample_recognize(fname):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    seg = duration//10+1
    r = sr.Recognizer()
    aFile = sr.AudioFile(fname)

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
