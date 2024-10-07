from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadLanguageValidator:
    def __init__(self, bad_words = None, message = None):
        self.bad_words = bad_words
        self.message = message  # or "The text contains bad language!"

    @property
    def bad_words(self):
        return self._bad_words

    @bad_words.setter
    def bad_words(self, value):
        if value is None:
            self._bad_words = ["bad_word_1", "bad_word_2", "bad_word_3"]
        else:
            self._bad_words = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if value is None:
            self._message = "The text contains bad language!"
        else:
            self._message = value

    def __call__(self, value):
        found_bad_words = [bad_word for bad_word in self.bad_words if bad_word.lower() in value.lower()]
        if found_bad_words:
            bad_words_str = ", ".join(found_bad_words)
            raise ValidationError(f"{self.message} Bad words: {bad_words_str}")
