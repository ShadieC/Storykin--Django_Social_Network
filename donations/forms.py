from django import forms
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


class DonationForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    recurring = forms.BooleanField(required=False)

    def get_paypal_form(self, request):
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': self.cleaned_data['amount'],
            'item_name': 'Donation',
            'invoice': str(uuid.uuid4()),
            'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': request.build_absolute_uri(reverse('donation_success')),
            'cancel_return': request.build_absolute_uri(reverse('donation_cancel')),
        }
        if self.cleaned_data['recurring']:
            paypal_dict['cmd'] = '_xclick-subscriptions'
            paypal_dict['a3'] = self.cleaned_data['amount']
            paypal_dict['p3'] = 1
            paypal_dict['t3'] = self.cleaned_data['frequency']
            paypal_dict['src'] = 1
            paypal_dict['sra'] = 1
        else:
            paypal_dict['cmd'] = '_donations'
        return PayPalPaymentsForm(initial=paypal_dict)


class StripeDonationForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    is_monthly = forms.BooleanField(required=False)
    stripe_token = forms.CharField(widget=forms.HiddenInput())