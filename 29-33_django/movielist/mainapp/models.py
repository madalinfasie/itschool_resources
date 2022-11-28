from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f'Movie(title="{self.title}", release_date={self.release_date})'
