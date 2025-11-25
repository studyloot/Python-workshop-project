from django.db import models

class mstuser(models.Model):
    sno=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=60)
    email=models.CharField(unique=True,max_length=45)
    pwd=models.CharField(max_length=13)
    role=models.CharField(max_length=15)

class course(models.Model):
    courseid=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=20)
    duration=models.IntegerField()
    fees=models.IntegerField()
    coursedetail=models.CharField(max_length=100)
    courseicon=models.CharField(max_length=60)

class batch(models.Model):
    batchno=models.AutoField(primary_key=True)
    batchtitle=models.CharField(max_length=20)
    startdate=models.DateField()
    facultyname=models.CharField(max_length=40)

class admission(models.Model):
    admissionno=models.AutoField(primary_key=True)
    batchno=models.IntegerField()
    admissiondate=models.DateField()
    emailid=models.CharField(max_length=45)