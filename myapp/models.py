from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=30)
    created_at =models.DateTimeField(auto_now=True)
    # email =models.CharField(max_length=200)
    email = models.EmailField (null=True ,blank=True)
    phone = models.CharField (null=True ,max_length=20)


    def __str__(self):
        return self.title

