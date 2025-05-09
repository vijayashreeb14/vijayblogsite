# Generated by Django 5.2 on 2025-04-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(blank=True, default='20 April 2025', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(blank=True, default='20 April 2025', max_length=100),
        ),
    ]
