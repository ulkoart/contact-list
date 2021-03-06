from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
