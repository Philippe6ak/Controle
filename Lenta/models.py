from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.username)


class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=500)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)


