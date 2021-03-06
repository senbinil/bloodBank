# Generated by Django 4.0.2 on 2022-02-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='blood',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='district',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]
