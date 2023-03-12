from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=55, verbose_name='Название товара')
    version = models.CharField(max_length=55, null=True, verbose_name='Модель товара')
    release_date = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Дата выпуска')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    email = models.EmailField(unique=True, null=True, verbose_name='Почта')
    country = models.CharField(max_length=55, null=True, verbose_name='Страна')
    city = models.CharField(max_length=55, null=True, verbose_name='Город')
    street = models.CharField(max_length=55, null=True, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class BusinessUnit(models.Model):
    FACTORY = 'F'
    RETAIL_NETWORK = 'R'
    ENTREPRENEUR = 'E'
    COMPANY_TYPES = [
        (FACTORY, 'Завод'),
        (RETAIL_NETWORK, 'Розничная сеть'),
        (ENTREPRENEUR, 'Предприниматель'),
    ]
    title = models.CharField(max_length=55, verbose_name='Название компании')
    company_type = models.CharField(max_length=1, choices=COMPANY_TYPES, default=FACTORY, verbose_name='Тип компании')
    provider = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Поставщик',
    )

    class Meta:
        verbose_name = 'BusinessUnit'
        verbose_name_plural = 'BusinessUnit'

    def __str__(self):
        return self.title


class BaseModel(models.Model):
    company = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product)
    contacts = models.ForeignKey(Contact, on_delete=models.PROTECT)
    created_date = models.DateField(auto_now_add=True)
    duty = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        verbose_name='Задолженность поставщику',
        blank=True
    )

    class Meta:
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModel'

    def __str__(self):
        return f'{self.company.title} - {self.company.company_type}'
