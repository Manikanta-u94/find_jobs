# Generated by Django 2.1.3 on 2019-02-06 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190206_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.S_Question'),
        ),
    ]
