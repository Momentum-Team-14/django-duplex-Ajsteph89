# Generated by Django 4.1 on 2022-08-31 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_remove_flashcard_user_alter_subject_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='user_subject',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, related_name='flashcard_user', to='flashcards.subject'),
            preserve_default=b'I01\n',
        ),
    ]
