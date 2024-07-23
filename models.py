from django.db import models

class modelClass(models.Model):
    i=models.IntegerField()
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    ph=models.IntegerField(max_length=10)
    
    def __str__(self):
        return f"{self.i},{self.name},{self.password},{self.email},{self.ph}"