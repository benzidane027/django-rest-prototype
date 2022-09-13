from distutils.command.upload import upload
from email.policy import default
from django.db import models


class Adreas(models.Model):
    city = models.CharField(max_length=50, null=True, blank=True,
            choices=[
                ("27","mostagane"),
                ("31","oran"), 
                ("48","relizan")
                ]
            )
    zip = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.city, self.zip)

# Create your models here.


class Testify(models.Model):
    #id=models.AutoField()
    name = models.CharField(max_length=100, verbose_name="name" ,blank=True)
    age = models.IntegerField(default=0)
    maried = models.BooleanField(default=False)
    pic = models.ImageField(upload_to="firsty/public/upload_file", default="")
    discription = models.TextField(blank=True)
    #adreas=models.OneToOneField(Adreas,on_delete=models.CASCADE,default="")
    def __str__(self) -> str:
        return self.name 
