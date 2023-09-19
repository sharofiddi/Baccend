# Generated by Django 4.2.5 on 2023-09-16 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='books/')),
                ('bio', models.TextField(null=True)),
                ('jenre', models.CharField(choices=[('Роман', 'Novel'), ('Фантастика', 'Fantasy'), ('Путешествие', 'Travel'), ('История', 'History'), ('Ужастик', 'Horror'), ('Детевтик', 'Detective')], max_length=20, null=True)),
                ('author', models.CharField(max_length=300)),
                ('date_of_release', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]