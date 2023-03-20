from django.db import models
from django.urls import reverse
from slugify import slugify
class group(models.Model):
    
    name=models.CharField('新名字',max_length=10,unique=True)

    notice=models.TextField('新通知',null=True,blank=True)

    date=models.DateField('发布日期',null=True, blank=True,auto_now=True)#default=time.strftime('%Y-%m-%d',time.localtime())

    slug=models.SlugField(null=True,blank=True)
    def get_absolute_url(self):
    #返回带id的url
        return reverse('catalog:group_detail', args=[str(self.slug)])
    def __str__(self):
        
        return self.name
    
    def get_update_url(self):
        return reverse('catalog:update', args=[str(self.slug)])
    class Meta:
        
        permissions = (("can_notice", "notice"),)#权限设置
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)
         