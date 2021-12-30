from django.db import models


class BasePage(models.Model):
    created_time = models.DateTimeField('created time', auto_now_add=True)
    last_mod_time = models.DateTimeField('modified time', auto_now=True)
    
    class Meta:
        abstract = True


class Page(BasePage):
    title = models.CharField(max_length=200, null=True, blank=True)
    order = models.PositiveIntegerField("page order", default=1)
    
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = verbose_name
        db_table = 'page'
        

class Component(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=1000, null=True, blank=True)
    body = models.TextField(default='')
    
    order = models.PositiveIntegerField("component order", default=1)
    type = models.CharField(max_length=100, null=True, blank=True)
    sub_type = models.CharField(max_length=100, null=True, blank=True)
    
    bg_color_code = models.CharField(max_length=50, null=True, blank=True)
    
    page = models.ForeignKey(
        Page, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name='component')
    
    def __str__(self):
        try:
            return self.title
        except:
            return ''
    

class Banner(Component):
    class Meta:
        db_table = 'banner'


class Gallery(Component):
    class Meta:
        db_table = 'gallery'


class CompanyRecord(Component):
    class Meta:
        db_table = 'companyrecord'


class CompanyDo(models.Model):
    year = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=32, null=True, blank=True)
    company_record = models.ForeignKey(
        CompanyRecord, 
        on_delete=models.CASCADE, 
        related_name='companydo')
    
    class Meta:
        ordering = ['-year']
        db_table = 'companydo'


class PageImage(models.Model):
    alt = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=256)
    order = models.PositiveIntegerField("image order", default=1)
    created_time = models.DateTimeField('created time', auto_now_add=True)

    component = models.ForeignKey(
        Component, 
        on_delete=models.CASCADE, 
        related_name='pageimage')
    
    def __str__(self):
        return self.image_url
    
    class Meta:
        db_table = 'pageimages'
        