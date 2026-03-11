from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username

class University(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class College(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    university=models.ForeignKey(University,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name=models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.name}"

class Cutoff(models.Model):
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ("OPEN", "OPEN"),
        ("OBC", "OBC"),
        ("SC", "SC"),
        ("ST", "ST"),
        ("EWS", "EWS"),
        ("NT", "NT"),
        ("VJ", "VJ"),
    ]
    category=models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES        
    )
    percentile = models.FloatField()
    year = models.IntegerField()
    
    class Meta:
        unique_together = ("college","branch", "category", "year")
        
    def __str__(self):
        return f"{self.college} - {self.branch.name} - {self.category}"    
    
class Student(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE, null=True, blank=True)
    percentile=models.FloatField()
    HOME_UNIVERSITY=[
        ('YES','YES'),
        ('NO','NO')
    ]
    
    CATEGORY_CHOICES = [
        ("OPEN", "OPEN"),
        ("OBC", "OBC"),
        ("SC", "SC"),
        ("ST", "ST"),
        ("EWS", "EWS"),
        ("NT", "NT"),
        ("VJ", "VJ"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    home_university=models.CharField(
        max_length=3,
        choices=HOME_UNIVERSITY
    )
    preferred_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.user.username} - {self.percentile}"
    
    
class CollegeDetail(models.Model):
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    cutoff=models.ForeignKey(Cutoff,on_delete=models.CASCADE,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)
    average_package = models.FloatField(null=True, blank=True)
    highest_package = models.FloatField(null=True, blank=True)
    hostel_available = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.college.name