class WordCounter:
    def __init__(self, text=""):
        self._text = text

    # Getter for text
    @property
    def text(self):
        return self._text

    # Setter for text
    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError("Text must be a string")

    # Count the number of words
    def count_words(self):
        return len(self._text.split())