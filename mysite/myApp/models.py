from django.db import models

# Create your models here.
class Grades(models.Model):
    gname    = models.CharField(max_length = 20)
    gdate    = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum  = models.IntegerField()
    isDelete = models.BooleanField(default = False)

    def __str__(self):
        #return "{0}-{1}-{2}".format(self.gname,self.ggirlnum,self.gboynum)
        return self.gname

class Students(models.Model):
    sname = models.CharField(max_length = 20)
    sgender = models.BooleanField(default = True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length = 20)
    isDelete = models.BooleanField(default = False)
    #关联外键 Django 2.0以后必须加on_delete参数,否则报异常.
    sgrade = models.ForeignKey("Grades",on_delete = models.CASCADE)

    def __str__(self):
        return self.sname
