from django.db import models

# Create your models here.

class Image(models.Model):
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=128, unique=True)
    pub_date = models.DateTimeField('Pubished at')

    def __str__(self):
        return f"{self.id}: {self.title[:30]}"

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(blank=False)

    def __str__(self):
        return f"{self.id}: ({self.image.title[:15]}) {self.text[:30]}"