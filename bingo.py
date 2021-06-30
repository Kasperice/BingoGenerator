from random import randint
from os import remove
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator


class BingoGenerator:
    def __init__(self, language: str):
        self.language = language.lower()
        self.letters = "BINGO"
        self.bingo_list = []
        self.used = []
        self.translator = Translator()
        self.welcome_text = "Welcome to the game of Bingo. We're starting in three! two! one! Start! "
        self.end_text = "Thanks for playing, I hope you enjoyed it"
        self.results_text = "The values drawn in the game:"

    def __del__(self):
        remove('number.mp3')
        remove('message.mp3')

    def _prepare_bingo_list(self):
        for n, letter in enumerate(self.letters):
            for i in range(1, 16):
                self.bingo_list.append(letter + " " + str(n * 15 + i))

    def _translate_text(self, text: str):
        return self.translator.translate(text, dest=self.language).text

    def _play_message(self, message: str):
        message_text = self._translate_text(message)
        message = gTTS(text=message_text, lang=self.language, slow=False)
        message.save("message.mp3")
        sound = AudioSegment.from_mp3("message.mp3")
        play(sound)

    def _display_results(self):
        self.used.sort()
        results_text = self._translate_text(self.results_text)
        print("\n\n" + results_text)
        for letter in self.letters:
            print(
                f"{letter}: {', '.join([element.split()[1] for element in self.used if letter in element])}"
            )
        print("\n\n")

    def start_game(self):
        self._prepare_bingo_list()
        self._play_message(self.welcome_text)
        try:
            while self.bingo_list:
                n = randint(0, len(self.bingo_list)-1)
                pooled_number = gTTS(text=f";     {self.bingo_list[n]}", lang=self.language, slow=False)
                pooled_number.save("number.mp3")
                sound = AudioSegment.from_mp3("number.mp3")
                play(sound)
                self.used.append(self.bingo_list[n])
                del self.bingo_list[n]

            self._display_results()
            self._play_message(self.end_text)

        except KeyboardInterrupt:
            self._display_results()
            self._play_message(self.end_text)


