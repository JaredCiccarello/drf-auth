from django.db import models
from django.contrib.auth import get_user_model


class camera(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length= 280)
    velocity = models.CharField(max_length= 64)
    seen_by = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seen_by

# Create your models here.
