from django.db import models

# Create your models here.
class userprofile(models.Model):
    name=models.CharField(max_length=100)
    

class University(models.Model):
    name=models.CharField(max_length=100)

class College(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    university=models.ForeignKey(University,on_delete=models.CASCADE)
class Branch(models.Model):
    branch=models.CharField(max_length=100)

class Cuttoff(models.Model):
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    university=models.ForeignKey(University,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    percentile = models.FloatField()
    year = models.IntegerField()
    
    class Meta:
        unique_together = ("college", "branch", "category", "year")
        
class Student(models.Model):
    full_name=models.CharField(max_length=20)
    email=models.EmailField()
    cet_percentile=models.FloatField()
    category=models.CharField(max_length=50)
    home_university=models.ForeignKey(University,on_delete=models.CASCADE)
    preferred_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    