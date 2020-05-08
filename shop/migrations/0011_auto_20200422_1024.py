# Generated by Django 3.0.5 on 2020-04-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_productcategory_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=0, max_digits=2)),
                ('sizesInStock', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='shop.ProductSize'),
        ),
    ]