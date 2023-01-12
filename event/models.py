from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    recipient_list = models.TextField()
    scheduled_time = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
