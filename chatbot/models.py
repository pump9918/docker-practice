# chatbot/models.py

from django.db import models

class Message(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
