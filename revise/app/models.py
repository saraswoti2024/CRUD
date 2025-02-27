from django.db import models

# Create your models here.
class formfill(models.Model):
    namemodel = models.CharField(max_length=50)
    emailmodel = models.EmailField(unique=True)
    imagemodel = models.ImageField(upload_to="images")
    