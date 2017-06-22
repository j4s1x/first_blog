from django.db import models

class Posts(models.Model):
    '''blog entry title-first column of the database'''
    title = models.CharField(max_length=400)    #blog article title
    text = models.TextField()                   #blog article content
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return representation of model'''
        return self.title + self.text

class Comments(models.Model):
    post = models.ForeignKey(Posts, null=True)
    name = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + self.text
