from django.db import models

# Create your models here.


class Entry(models.Model):
    text = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f" {self.id} | {self.text[:20]} | {self.date_added} ")
