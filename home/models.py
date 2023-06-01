from django.db import models
from datetime import date

today = date.today()

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    # In admin dashboard for Contacts - each row is shown as contact object(1) - to change it to name field of each contact:
    def __str__(self):
        return self.name + " - " + self.email

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)  # Primary Key
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20, default="Shoubhit")
    tags = models.CharField(max_length=40, default="Django, Wordpress, Bootstrap")
    date = models.CharField(max_length=30, default=today.strftime("%b %d, %Y"))
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    # time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", default="")

    def __str__(self):  #Tunder method
        return self.title