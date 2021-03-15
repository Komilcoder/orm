from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User

# user testing
class BlogPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create user
        testuser1 = User.objects.create_user(username='tester',password='orm2020')
        testuser1.save()

        # create post 
        testpost = Post.objects.create(author=testuser1, title='post title',status='post status')
        testpost.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        status = f'{post.status}'
        self.assertEquals(author,'tester')
        self.assertEquals(title,'post title')
        self.assertEquals(status,'post status')




class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='first title',status='status time',publish='published')

    def post_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name,'first title') 

    def post_status_content(self):
        status = Post.objects.get(id=1)
        expected_object_name = f'{status.status}'
        self.assertEquals(expected_object_name,'status time')

    def post_publish_content(self):
        publish = Post.objects.get(id=1)
        expected_object_name = f'{publish.publish}'
        self.assertEquals(expected_object_name,'published')


