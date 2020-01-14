from django.db import models


class Message(models.Model):
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.message[:10])
