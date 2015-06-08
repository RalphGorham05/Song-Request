import speech_recognition as sr


class AudioInput:
    def __init__(self):
        self.song = ''
        self.input_list = []


    def songInput(self):
        print 'Say Song Name'
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
            r.duration = 10

        try:
            print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
            self.song = r.recognize(audio)
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio. Try again")
            songInput()


    def validateSong(self):
        print 'Correct?: Yes or No'
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
            r.duration = 5
        try:
            if (r.recognize(audio) == 'yes'):
                print self.song

            elif(r.recognize(audio) == 'no'):
                songInput()
                print 'sorry i misunderstood. give me another shot!'

        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")


    def getSong(self):
        self.songInput()
        self.validateSong()

'''
def artistInput():
    print 'Which Artist'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 10
    try:
        print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
        return r.recognize(audio)
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio. Try again")
        artistInput()


def validateArtist(phrase):
    print 'Correct?: Yes or No'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 5
    try:
        if (r.recognize(audio) == 'yes'):
            print phrase

        elif(r.recognize(audio) == 'no'):
            artistInput()
            print 'sorry i misunderstood. give me another shot!'

    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")


def delayInput():
    print 'Wait Time'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 5
    try:
        print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
        return r.recognize(audio)
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio. Try again")
        delayInput()


def validateDelay(phrase):
    print 'Correct?: Yes or No'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 5
    try:
        if (r.recognize(audio) == 'yes'):
            print phrase

        elif(r.recognize(audio) == 'no'):
            delayInput()
            print 'sorry i misunderstood. give me another shot!'

    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")


def votesInput():
    print 'How many votes'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 5
    try:
        print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
        return r.recognize(audio)
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio. Try again")
        votesInput()


def validateVotes(phrase):
    print 'Correct?: Yes or No'
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        r.duration = 5
    try:
        if (r.recognize(audio) == 'yes'):
            print phrase

        elif(r.recognize(audio) == 'no'):
            votesInput()
            print 'sorry i misunderstood. give me another shot!'

    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")



so = AudioInput()

so.getSong()


input_list = []

    
song = songInput()
validateSong(song)
input_list.append(song)

artist = artistInput()
validateArtist(artist)
input_list.append(artist)

delay = delayInput()
validateDelay(delay)
input_list.append(delay)

votes = votesInput()
validateVotes(votes)
input_list.append(votes)

print input_list
'''