from django.db import models

# Create your models here.
class Subfamily(models.Model):
    name = models.CharField('拉丁学名',max_length=255)
    chinese_name = models.CharField('中文名',max_length=255)
    create_time = models.DateTimeField('创建时间',auto_now_add = True)
    update_time = models.DateTimeField('更新时间',auto_now = True)

    def __str__(self):
        return f"{self.chinese_name}[{self.name}]"
    class Meta:
        verbose_name = '亚科(Subfamily)'       
        verbose_name_plural = verbose_name

class Genus(models.Model):
    subfamily = models.ForeignKey(Subfamily,on_delete=models.CASCADE,verbose_name='所属亚科')
    name = models.CharField('拉丁学名',max_length=255)
    chinese_name = models.CharField('中文名',max_length=255)
    create_time = models.DateTimeField('创建时间',auto_now_add = True)
    update_time = models.DateTimeField('更新时间',auto_now = True)

    def __str__(self):
        return f"{self.chinese_name}[{self.name}]"

    class Meta:
        verbose_name = '属(Genus)'
        verbose_name_plural = verbose_name

class BaseData(models.Model):
    chinese_name = models.CharField('中文学名',max_length=255)
    latin_name = models.CharField('拉丁学名',max_length=255)
    other_name = models.CharField('常用名称',max_length=255)
    genus = models.ForeignKey(Genus,on_delete=models.CASCADE)
    distribution = models.CharField('分布',max_length=255)
    habitat = models.CharField('栖息地',max_length=255)
    colony_form = models.CharField('群落形式',max_length=255)
    queen_size = models.CharField('蚁后尺寸',max_length=255)
    queen_color = models.CharField('蚁后颜色',max_length=255)
    worker_size = models.CharField('工蚁尺寸',max_length=255)
    worker_color = models.CharField('工蚁颜色',max_length=255)
    soldier_size = models.CharField('兵蚁尺寸',max_length=255)
    soldier_color = models.CharField('兵蚁颜色',max_length=255)
    males_size = models.CharField('雄蚁尺寸',max_length=255)
    males_color = models.CharField('雄蚁颜色',max_length=255)
    nutrition = models.CharField('饲养食物',max_length=255)
    arena_humidity = models.CharField('活动区湿度',max_length=255)
    nest_humidity = models.CharField('巢湿度',max_length=255)
    arena_temperature = models.CharField('活动区温度',max_length=255)
    nest_temperature = models.CharField('巢温度',max_length=255)
    hibernation = models.CharField('冬眠',max_length=255)
    camp_form = models.CharField('野外营巢',max_length=255)
    nest_form = models.CharField('巢形式',max_length=255)
    nest_size = models.CharField('巢尺寸',max_length=255)    
    nest_substrate = models.CharField('巢基底',max_length=255)
    arena_substrate = models.CharField('活动区基底',max_length=255)
    planting = models.CharField('活动区种植',max_length=255)
    decoration = models.CharField('活动区装饰',max_length=255)
    description = models.CharField('描述',max_length=255)
    colony_size = models.CharField('群落规模',max_length=255)
    mating_flight = models.CharField('婚飞',max_length=255)
    founding = models.CharField('发育',max_length=255)
    antmap = models.URLField('蚂蚁地图')
    antwiki = models.URLField('蚂蚁维基')
    antstore = models.URLField('蚂蚁商店')
    create_time = models.DateTimeField('创建时间',auto_now_add = True)
    update_time = models.DateTimeField('更新时间',auto_now = True)
    class Meta:
        verbose_name = '蚂蚁信息'
        verbose_name_plural = verbose_name