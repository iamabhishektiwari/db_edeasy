# Generated by Django 3.0.8 on 2020-07-20 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_db', '0006_mcq_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MCQ_Question',
            new_name='McqQuestion',
        ),
    ]