from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()


    def __str__(self):

        return self.title

    def pub_date_beaury(self):

        return self.pub_date.strftime('%b %d %Y')

    def shorten_body(self):

        return self.body[0:20]