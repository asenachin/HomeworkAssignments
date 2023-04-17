# Generated by Django 4.1 on 2023-04-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'paidcontent',
            },
        ),
    ]
