# Generated by Django 3.2.4 on 2021-07-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseMaterials', '0003_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='semID',
            field=models.IntegerField(blank=True, default=0, max_length=3, verbose_name='Semester ID'),
            preserve_default=False,
        ),
    ]
