# Generated by Django 5.0.3 on 2024-09-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_alter_role_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='module_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
