from django.db import models

class company(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    location = models.CharField(max_length=255)
    mailId = models.CharField(max_length=255)
    ownerName = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)

    def __self__(self):
        return self.name

class investor(models.Model):
    investor_name = models.CharField(max_length=255)
    no_invested = models.CharField(max_length=255)
    mailId = models.CharField(max_length=255)
    linkedin_profile = models.CharField(max_length=255)

    def __self__(self):
        return self.name