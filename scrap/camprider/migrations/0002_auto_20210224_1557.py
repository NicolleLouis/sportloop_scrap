# Generated by Django 3.1.7 on 2021-02-24 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camprider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='url',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.TextField()),
                ('price', models.FloatField()),
                ('postal_code', models.IntegerField()),
                ('seller', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='camprider.seller', verbose_name='seller')),
            ],
        ),
    ]
