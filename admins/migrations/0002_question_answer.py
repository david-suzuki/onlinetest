# Generated by Django 4.0 on 2021-12-20 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('qlevel', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=100)),
                ('answer_type', models.CharField(choices=[('single', 'Single'), ('multiple', 'Multiple')], default='single', max_length=100)),
                ('explanation', models.TextField(default='')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('correct_type', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.question')),
            ],
        ),
    ]