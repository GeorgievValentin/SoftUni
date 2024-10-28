from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message = None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PasscodeValidator:
    def __init__(self, message = None, length = None):
        self.message = message
        self.length = length

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your passcode must be exactly 6 digits!"
        else:
            self.__message = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value is None:
            self.__length = 6
        else:
            self.__length = value

    def __call__(self, value: str, *args, **kwargs):
        if not (value.isdigit() and len(value) == self.length):
            raise ValidationError(self.message)