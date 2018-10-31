from django.db import models


class Click(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    hyperlink = models.ForeignKey('compressor.HyperlinkModel', on_delete=models.CASCADE)
    referrer = models.CharField(max_length=255)

    def get_age(self):
        return

    def get_click_count(self):
        """use count"""
        return

    def get_last_click(self):
        # get newest click
        return

    def get_top_referrer(self):
        return
