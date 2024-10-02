from django.db import models


class LanguageChoice(models.TextChoices):
    PYTHON = "py", "Python"
    JAVA = "java", "JAVA"
    JAVASCRIPT = "js", "JavaScript"
    C = "c", "C"
    C_PLUS_PLUS = "cpp", "C++"
    OTHER = "other", "Other"

