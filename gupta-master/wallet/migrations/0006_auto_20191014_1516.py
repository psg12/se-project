# Generated by Django 2.2.5 on 2019-10-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_balance_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
