import random
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


language = "en"
letters = "BINGO"
used = []


def prepare_bingo_list():
    bingo_list = []
    for n, letter in enumerate(letters):
        for i in range(1, 16):
            bingo_list.append(letter + " " + str(n * 15 + i))

    return bingo_list


def play_welcome_message(language):
    if language == 'pl':
        welcome_text = "Witajcie na zawodach w Bingo. Zaczynamy za trzy! dwa! jeden! START!"
    else:
        welcome_text = "Welcome to the Bingo game. Start in three! two! one! Go!"
    message = gTTS(text=welcome_text, lang=language, slow=False)
    message.save("welcome_message.mp3")
    sound = AudioSegment.from_file("welcome_message.mp3")
    play(sound)


bingo_list = prepare_bingo_list()
play_welcome_message(language)


while bingo_list:
    n = random.randint(0, len(bingo_list))
    try:
        print(bingo_list[n])
        pooled_number = gTTS(text=f";     {bingo_list[n]}", lang=language, slow=False)
        pooled_number.save("pooled_number.mp3")
        sound = AudioSegment.from_file("pooled_number.mp3")
        play(sound)
        used.append(bingo_list[n])
        del bingo_list[n]
    except IndexError:
        continue

    except KeyboardInterrupt:
        used.sort()
        for letter in letters:
            print(
                f"{letter}: {', '.join([element.split()[1] for element in used if letter in element])}"
            )
        break
