from django.forms import ModelForm

from bbs import models

class ArticleModelForm(ModelForm):
    class Meta:
        model=models.Article
        #去除括号中的字段
        exclude=('author','pub_date','priority')
    # 初始化
    def __init__(self,*args,**kwargs):
        super(ArticleModelForm,self).__init__(*args,**kwargs)

        for field_name in self.base_fields:
            field=self.base_fields[field_name]
            field.widget.attrs.update({'class':'form-control'})