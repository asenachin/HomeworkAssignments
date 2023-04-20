# Generated by Django 3.2.15 on 2023-04-15 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_info', models.JSONField()),
                ('amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('paid', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('telegram_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, null=True)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_address', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=16)),
                ('usd_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('pay_amount', models.DecimalField(decimal_places=8, max_digits=16)),
                ('paid', models.BooleanField(default=False)),
                ('payment_id', models.BigIntegerField(null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.user')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.user'),
        ),
    ]