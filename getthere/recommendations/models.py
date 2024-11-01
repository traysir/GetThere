from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    CATEGORY_CHOICES = [
        ('game', 'Game'),
        ('movie', 'Movie'),
        ('sport', 'Sports Event'),
        ('travel', 'Travel Destination')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    liked = models.BooleanField(default=False)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.media_item.title} ({self.rating})"
