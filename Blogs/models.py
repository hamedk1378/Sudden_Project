from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta



class BaseContent(models.Model):
    #
    body = models.TextField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def is_recently_published(self):
        return self.pub_date >= timezone.now() - timedelta(days = 3)


class Idea(BaseContent):
    #any Idea that user wish to share with others
    topic = models.CharField(max_length=256)

    def __str__(self):
        return str(self.user.username + f" 's Idea: {self.topic}")


class Comment(BaseContent):
    #People's comment on a Idea
    idea = models.ForeignKey(Idea, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user.username + f" 's comment on: {self.idea.topic}")



