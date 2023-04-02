from django.db import models

class Task(models.Model):
    id= models.AutoField(
                auto_created = True,
                unique=True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID_nama: ')
    content = models.CharField(max_length=50, null=True, blank=False)
    date = models.BigIntegerField()

    def __str__(self):
        return "%s %s" % (self.content, self.date)
