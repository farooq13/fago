# Generated by Django 5.1 on 2024-08-22 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_remove_community_banner'),
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='community',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='communities.community'),
        ),
    ]
