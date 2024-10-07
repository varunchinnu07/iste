from django.db import models
        
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    domain = models.CharField(max_length=100,choices=[('design', 'Design'), ('tech', 'Tech'), ('Innovation', 'Innovation')],null=True)
    idea_description = models.TextField()
    idea_ppt = models.FileField(upload_to='ppt/', null = True)
    def __str__(self):
        return self.team_name
    
class Participant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='participants',null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
        
class Payment(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    payment_person_name = models.CharField(max_length=100)
    receipt_image = models.ImageField(upload_to='receipts/', null=True)