# Generated by Django 4.1 on 2022-08-07 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subfamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('chinese_name', models.CharField(max_length=255, verbose_name='中文名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '亚科',
                'verbose_name_plural': '亚科',
            },
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('chinese_name', models.CharField(max_length=255, verbose_name='中文名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('subfamily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ant.subfamily')),
            ],
            options={
                'verbose_name': '属',
                'verbose_name_plural': '属',
            },
        ),
        migrations.CreateModel(
            name='BaseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=255, verbose_name='中文学名')),
                ('latin_name', models.CharField(max_length=255, verbose_name='拉丁学名')),
                ('other_name', models.CharField(max_length=255, verbose_name='常用名称')),
                ('distribution', models.CharField(max_length=255, verbose_name='分布')),
                ('habitat', models.CharField(max_length=255, verbose_name='栖息地')),
                ('colony_form', models.CharField(max_length=255, verbose_name='群落形式')),
                ('queen_size', models.CharField(max_length=255, verbose_name='蚁后尺寸')),
                ('queen_color', models.CharField(max_length=255, verbose_name='蚁后颜色')),
                ('worker_size', models.CharField(max_length=255, verbose_name='工蚁尺寸')),
                ('worker_color', models.CharField(max_length=255, verbose_name='工蚁颜色')),
                ('soldier_size', models.CharField(max_length=255, verbose_name='兵蚁尺寸')),
                ('soldier_color', models.CharField(max_length=255, verbose_name='兵蚁颜色')),
                ('males_size', models.CharField(max_length=255, verbose_name='雄蚁尺寸')),
                ('males_color', models.CharField(max_length=255, verbose_name='雄蚁颜色')),
                ('nutrition', models.CharField(max_length=255, verbose_name='饲养食物')),
                ('arena_humidity', models.CharField(max_length=255, verbose_name='活动区湿度')),
                ('nest_humidity', models.CharField(max_length=255, verbose_name='巢湿度')),
                ('arena_temperature', models.CharField(max_length=255, verbose_name='活动区温度')),
                ('nest_temperature', models.CharField(max_length=255, verbose_name='巢温度')),
                ('hibernation', models.CharField(max_length=255, verbose_name='冬眠')),
                ('camp_form', models.CharField(max_length=255, verbose_name='野外营巢')),
                ('nest_form', models.CharField(max_length=255, verbose_name='巢形式')),
                ('nest_size', models.CharField(max_length=255, verbose_name='巢尺寸')),
                ('nest_substrate', models.CharField(max_length=255, verbose_name='巢基底')),
                ('arena_substrate', models.CharField(max_length=255, verbose_name='活动区基底')),
                ('planting', models.CharField(max_length=255, verbose_name='活动区种植')),
                ('decoration', models.CharField(max_length=255, verbose_name='活动区装饰')),
                ('description', models.CharField(max_length=255, verbose_name='描述')),
                ('colony_size', models.CharField(max_length=255, verbose_name='群落规模')),
                ('mating_flight', models.CharField(max_length=255, verbose_name='婚飞')),
                ('founding', models.CharField(max_length=255, verbose_name='发育')),
                ('antmap', models.URLField(verbose_name='蚂蚁地图')),
                ('antwiki', models.URLField(verbose_name='蚂蚁维基')),
                ('antstore', models.URLField(verbose_name='蚂蚁商店')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ant.genus')),
            ],
            options={
                'verbose_name': '蚂蚁信息',
                'verbose_name_plural': '蚂蚁信息',
            },
        ),
    ]
