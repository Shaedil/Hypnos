<div align="center">
	<h1>Hypnos</h1>
	<blockquote>
		<p><i><b>Sleep in tonight 🌙 Read less tomorrow 🔆 </i></b></p>
		<p><i>Hypnos is a transcript-generating summarizer that aims to help students get up-to-speed from their recorded class lecture that morning.</i></p>
		<p><b>To be submitted as part of the "First Day Back Hacks" hackathon by MLH</b></p>
	<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
	<img src="https://img.shields.io/badge/Made%20with-python-blue?style=for-the-badge">
	<img src="https://img.shields.io/badge/Made%20with-Google%20Cloud-orange?style=for-the-badge">
	</blockquote>
</div>

## Inspiration

The idea came from our personal experiences of being night owls. As night owls, **we sleep late at night and wake up late in the morning**. As you can probably tell, this also means **we miss morning lectures**, which is disappointing because we'd have to watch the recorded lecture which may be an hour long.

Long story short, we wanted to find **a way to read the video transcript in less time than required**. Now, we could just speed up the video lecture to 2X speed. But, the audio would be incomprehensible. Also, **many people do not learn by watching lectures, most learn by reading**. So, we decided to create Hypnos.

Hypnos also goes beyond the classroom. Stuck in a boring meeting? are your the minute taker? just record the meeting and upload you audio file into our app and get a full text document! Now you can play games during your meeting :p

## What it does

Hypnos was designed to take your class lecture video that may be an hour long and segments it into 10 seconds (*one of our challenges. Explained later*) in which the transcripts are generated and stitched back into one full transcript. Hypnos then takes that full transcript and runs it through the textrank algorithm, which ranks sentences based on their importance, meaning and their word frequency. **From this, a reduced transcript is generated that can be as much as 50% of the original, which is INSANE**


## How we Built it

Using **Google Cloud's speech-to-text API**, we managed to create a transcript from a video. Using a separate **'textrank' algorithm, we summarized the transcript** by a factor of 20%, which seems to be the point at which useful information becomes removed (at least from our testing). After that, we layered a simple GUI over it for the convenience of the user so that they can import a video and get a summarized transcript into PDF format.

## Challenges that we ran into

We hit our first major bump when designing the process. We had multiple ideas and APIs we wanted to use, you know, **conflict of interest**. We decided on using Google Cloud's APIs and the textrank algorithm as our approach. However, when using the Google Cloud APi, **we were limited by the amount of data we could send to the API**. We were only able to send 10 seconds of audio at a time. **It was frustrating** for us because we found no other viable library or API that didn't have a limit on its use. But, we managed to overcome the hurdle and segment videos in 10 seconds and stitch the text back up again.

## What we learned

This was our **first time handling machine learning models** like these and the **google cloud API as well**. And though we're grateful for the opportunities it provided, it did not come without a learning curve. Many times, even when an idea *works* well on paper, the commands don't execute *exactly* how you would expect them to. **We had to strain our brains to search for workarounds until one of them *finally* worked!** We'll definitely carry these solutions with us well off into the future.

## What's next for Hypnos

We had a brainstorming session the other day and we wanted to incorporate something spectacular into Hypnos. **We thought about how hard it must be for teachers to create questions based on content they have said, especially when they don't remember what they said**. This will be helpful for teachers to prepare their students on their quizzes which test on things that have been said, but not written down. **It's always a nuisance when that happens**. Now with Hypnos, teachers will be able to generate questions on recorded videos with a click of a button. Questions generated will generally follow the format: "------ is a property of matter dealing with how much stuff it contains" Answer: *Volume*

## Try it out

**[https://github.com/Shaedil/Hypnos](https://github.com/Shaedil/Hypnos)**
