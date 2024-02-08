from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TestBaseAcc(models.Model):

    name = models.CharField(max_length=255, verbose_name="")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="")


class TestCash(TestBaseAcc): ...


class TestUser(TestBaseAcc): ...


class TestEntity(TestBaseAcc): ...


class TestProvider(TestBaseAcc): ...


class Account(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    account = GenericForeignKey('content_type', 'object_id')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='', default=0.00)

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]


class Schemes(models.Model):
    TYPE = (
        ("1", "ПРИХОД"),
        ("2", "РАСХОД"),
        ("3", "ПЕРЕМЕЩЕНИЕ"),
    )

    title = models.CharField(max_length=255, verbose_name="")
    sub = models.BooleanField(default=False, verbose_name="")
    plus = models.BooleanField(default=False, verbose_name="")

    move_first = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='move_first', verbose_name="")

    move_second = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='move_second', verbose_name="")

    move_third = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='move_third', blank=True, null=True, verbose_name="")


class Transaction(models.Model):
    schemes = models.ForeignKey(Schemes, on_delete=models.CASCADE, verbose_name="")
    move_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField(default=False)
    sub_flag = models.BooleanField(default=False)
    plus_flag = models.BooleanField(default=False)