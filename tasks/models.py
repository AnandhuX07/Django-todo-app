from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    PRIORITY_CHOICE = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('Hard','Hard'),
    ]

    STATUS_CHOICE = [
        ('In_progress','In_progress'),
        ('Pending','Pending'),
        ('Done','DOne'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICE,default="Medium")
    due_date = models.DateTimeField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default= "Pending")

    def __str__(self):
        return self.name