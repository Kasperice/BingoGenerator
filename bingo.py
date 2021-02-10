from gtts import gTTS
import subprocess
import os
import random


DEVNULL = open(os.devnull, "wb")

language = "en"
letters = "BINGO"
bingo_list = []
used = []

for n, letter in enumerate(letters):
    for i in range(1, 16):
        bingo_list.append(letter + " " + str(n * 15 + i))

print(bingo_list)

speech = gTTS(
    text="Witajcie na zawodach w Bingo. Zaczynamy za trzy! dwa! jeden! START!",
    lang=language,
    slow=False,
)
speech.save("text.mp3")
subprocess.run("play text.mp3 -t alsa", shell=True)

while bingo_list:
    n = random.randint(0, len(bingo_list))
    try:
        print(bingo_list[n])
        speech = gTTS(text=";     " + bingo_list[n], lang=language, slow=False)
        speech.save("text.mp3")
        subprocess.run("play text.mp3 -t alsa", stdout=None, shell=True)
        used.append(bingo_list[n])
        del bingo_list[n]
    except IndexError:
        continue

    except KeyboardInterrupt:
        used.sort()
        # print(used)
        for letter in letters:
            print(
                letter
                + ": "
                + ", ".join([element.split()[1] for element in used if letter in element])
            )
        break
