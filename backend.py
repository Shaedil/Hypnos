import os
from summa.summarizer import summarize
from summa import keywords
import speech_recognition as sr
import wave
import contextlib

blacklist = ["very", "so", "pretty", "always", "the", "are", "is", "but",
             "and", "for", "in", "they", "a"]


def genQ(text, pText):
    textL = text.split(" ")
    textS = list(set(textL))
    keywords = []
    for i in range(len(textL)//20+1):
        word = min(set(textS), key=textL.count)
        keywords.append(word)
        textS.remove(word)
    for word in keywords:
        pText.replace(word, "_"*len(word))
    return pText, keywords

def stripUseless(text):
    global blacklist
    for word in blacklist:

        text = text.replace(" "+word+" ", " ")

    return text


def sumThis(text):
    result = ""
    # n = 0.01
    while result == "":
        result = summarize(text)
        print(keywords.keywords(text))
        # result = summarize(text, ratio=n)
        # n += 0.01
        # if n > 1:
        #     result = text
        #     break

    return result


def sample_recognize(fname):
    head, tail = os.path.split(fname)
    if not(tail[-4:] == '.wav'):
        wavname = head + '/' + tail[:-4] + '.wav'
        os.popen('ffmpeg -i {} {}'.format(fname, wavname))
        if 'ffmpeg: command not found' in wavname:
            return("ffmpeg is not installed")
    else:
        wavname = fname

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
    # here is where the punctuated functon is called
    punctuated_text = punctuate(text)
    return text


def punctuate(text):
    punctuated_text = os.popen('curl -d "text={}" http://bark.phon.ioc.ee/punctuator'.format(text))
    punctuatedText = punctuated_text.read()
    return punctuatedText


def backend(file_path):
    script = sample_recognize(file_path)
    summaryScript = sumThis(script)
    return script, summaryScript


# print(backend("/home/shaedil/Downloads/recordings/Recording 1.wav"))
print(backend("./test.wav"))
