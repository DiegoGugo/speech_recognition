import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz:')
        r.adjust_for_ambient_noise(source, duration = 5)
        audio = r.listen(source)
        print(audio)
        try:
            text = r.recognize_google(audio)
            print(f'Has dicho: {text}')
            print(text)
            if text in 'Amazon':
                webbrowser.open('http://amazon.es')
            if 'news' in text:
                webbrowser.open('https://www.bbc.com/mundo')
            if 'hello' in text:
                print('Bien y tu?')
        except:
            print('No te he entendido')