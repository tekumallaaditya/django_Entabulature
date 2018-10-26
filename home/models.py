from django.db import models


class homeDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "home"

class projectsDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)
    thumb1 = models.ImageField(blank=True)
    thumb2 = models.ImageField(blank=True)
    thumb3 = models.ImageField(blank=True)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "projects"
