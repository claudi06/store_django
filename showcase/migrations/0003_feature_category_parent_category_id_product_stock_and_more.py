# Generated by Django 4.1.3 on 2022-12-01 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_alter_product_brand_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=300, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.feature')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.product')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.category'),
        ),
    ]
