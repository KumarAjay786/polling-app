# Generated by Django 5.0.3 on 2024-03-15 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=1000)),
                ('votes', models.IntegerField(default=0)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollapp.questions')),
            ],
        ),
    ]