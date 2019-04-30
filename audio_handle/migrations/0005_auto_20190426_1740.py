# Generated by Django 2.2 on 2019-04-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_handle', '0004_audio_success'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='success',
        ),
        migrations.AddField(
            model_name='audio',
            name='task_id',
            field=models.CharField(default='asdf', max_length=64),
            preserve_default=False,
        ),
    ]