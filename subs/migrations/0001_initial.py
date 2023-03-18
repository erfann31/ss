# Generated by Django 4.1.7 on 2023-03-17 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CROwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('past_period', models.IntegerField(default=0)),
                ('remaining_period', models.IntegerField(default=0, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subs.crowner')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subs.store')),
            ],
        ),
    ]