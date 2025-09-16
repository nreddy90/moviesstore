from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    favorited_by = models.ManyToManyField(User, related_name='favorite_movies', blank=True)
    def __str__(self):
        return str(self.id) + ' - ' + self.name
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count=models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="review_likes", blank=True)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
    def total_likes(self):
        return self.likes.count()