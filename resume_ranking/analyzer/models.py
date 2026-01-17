from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='resumes/')
    score = models.FloatField(default=0)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
