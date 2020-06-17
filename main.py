from googletrans import Translator
import sys

print("Please paste Spanish lyrics and then press Alt+D:")
lyrics = sys.stdin.readlines()
translator = Translator()
for line in lyrics:
    trans = translator.translate(line, dest='en')
    if line != '\n':
        print(line.replace('\n', ''))
        print(trans.text)
    else:
        print('\n')
