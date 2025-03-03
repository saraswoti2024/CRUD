from django.db import models

# Create your models here.
class formfill(models.Model):
    namemodel = models.CharField(max_length=50)
    emailmodel = models.EmailField(unique=True)
    imagemodel = models.FileField(upload_to="images",null=True)
    checkmodel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.namemodel} - {self.emailmodel} - {'Checked' if self.checkmodel else 'Not Checked'}"

    