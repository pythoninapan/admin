from django.db import models

# Create your models here.
class Article(models.Model):


    title = models.CharField(max_length=20)
    desription = models.TextField()
    slug = models.SlugField(max_length=25)

    def get_absolute_url(self):
        return reverse('blog', kwargs={'post_slug': self.slug})

