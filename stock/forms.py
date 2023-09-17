from django import forms

class Add_inventory_form (forms.Form):
    name=forms.CharField(max_length=255)
    model = forms.CharField(max_length=255, required=False, strip=True)
    description=forms.CharField(max_length=555,required=False, strip=True)
    sale_price = forms.DecimalField(decimal_places=2, max_value=7, required=False)
    cost_price = forms.DecimalField(decimal_places=2, max_value=7, required=False)
    quantity = forms.IntegerField()
    category = forms.IntegerField(required=True)
    shelve = forms.IntegerField(required=True)
