from django import forms
from .models import *

from ckeditor.widgets import CKEditorWidget


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Название набора',
        max_length=255,
    )
    season = forms.ModelChoiceField(queryset=CategorySeason.objects.all())
    size = forms.ModelChoiceField(queryset=CategorySize.objects.all())
    text = forms.CharField(
        label='Описание товара (Наряда / костюма)',
        widget=CKEditorWidget(
            attrs={
                'class': 'product_form_text',
                'id': 'product_form_text_label'
            }
        )
    )

    link = forms.URLField(
        label='Ссылки на товары из набора',
        help_text='Введите ссылки для вашего лука',
    )

    price = forms.IntegerField(label='Цена набора')
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ('title', 'season', 'size', 'text', 'link', 'price', 'image')
