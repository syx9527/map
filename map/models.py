from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField("类别名称", max_length=255, null=False, blank=False)

    # name = models.CharField("类别名称", max_length=255, )

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(verbose_name="位置", max_length=255, null=False)

    class Meta:
        verbose_name = '位置_Location'
        verbose_name_plural = verbose_name
    

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(verbose_name="地点名称", max_length=255, null=False)
    location = models.ForeignKey(to="Location", on_delete=models.CASCADE, null=True, verbose_name="位置", blank=True)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, null=True, verbose_name="类别", blank=True)

    class Meta:
        verbose_name = '地点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
