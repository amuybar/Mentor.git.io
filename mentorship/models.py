from django.db import models
from django.contrib.auth.models import User
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')  # Upload images to a 'testimonials/' directory
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
 
 


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    expertise = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    student_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
    
    from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    # twitter = models.URLField(blank=True, null=True)
    # facebook = models.URLField(blank=True, null=True)
    # instagram = models.URLField(blank=True, null=True)
    # linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    

   

