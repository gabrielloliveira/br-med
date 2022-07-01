import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from br_med.core.enums import CurrencyEnum


class DefaultBaseModel(models.Model):
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)
    uuid = models.UUIDField(_("UUID"), unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Quote(DefaultBaseModel):
    date = models.DateField(_("data de referência"))
    currency = models.CharField(_("moeda"), max_length=3, choices=CurrencyEnum.choices)
    value = models.DecimalField(_("valor da cotação"), max_digits=100, decimal_places=20)

    class Meta:
        verbose_name = _("cotação")
        verbose_name_plural = _("cotações")

    def __str__(self):
        return f"{self.currency} - {self.date} - {self.value}"
