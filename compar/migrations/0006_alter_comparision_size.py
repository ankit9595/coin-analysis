# Generated by Django 4.2.20 on 2025-04-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compar', '0005_alter_comparision_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparision',
            name='size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
