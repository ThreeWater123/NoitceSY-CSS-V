# Generated by Django 4.1.7 on 2023-03-20 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_group_slug_alter_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='新名字'),
        ),
    ]
