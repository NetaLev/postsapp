from django.db import models

class Category(models.Model):
    value = models.CharField(max_length=50)
    # === toString
    def __str__(self):
        return self.value

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.TextField()

    # def create(self):
    #     self.save()

    # === toString
    def __str__(self):
        return self.value
