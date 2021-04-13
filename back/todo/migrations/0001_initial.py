# Generated by Django 3.2 on 2021-04-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='TODO 제목입니다.', max_length=64, verbose_name='TODO 제목')),
                ('description', models.CharField(blank=True, help_text='TODO 설명입니다.', max_length=256, null=True, verbose_name='TODO 설명')),
                ('author', models.CharField(help_text='TODO 작성자를 나타냅니다.', max_length=16, verbose_name='TODO 작성자')),
                ('due_date', models.DateTimeField(help_text='TODO 마감일을 나타냅니다.', verbose_name='TODO 마감일')),
                ('completed', models.BooleanField(default=False, help_text='TODO 완료 여부를 나타냅니다.', verbose_name='TODO 완료 여부')),
            ],
            options={
                'verbose_name': 'TODO 리스트',
                'verbose_name_plural': 'TODO 리스트(들)',
            },
        ),
    ]
