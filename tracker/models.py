from django.db import models
from django.contrib.auth.models import User


class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    
class Tasks(models.Model):
    PHASE_CHOICES = [
        ('NS', 'Not Started'),
        ('PD', 'Pending'),
        ('IP', 'In Progress'),
        ('CM', 'Completed'),
        ('BH', 'Behind'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    phase = models.CharField(max_length=2, choices=PHASE_CHOICES, default='NS')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

