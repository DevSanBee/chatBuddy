# Generated by Django 4.2.1 on 2023-06-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_remove_message_savemsg_remove_message_unlikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
