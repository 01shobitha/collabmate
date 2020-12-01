from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#language
class Language(models.Model):
    lang_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['lang_name']

#languageUser
class LanguageUser(models.Model):
    land_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}'


#Project
class Project(models.Model):
    proj_name = models.CharField(max_length=100)
    description = models.TextField(max_length = 700, blank = True)
    git_hub_link = models.TextField(max_length = 1000, blank = True)
    proj_link = models.TextField(max_length = 1000, blank = True)


#Profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500, blank = True)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}'
