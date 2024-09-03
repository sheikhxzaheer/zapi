from django.db import models


class ZUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    access_token = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.email

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=20, default='')
    chat_description = models.CharField(max_length=500, default='') 
    chat_url = models.CharField(max_length=500, default='') 
    
    def __str__(self):
        return self.chat_name
    

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(ZUser, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField(max_length=50, null=False, default='')

    def __str__(self):
        return self.message