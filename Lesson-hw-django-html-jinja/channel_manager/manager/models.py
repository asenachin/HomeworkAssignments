from django.db import models

# Create your models here.

class User(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    # вывод в терминале telegram_id
    def __str__(self):
        return f'User: {self.telegram_id}'

# def __str__(self) чтобы использовать метод строки
# user = User(telegram_id=123456789, username='username', full_name='full_name')
# print(user)

class Order(models.Model):
    order_info = models.JSONField()
    amount = models.DecimalField(max_digits=16, decimal_places=4)
    paid = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

    # вывод в терминале для id
    # def __str__(self):
    #     return f'Order: {self.id}. User: {self.user.telegram_id}'

class Transaction(models.Model):
    pay_address = models.CharField(max_length=255)
    currency = models.CharField(max_length=16)
    usd_amount = models.DecimalField(max_digits=16, decimal_places=4)
    pay_amount = models.DecimalField(max_digits=16, decimal_places=8)
    paid = models.BooleanField(default=False)
    payment_id = models.BigIntegerField(null=True)
    comment = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'transactions'

class PaidContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'paidcontent'

    # paid_content_id = models.IntegerField(primary_key=True)
    # url = models.CharField(max_length=255)
    # price = models.FloatField(null=True, blank=True)