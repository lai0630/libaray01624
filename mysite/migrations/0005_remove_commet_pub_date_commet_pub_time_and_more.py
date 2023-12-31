# Generated by Django 4.2.5 on 2023-12-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_mood_commet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commet',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='commet',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='commet',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='commet',
            name='nickname',
            field=models.CharField(default='不願意透漏身份的人', max_length=10),
        ),
    ]