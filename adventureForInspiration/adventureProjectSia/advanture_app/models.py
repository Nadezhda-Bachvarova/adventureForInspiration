from django.db import models

from adventureProjectSia.accounts.models import UserProfile


class Article(models.Model):
    title = models.CharField(max_length=50)
    destination = models.CharField(max_length=30)
    content = models.TextField()
    hashtag = models.CharField(max_length=20, default='')
    image = models.ImageField(
        blank=False,
        upload_to='articles',
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Test(models.Model):
    test = models.BooleanField(default=True)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(blank=False)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class NewsAndEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    time = models.TimeField()
    description = models.TextField(blank=False)
    image = models.ImageField(
        blank=False,
        upload_to='events',
    )


