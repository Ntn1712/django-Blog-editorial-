from django.db import models

# Create your models here.
class articles(models.Model):
    Name = models.CharField(max_length=300)
    Topic = models.CharField(max_length=500)
    Content = models.CharField(max_length=5000)

    def __str__(self):
        return self.Topic

class posts(models.Model):
    Name = models.CharField(max_length=300)
    Topic = models.CharField(max_length=500)
    Content = models.CharField(max_length=5000)

    def __str__(self):
        return self.Topic

class bangalore(models.Model):
    Name = models.CharField(max_length=300)
    Comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.Name

class delhi(models.Model):
    Name = models.CharField(max_length=300)
    Comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.Name

class chennai(models.Model):
    Name = models.CharField(max_length=300)
    Comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.Name

class mumbai(models.Model):
    Name = models.CharField(max_length=300)
    Comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.Name

class ques(models.Model):
    Ques = models.CharField(max_length=2000)

    def __str__(self):
        return self.Ques