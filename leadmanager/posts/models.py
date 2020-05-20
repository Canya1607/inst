from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# one to many(no repost)
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # CASCADE = if user is deleted -> delete post;


    def __str__(self):
        return self.title












# feature checkout 
# python manage.py shell
#>> from posts.models import Post
#>> from django.contrib.auth.models import User
#>> user1 = User.objects.get(username = 'user1')
#>> post_1 = Post(title='Post One', content='Henlo Wrld :) ', author = user1)
#>> post_2.save()
#>> Post.objects.all() 
#<QuerySet [<Post: Post one>]>

#>> post = Post.objects.first()
#>> post.content
# 'Henlo Wrld :)'

#>> post.author
# <User: user1>

#>> post.author.email
# 'user1@gmail.com'

# GET ALL POST FROM SPECIFIC USER(user1)
#>> user1.post_set
#>> user1.post_set.all()

# NOW CREATE A NEW POST WITH CURRENT USER(user1)
#>> user1.post_set.create(title='Post three', content= 'Now w h threesome')
