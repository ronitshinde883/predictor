from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name=models.CharField(max_length=100)
    

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
        return self.name

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
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    percentile = models.FloatField()
    year = models.IntegerField()
    
    class Meta:
        unique_together = ("college", "branch", "category", "year")
        
    def __str__(self):
        return f"{self.college} - {self.branch} ({self.year})"    
    
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    cet_percentile=models.FloatField()
    category=models.CharField(max_length=100)
    home_university=models.ForeignKey(University,on_delete=models.CASCADE)
    preferred_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.full_name