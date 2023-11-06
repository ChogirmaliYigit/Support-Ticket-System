import uuid

from django.db import models


class Chat(models.Model):
    subject = models.CharField(max_length=300)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company = models.ForeignKey("users.Company", models.CASCADE, "company_chats")
    user = models.ForeignKey("users.User", models.CASCADE, "user_chats")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = "chats"


class Message(models.Model):
    user = models.ForeignKey("users.User", models.CASCADE, "user_messages")
    chat = models.ForeignKey(Chat, models.CASCADE, "chat_messages")
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="message_photos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "messages"
