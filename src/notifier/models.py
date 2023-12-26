from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Notification(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="notifications", null=False, blank=True)
    text = models.TextField(_("text"), null=False, blank=True)
    is_seen = models.BooleanField(_("is seen"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("notification_details", kwargs={"pk": self.pk})
