from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    createdAt = models.DateField(auto_now_add=True)  # Automatically set to current date on creation
    modifiedAt = models.DateField(null=True)  #set to current date on modification
    status = models.BooleanField(default=False)
    Otp = models.CharField(max_length=6, null=True, default=None)  # Nullable OTP field
    Token = models.CharField(max_length=255, null=True, default=None)

class Paragraph(models.Model):
    content = models.TextField()
