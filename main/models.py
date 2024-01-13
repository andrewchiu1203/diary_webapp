from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 128)
    body = RichTextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']