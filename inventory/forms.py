from django import forms
from .models import product_type,inventory,supplier,add_inventory
from django.template.defaultfilters import mark_safe
from django.utils.translation import ugettext_lazy as _


class ProductTypeForm(forms.ModelForm):

    class Meta:
        model = product_type
        fields = ('name','note1','note2')
        labels = {
            'name': _('Ապրանքատեսակ'),
            'note1': _('Լրացուցիչ նշում 1'),
            'note2': _('Լրացուցիչ նշում 2'),

        }
        help_texts = {
            'name': _('Այստեղ նշվում է ընդահանուր խումբ, օրինակ՝ ներկ'),
        }



class InventoryForm(forms.ModelForm):

    class Meta:
        model = inventory
        fields = (
            'inventory_type',
            'model',
            'conversion_rate',
            'measure',
            'note1',
            'note2',
        )
        labels = {
            'inventory_type': _('Ապրանքատեսակ'),
            'model': _('Ապրանքի մոդել'),
            'conversion_rate': _('Խտություն/ ԿԳ-ի Փոխակերպման գործակից'),
            'measure': _('Չափման միավոր'),
            'note1': _('Լրացուցիչ նշում 1'),
            'note2': _('Լրացուցիչ նշում 2'),

        }
        help_texts = {
            'conversion_rate': _('Այստեղ նշվում է գորշակցի արժեքը, որով տվյալ ներկի լիտրը վերածվում է ԿԳ-ի: Այլ ապրանքների դեպքում մուտքագրել անհրաժեշտ չէ:'),
        }

class SupplierForm(forms.ModelForm):

    class Meta:
        model = supplier
        fields = (
            'name',
            'contact_name',
            'address',
            'phone',
            'bank_account',
            'note1',
            'note2',
        )


        labels = {
            'name': _('Ընկերության անվանում'),
            'contact_name': _('Կոնտակտային անձ'),
            'address': _('Հասցե'),
            'phone': _('Հեռախոսահամար'),
            'bank_account': _('Բանկային ռեկվիզիտներ'),
            'note1': _('Լրացուցիչ նշում 1'),
            'note2': _('Լրացուցիչ նշում 2'),

        }


class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = add_inventory
        fields = (
            'date',
            'supplier',
            'product_type',
            'quantity',
            'price',
            'note1',
            'note2',
            'note3',
        )

        labels = {
            'date': _('Ամսաթիվ'),
            'supplier': _('Մատակարար'),
            'product_type': _('Ապրանքի մոդել'),
            'quantity': _('Քանակ'),
            'price': _('Գին'),
            'note1': _('Լրացուցիչ նշում 1'),
            'note2': _('Լրացուցիչ նշում 2'),
            'note3': _('Լրացուցիչ նշում 3'),

        }
