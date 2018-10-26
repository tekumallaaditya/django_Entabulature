from django.db import models


class homeDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "home"