from django.db import models

# Create your models here.
class Sendmoney(models.Model):
    amount = models.FloatField(max_length=255, default=0)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    receiverPhone = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['created']
    def __str__(self):
        return self.sender