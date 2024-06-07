# Generated by Django 5.0.6 on 2024-06-04 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_note_private_alter_note_author_userdata'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='can_edit',
            field=models.ManyToManyField(null=True, related_name='editable_notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='public_to',
            field=models.ManyToManyField(null=True, related_name='readable_notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]