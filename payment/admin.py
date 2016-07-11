from django.contrib import admin

from payment.models import *
from payment.admin_actions import process_payments


class SubscriptionPaymentInline(admin.TabularInline):
    model = SubscriptionPayment
    extra = 0


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'state', 'type', 'name', 'date', 'address', 'transaction_id', 'iban', 'bic', 'amount',
                    'amount_to_reimburse',
                    'currency_code', 'remittance_user_string', 'filename']
    list_filter = ['state', 'type', 'date']
    search_fields = ['id', 'name', 'address', 'transaction_id', 'iban', 'bic', 'amount',
                     'currency_code', 'remittance_user_string', 'filename']
    inlines = [SubscriptionPaymentInline]
    actions = [process_payments]


@admin.register(SubscriptionPayment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment', 'subscription', 'amount']
    raw_id_fields = ['payment', 'subscription']
    search_fields = ['id', 'payment', 'subscription', 'amount']

