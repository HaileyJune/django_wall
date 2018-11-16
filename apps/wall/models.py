from django.db import models
from apps.login_registration.models import Users
# Create your models here.

class Messages(models.Model):
    user_id = models.ForeignKey(Users, related_name="messages")
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user_id = models.ForeignKey(Users, related_name="comments")
    message_id = models.ForeignKey(Messages, related_name="comments")
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)