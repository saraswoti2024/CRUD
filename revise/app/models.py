from django.db import models

# Create your models here.
class formfill(models.Model):
    namemodel = models.CharField(max_length=50)
    emailmodel = models.EmailField(unique=True)
    imagemodel = models.FileField(upload_to="images")
    videomodel = models.FileField(upload_to="video",null=True)
    checkmodel = models.BooleanField(default=False)
    isdelete = models.BooleanField(default=False)
    isdelete2 = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f"{self.namemodel} - {self.emailmodel} - {'Checked' if self.checkmodel else 'Not Checked'}"

    