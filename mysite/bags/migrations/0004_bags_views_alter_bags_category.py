# Generated by Django 4.2.4 on 2023-09-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0003_category_bags_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bags',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bags',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bags.category', verbose_name='Категорія'),
        ),
    ]
