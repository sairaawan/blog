# Generated by Django 3.0.5 on 2020-07-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200714_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='categories',
            field=models.ManyToManyField(to='post.Category'),
        ),
    ]
