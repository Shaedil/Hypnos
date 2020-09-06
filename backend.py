import os
from summa.summarizer import summarize
import speech_recognition as sr
import wave
import contextlib


blacklist = ["very", "so", "pretty", "always", "the", "are", "is", "but",
             "and", "for", "in", "they", "a"]


def genQ(text, pText):
    # text -> unpunctuated text
    # pText -> punctuated text
    textL = text.split(" ")
    textS = list(set(textL))
    keywords = []
    for i in range(len(textL)//20+1):
        word = max(set(textS), key=textL.count)
        keywords.append(word)
        textS.remove(word)
    for word in keywords:
        pText = pText.replace(word, "_"*len(word))
    # pText -> punctuated text with blanks
    # keywords -> word bank
    questions = []
    pTextL = pText.replace("?", ".").replace("!", ".").split(". ")
    for t in pTextL:
        if t.find("__") != -1:
            questions.append(t)
    return questions, keywords


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
        # print(keywords.keywords(text))
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
    return text


def punctuate(text):
    punctuated_text = os.popen('curl -d "text={}" http://bark.phon.ioc.ee/punctuator'.format(text))
    punctuatedText = punctuated_text.read()
    return punctuatedText


def save_questions(questionsList):
    with open('questions.txt', 'w') as f:
        for item in questionsList:
            if not item == '':
                for i in item:
                    f.write("%s\n" % i)
            else:
                f.write("%s\n" % item)


def save_summary(summaryScript):
    with open('summary.txt', 'w') as f:
        f.write(summaryScript)


def save_transcript(pscript):
    with open('transcript.txt', 'w') as f:
        f.write(pscript)


def backend(file_path):
    script = sample_recognize(file_path)
    pscript = punctuate(script)
    return script, pscript
"""
    questionsList = genQ(script, pscript)
    summaryScript = sumThis(pscript)
    # save_questions(questionsList)
    # save_summary(summaryScript)
    # save_transcript(pscript)
    return script, pscript, questionsList, summaryScript"""


# print(backend("./test.wav"))
