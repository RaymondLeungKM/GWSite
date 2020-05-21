from django.db import models

from tinymce.models import HTMLField

from ckeditor.fields import RichTextField

# Create your models here.
class jobOpenings(models.Model):
    jobTitle = models.CharField(max_length=50, blank=True, null=True)
    jobRespons = models.TextField(blank=True, null=True)
    jobRequirements = models.TextField(blank=True, null=True)
    jobPDF = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.jobTitle

class pressRelease(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title

class companyNews(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    published_date = models.DateField()
    image = models.ImageField()

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

