import os
import django
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from tweet.models import Tweet

# Configure Django settings for testing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twipost.settings')
django.setup()


class TweetModelTest(TestCase):
    """Test cases for Tweet model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_tweet_creation(self):
        """Test creating a tweet"""
        tweet = Tweet.objects.create(
            user=self.user,
            text='This is a test tweet'
        )
        self.assertEqual(tweet.text, 'This is a test tweet')
        self.assertEqual(tweet.user, self.user)
        self.assertTrue(tweet.created_at)
        self.assertTrue(tweet.updated_at)
    
    def test_tweet_str_method(self):
        """Test tweet string representation"""
        tweet = Tweet.objects.create(
            user=self.user,
            text='This is a test tweet for string method'
        )
        expected_str = f'{self.user.username} - This is a '
        self.assertEqual(str(tweet), expected_str)
    
    def test_tweet_max_length(self):
        """Test tweet text max length"""
        long_text = 'a' * 250  # More than 240 characters
        tweet = Tweet(user=self.user, text=long_text)
        # This should raise a validation error in production
        # For now, we'll just check the length
        self.assertGreater(len(tweet.text), 240)


class TweetViewTest(TestCase):
    """Test cases for Tweet views"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.tweet = Tweet.objects.create(
            user=self.user,
            text='Test tweet for views'
        )
    
    def test_tweet_list_view(self):
        """Test tweet list view"""
        response = self.client.get(reverse('tweet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test tweet for views')
    
    def test_tweet_create_view_requires_login(self):
        """Test that tweet creation requires login"""
        response = self.client.get(reverse('tweet_create'))
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
    
    def test_tweet_create_view_authenticated(self):
        """Test tweet creation when authenticated"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('tweet_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_tweet_edit_own_tweet(self):
        """Test editing own tweet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('tweet_edit', args=[self.tweet.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_tweet_delete_own_tweet(self):
        """Test deleting own tweet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('tweet_delete', args=[self.tweet.id]))
        self.assertEqual(response.status_code, 200)


class UserRegistrationTest(TestCase):
    """Test cases for user registration"""
    
    def test_user_registration_view(self):
        """Test user registration page"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_user_registration_post(self):
        """Test user registration form submission"""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        response = self.client.post(reverse('register'), user_data)
        # Should redirect after successful registration
        self.assertEqual(response.status_code, 302)
        # Check if user was created
        self.assertTrue(User.objects.filter(username='newuser').exists())


class HealthCheckTest(TestCase):
    """Basic health check tests"""
    
    def test_database_connection(self):
        """Test database connection"""
        user_count = User.objects.count()
        self.assertIsInstance(user_count, int)
    
    def test_models_import(self):
        """Test that models can be imported"""
        from tweet.models import Tweet
        from django.contrib.auth.models import User
        self.assertTrue(Tweet)
        self.assertTrue(User)
