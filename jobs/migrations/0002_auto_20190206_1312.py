# Generated by Django 2.1.3 on 2019-02-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='answer',
            field=models.CharField(default='please answer', max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='contact',
            field=models.IntegerField(),
        ),
    ]