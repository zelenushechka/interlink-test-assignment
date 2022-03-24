from django.db import models


class PortComponent(models.Model):
    location = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.location


class User(models.Model):
    port = models.ForeignKey(PortComponent, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name
