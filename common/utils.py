import re


NUMBER = r"^\d+$"
LETTERS_SPACES = re.compile(r"^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ\s]+$")
LETTERS = re.compile(r"^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ\s]+$")
PHONE_NUMBER = r"^\+?\d+$"
ACADEMIC_PERIOD_FORMAT = r'^\d{4}-\d{4}$'

