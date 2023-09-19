from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Device(models.Model):
    class Types(models.TextChoices):
        Novel = 'Роман', 'Novel'
        Fantasy = 'Фантастика', 'Fantasy'
        Travel = 'Путешествие', 'Travel'
        History = 'История', 'History'
        Horror = 'Ужастик', 'Horror'
        Detective = 'Детевтик', 'Detective'
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books/')
    bio = models.TextField(null=True)
    jenre = models.CharField(max_length=20, choices=Types.choices, null=True)
    author = models.CharField(max_length=300)
    date_of_release = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse(
            'detail',
            args=[
                self.slug,
                self.date_of_release,
                self.author
            ]
        )