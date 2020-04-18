from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Title")
    content = models.TextField(verbose_name= "Content")

    ##clase anidada para dar nombre al modelo
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    

    def __str__(self):
        return self.title
