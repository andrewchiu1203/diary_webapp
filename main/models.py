from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
    
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 128)
    body = RichTextField(blank = True, null = True)
    created = models.CharField(default = timezone.now, max_length = 128)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']