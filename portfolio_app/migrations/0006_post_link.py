# Generated by Django 4.0.4 on 2022-07-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_tag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
