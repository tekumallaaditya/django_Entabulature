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

class constructionPicsDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "constructionPics"

class elevationPicsDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "elevationPics"


class interiorPicsDB(models.Model):
    title = models.CharField(max_length=20)
    thumb = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "interiorPics"

class teamDB(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=100)
    pic = models.ImageField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "team"

class blogDB(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(blank=True)
    story = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "blog"

class testimonialDB(models.Model):
    name = models.CharField(max_length=20)
    testimonial = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "testimonials"

class contactUsDB(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "contactUs"







