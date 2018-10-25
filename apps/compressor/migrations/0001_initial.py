# Generated by Django 2.1.2 on 2018-10-25 17:54

import apps.compressor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HyperlinkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('original', models.CharField(max_length=254)),
                ('internal', models.CharField(default=apps.compressor.models.generate_internal_id, editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'hyperlink',
                'verbose_name_plural': 'hyperlinks',
                'db_table': 'hyperlink',
            },
        ),
    ]