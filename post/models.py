from django.db import models

# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    content_text = models.TextField()
    is_active = models.Boolean(default=True)

    def __str__(self):
        return 'Post: {}'.format(self.title_text)
        return 'Date Created: {}'.format(self.date_created)
        return 'Date Updated: {}'.format(self.date_updated)
        return 'Content: {}'.format(self.content_text)


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    content_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    #def __str__(self):
    #    return'Choice: {}'.format(self.choice_text)
