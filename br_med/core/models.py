import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class DefaultBaseModel(models.Model):
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)
    uuid = models.UUIDField(_("UUID"), unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Currency(DefaultBaseModel):
    name = models.CharField(_("moeda"), max_length=25)
    symbol = models.CharField(_("símbolo"), max_length=25)
    acronym = models.CharField(_("acrônimo"), max_length=3)

    class Meta:
        verbose_name = _("moeda")
        verbose_name_plural = _("moedas")

    def __str__(self):
        return f"{self.acronym} - {self.name}"

    def save(self, *args, **kwargs):
        self.acronym = self.acronym.upper()
        return super(Currency, self).save(*args, **kwargs)


class Quote(DefaultBaseModel):
    date = models.DateField(_("data de referência"))
    currency = models.ForeignKey("core.Currency", on_delete=models.CASCADE)
    value = models.DecimalField(_("valor da cotação"), max_digits=100, decimal_places=20)

    class Meta:
        verbose_name = _("cotação")
        verbose_name_plural = _("cotações")

    def __str__(self):
        return f"{self.currency.acronym} - {self.date} - {self.value}"
