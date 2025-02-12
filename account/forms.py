from django import forms

from .models import Shipment, LiveUpdate


class DateInput(forms.DateInput):
	input_type = 'date'


class ShipmentCreateForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = '__all__'
        exclude = ['date_created']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget = forms.Textarea(attrs={'rows':1, 'cols':15})
        self.fields['shipping_date'].widget = DateInput()
        self.fields['delivery_date'].widget = DateInput()

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class LiveUpdateCreateForm(forms.ModelForm):

    class Meta:
        model = LiveUpdate
        fields = '__all__'
        exclude = ['created_on', 'shipment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['content'].widget = forms.Textarea(attrs={'rows':1, 'cols':15})
        # self.fields['shipping_date'].widget = DateInput()
        # self.fields['delivery_date'].widget = DateInput()

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})