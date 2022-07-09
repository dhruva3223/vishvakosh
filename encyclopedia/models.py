from distutils.command.upload import upload
from django.db import models
import uuid
import os


# Create your models here.
# class User(models.Model):
    # img = models.ImageField(upload_to = "static/picture");
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "hhsadashs.png"
    return os.path.join(instance.directory_string_var, filename)

class User(models.Model):
    img = models.ImageField(upload_to = get_file_path)
    directory_string_var = 'static/picture'