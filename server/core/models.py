from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom user model for Love and Ledger.
    Extends Django's AbstractUser to add wedding-specific fields.
    """
    # We'll use email as the username field
    email = models.EmailField(_('email address'), unique=True)
    
    # Wedding-specific fields
    wedding_date = models.DateField(null=True, blank=True)
    partner_name = models.CharField(max_length=256, blank=True)
    wedding_location = models.CharField(max_length=256, blank=True)
    
    # Override username field to use email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username is still required but not used for login
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['email']

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Get the user's full name."""
        return f"{self.first_name} {self.last_name}".strip() or self.email

    def get_short_name(self):
        """Get the user's short name."""
        return self.first_name or self.email.split('@')[0]

