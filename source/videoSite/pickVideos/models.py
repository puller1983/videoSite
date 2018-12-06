from django.db import models

# Create your models here.

class VideoUrl(models.Model):
    url = models.URLField()
    def __str__(self):
        return self.url

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField('birthday')

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name+self.last_name
    

class Parent(Person):
    pass

class Children(Person):
    father = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="father")
    mother = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="mother")
    video_url = models.ManyToManyField(VideoUrl, blank=True)

