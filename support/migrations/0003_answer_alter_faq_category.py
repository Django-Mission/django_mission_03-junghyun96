# Generated by Django 4.0.4 on 2022-05-10 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_delete_answer_inquiry_category_inquiry_create_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[(1, '상품 문의'), (2, '교환&환불 문의'), (3, '배송 문의')], default=1, max_length=10, verbose_name='카테고리'),
        ),
    ]