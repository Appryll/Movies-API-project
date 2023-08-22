from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    vote_average = models.FloatField(default=0.0)
    vote_count = models.PositiveBigIntegerField()
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
