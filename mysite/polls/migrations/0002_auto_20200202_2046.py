# Generated by Django 3.0.2 on 2020-02-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_Date',
            new_name='pub_date',
        ),
    ]