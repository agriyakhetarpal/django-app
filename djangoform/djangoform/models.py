from django.db import models
# declare explicit app label name
app_label = 'djangoform'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)