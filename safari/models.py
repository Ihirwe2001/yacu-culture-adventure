from django.db import models

# Create your models here.
class Booking(models.Model):
    DESTINATION_CHOICES = [
        ('Kigali city', 'Kigali city'),
        ('Northern Province', 'Northern Province'),
        ('Southern Province', 'Southern Province'),
        ('Eastern Province', 'Eastern Province'),
        ('Western Province', 'Western Province'),
    ]
    
    DURATION_CHOICES = [
        ('Hours', 'Hours'),
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
    ]
    
    destination1 = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    destination2 = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    email = models.EmailField()
    names = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    depart_date = models.DateTimeField()
    return_date = models.DateTimeField()
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)

    def __str__(self):
        return f"{self.names} - {self.destination1} to {self.destination2}"