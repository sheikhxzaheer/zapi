# Generated by Django 5.1 on 2024-09-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadechatai', '0006_zuser_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
