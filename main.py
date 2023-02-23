# Import the required module for text
# to speech conversion
# https://www.geeksforgeeks.org/python-text-to-speech-by-using-pyttsx3/

import pyttsx3
name = 'Женя'
text = 'Солнце моё!'

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
# say method on the engine that passing input text to be spoken
engine.say('Привет Любимая,' + name + 'Добро пожаловать домой, как отдохнула? Следуй за белым кроликом! Каляка маляка, вовка морковка жопка пирожок писечка сосисечка' + text)
# run and wait method, it processes the voice commands.
engine.runAndWait()

#
# # Import the required module for text
# # to speech conversion
# from gtts import gTTS
#
# # This module is imported so that we can
# # play the converted audio
# import os
#
# # The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks!'
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")
#
# # Playing the converted file
# os.system("mpg321 welcome.mp3")

#
# def speak(text):
#     from gtts import gTTS
#     import os
#     tts = gTTS(text=text, lang='ko')
#     tts.save("tmp_talk.mp3")
#     os.system("omxplayer tmp_talk.mp3")
#     os.system("rm -f tmp_talk.mp3")

#
# from gtts import gTTS
# import os
#
# tts = gTTS(text="Под действие закона подпадут любые акции с участием автомобилей", lang='ru')
# tts.save("voice.mp3")
# os.system("omxplayer voice.mp3")



# import gtts
# from playsound import playsound
#
# tts = gtts.gTTS('Привет любимая Женя!', lang='ru')
# tts.save('converted.mp3')
# playsound('converted.mp3')



#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
