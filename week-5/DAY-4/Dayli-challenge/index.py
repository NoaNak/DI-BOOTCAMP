class Text:
    def __init__(self, text: str) -> None:
        self.text = text
        self.word_frequency: dict = self.frequency()

    def frequency(self) -> dict:

        text_lines = self.text.split(' ')

        frequency = {}

        for word in text_lines:
            word_strp = word.strip(',\n.?;!').lower()
            if word_strp not in frequency:
                frequency[word_strp] = 1
            else:
                frequency[word_strp] += 1

        return frequency

    def most_frequent_word(self) -> tuple[str, int]:
        most_frequent = 0
        most_frequent_word = ''

        for word, frequency in self.word_frequency.items():
            if frequency > most_frequent:
                most_frequent_word = word
                most_frequent = frequency
        
        return most_frequent_word, most_frequent

    def unique_words(self) -> list:
        return sorted(list(text_obj.word_frequency))
    

file_location = 'stranger.txt'
text_stranger = ""

with open(file_location, 'r') as file:
    text_stranger = file.read()

text_obj = Text(text_stranger)