# Generated by Django 4.2 on 2023-06-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('likes', models.IntegerField()),
                ('category', models.CharField(max_length=250)),
                ('difficulty', models.CharField(max_length=250)),
                ('has_solution', models.BooleanField()),
                ('tag', models.ManyToManyField(related_name='problems', to='problem.topictag')),
            ],
        ),
    ]
