from django.db import models
from django.contrib.auth.models import User

class userInfo(User):
    age = models.IntegerField()
    contact = models.IntegerField()
    gender = models.CharField(max_length=10)



class genre(models.Model):
    name = models.CharField(max_length=30)
    

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.name

class book(models.Model):
    name =  models.CharField(max_length=30)
    price = models.IntegerField()
    img = models.ImageField(upload_to = 'images', default='')
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=300, default='')
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

class cart(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE )

    class Meta:
        db_table = 'cart'

    

class order(models.Model):
    total_bill = models.IntegerField()
    order_date = models.DateField(auto_now = True)
    order_status = models.CharField(max_length =30,default='processing')
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'order'
