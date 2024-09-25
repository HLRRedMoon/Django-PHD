from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length = 200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title
    
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction_date = models.DateTimeField(auto_now_add=True)
    prediction_result = models.CharField(max_length=100)
    prediction_name = models.CharField(max_length=100, default="prediction")
    # You can add more fields to store other details about the prediction

    def __str__(self):
        return f"{self.user.username} - {self.prediction_result} - {self.prediction_name}"

