# Generated by Django 4.2.5 on 2023-09-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_alter_aqi_pm_alter_wqi_bod_alter_wqi_cond_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aqi",
            name="MONTH",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="wqi",
            name="MONTH",
            field=models.IntegerField(default=0),
        ),
    ]
