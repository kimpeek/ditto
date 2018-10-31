from random import choice
from string import ascii_letters, digits

from django.db import models


def generate_internal_id(length=5):
    """Create a short unique string of random characters."""

    internal_id = get_random_string(length)

    # Recursively check if the newly created ID already exists. Extend length if so
    # This does not mean that every possible shorter-length string has been used
    if is_extant_string(internal_id):
        return generate_internal_id(length + 1)
    return internal_id


def get_random_string(length):
    """Create a random string that is length-chars
    long comprised of upper, lower, and digits.
    """

    char_pool = [c for c in ascii_letters + digits]
    char_list = [choice(char_pool) for _ in range(length)]
    return ''.join(char_list)


def is_extant_string(string):
    """Check if the string exists in the database"""

    return HyperlinkModel.objects.filter(internal=string).exists()


class HyperlinkModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    original = models.URLField(max_length=255)
    internal = models.CharField(
        default=generate_internal_id,
        editable=False,
        max_length=15
    )

    class Meta:
        db_table = 'hyperlink'
        verbose_name = "hyperlink"
        verbose_name_plural = "hyperlinks"

    def __str__(self):
        return f'{self.internal} - {self.original}'
