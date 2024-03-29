# Generated by Django 4.0.2 on 2022-02-28 10:14

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nanglerng', '0004_alter_essay_rawhtmldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rawHtmlData', django_quill.fields.QuillField()),
                ('author', models.CharField(max_length=200)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('eventTime', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('desc', models.TextField()),
                ('rawHtmlData', django_quill.fields.QuillField()),
                ('culture', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('contribute', models.CharField(max_length=200)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nanglerng.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/%Y/%m/%d/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nanglerng.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='typePost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nanglerng.typepost'),
        ),
    ]
