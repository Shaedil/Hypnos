from summa.summarizer import summarize

def sumThis(text):

    result = ""
    n = 0.01
    while result == "":
        result = summarize(text, ratio=n)
        n += 0.01

    return result
