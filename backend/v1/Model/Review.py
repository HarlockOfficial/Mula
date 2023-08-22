from django.db import models

from user_management.Model import UserModel


class ReviewModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey('SupermarketProductPriceModel', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
