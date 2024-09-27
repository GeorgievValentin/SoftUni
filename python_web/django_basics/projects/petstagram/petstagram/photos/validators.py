from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# validator made via function - NOT THE BEST OPTION
# def validate_size(value):
#     if value.size > 5 * 1024 * 1024:
#         raise ValidationError("File is too big! It must be less or equal to 5MB.")


# validator made via class - most flexibility and pythonic method
@deconstructible
class FileSizeValidator:
    def __init__(self, file_size_mb: int, message = None):  # <- in here we initialize the validator, don't call it
        self.file_size_mb = file_size_mb
        self.message = message  # or f"File is too big! It must be less or equal to {file_size_mb}."

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File is too big! It must be less or equal to {self.file_size_mb}."
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.file_size_mb * 1024 * 1024:
            raise ValidationError(self.message)


