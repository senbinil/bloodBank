# Generated by Django 4.0.2 on 2022-02-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbankrequest',
            name='dateLog',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]