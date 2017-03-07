from django.db import models

# Create your models here.
from django_countries.fields import CountryField


class Client(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=500, blank=True)
    postal_code = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, default='Villeurbanne')
    country = CountryField(default='FR')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    name = models.CharField(max_length=100)
    oauth_id = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_app_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # @pvienne : not >= 0 to plan refunds
    taxes = models.FloatField()
    description = models.TextField(blank=True)
    application = models.ForeignKey(
        to=Application,
        on_delete=models.SET_NULL,
        related_name='products',
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    transaction_id = models.CharField(max_length=200)  # @pvienne : required.
    amount = models.IntegerField()

    STARTED = 'ST'
    DRAFT = 'DR'
    IN_PROGRESS = 'IP'
    FAILED = 'FA'
    SUCCESS = 'SU'

    STATUS_CHOICES = (
        (STARTED, 'Démarré'),
        (DRAFT, 'Brouillon'),
        (IN_PROGRESS, 'En cours'),
        (FAILED, 'Échoué'),
        (SUCCESS, 'Réussi')
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,  # @pvienne what to do if client is deleted ?
        related_name='payments'
    )
    products = models.ManyToManyField(
        to=Product,
        related_name='payments'
    )
    application = models.ForeignKey(
        to=Application,
        related_name='payments'
    )

    TEST = 'TEST'
    MERCANET = 'MERC'
    STRIPE = 'STRP'
    PAYPAL = 'PP'
    MANUAL_CB = 'MCB'
    MANUAL_CHQ = 'MCHQ'
    MANUAL_ESP = 'MESP'
    MANUAL_VIR = 'MVIR'

    METHOD_CHOICES = (
        (TEST, 'Test'),
        (MERCANET, 'Mercanet'),
        (STRIPE, 'Stripe'),
        (PAYPAL, 'Paypal'),
        (MANUAL_CB, 'Carte bancaire'),
        (MANUAL_CHQ, 'Chèque'),
        (MANUAL_ESP, 'Espèces'),
        (MANUAL_VIR, 'Virement'),
    )
    method = models.CharField(max_length=4, choices=METHOD_CHOICES)  # @pvienne changed field name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaymentLog(models.Model):
    payment = models.ForeignKey(
        to=Payment,
        on_delete=models.CASCADE,  # @pvienne what to do if payment is deleted ?
        related_name='logs'
    )

    from_status = models.CharField(max_length=2, choices=Payment.STATUS_CHOICES)
    to_status = models.CharField(max_length=2, choices=Payment.STATUS_CHOICES)
    signature = models.TextField()

    method_data = models.TextField()  # @pvienne Not sure about type + changed name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApplicationRequest(models.Model):
    application = models.ForeignKey(
        to=Application,
        on_delete=models.CASCADE,  # @pvienne what to do if application is deleted ?
        related_name='requests'
    )
    endpoint = models.TextField()
    method = models.CharField(max_length=10)
    params = models.TextField(blank=True)  # @pvienne merged GET and POST params
    response = models.TextField(blank=True)  # @pvienne not sure about type

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
