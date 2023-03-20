# Generated by Django 4.1.7 on 2023-03-18 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0013_alter_subscription_extension'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='extension',
        ),
        migrations.AddField(
            model_name='subscription',
            name='last_extension',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='period',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subs.store'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
