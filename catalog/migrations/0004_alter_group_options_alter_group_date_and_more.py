# Generated by Django 4.1.7 on 2023-03-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_group_notice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'permissions': (('test', 'test message'),)},
        ),
        migrations.AlterField(
            model_name='group',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='group',
            name='notice',
            field=models.TextField(blank=True, null=True, verbose_name='新通知'),
        ),
    ]