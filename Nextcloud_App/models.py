from django.db import models

# Create your models here.


#  Contact models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    contname = models.CharField(max_length=100)
    contemail = models.EmailField(max_length=100)
    contmessage = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.contname
