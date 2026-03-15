from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    attendance = models.IntegerField(default=0)
    canteen_debt = models.IntegerField(default=0)
    fashion_level = models.IntegerField(default=0)
    crush_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    strictness = models.IntegerField(default=5)

    def __str__(self):
        return self.name


class News(models.Model):
    headline = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline