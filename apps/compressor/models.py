from random import choice
from string import ascii_letters, digits

from django.db import models


def generate_internal_id(length=5):
    """Create a short string of unique random characters."""

    char_pool = [c for c in ascii_letters + digits]
    char_list = [choice(char_pool) for _ in range(length)]
    internal_id = ''.join(char_list)

    # Recursively check if the newly created ID already exists. Extend length if so
    # This does not mean that ever possible shorter length string has been used
    if HyperlinkModel.objects.filter(internal=internal_id).exists():
        return generate_internal_id(length + 1)
    return internal_id


class HyperlinkModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    original = models.URLField(max_length=254)
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
