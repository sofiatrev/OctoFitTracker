import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User
from bson import ObjectId

# Test saving a user directly using Django ORM
user = User(_id=ObjectId(), username='testuser', email='testuser@example.com', password='testpassword')
user.save()

# Retrieve and print the saved user
retrieved_user = User.objects.filter(username='testuser').first()
print("Retrieved user:", retrieved_user)