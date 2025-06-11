from django.db import models
from django.utils import timezone
from decimal import Decimal

from server.core.models import UserProfile

class Budget(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.name}'s Budget - ${self.amount}"

    def get_total_spent(self):
        """Calculate total amount spent across all expense items"""
        return self.expenseitem_set.aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')

    def get_remaining_budget(self):
        """Calculate remaining budget"""
        return self.amount - self.get_total_spent()

    def get_budget_utilization_percentage(self):
        """Calculate what percentage of budget has been used"""
        if self.amount == 0:
            return 0
        return (self.get_total_spent() / self.amount) * 100

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default='#007bff', help_text='Hex color code')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_expenses(self):
        """Get total amount spent in this category"""
        return self.expenseitem_set.aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')

    def get_expense_count(self):
        """Get number of expense items in this category"""
        return self.expenseitem_set.count()

class Vendor(models.Model):
    name = models.CharField(max_length=256)
    website = models.URLField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_expenses(self):
        """Get total amount spent with this vendor"""
        return self.expenseitem_set.aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')

    def get_expense_count(self):
        """Get number of expense items with this vendor"""
        return self.expenseitem_set.count()

class ExpenseItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(blank=True, null=True)
    paid_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Expense Item"
        verbose_name_plural = "Expense Items"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - ${self.amount} ({self.get_status_display()})"

    def is_overdue(self):
        """Check if the expense is overdue"""
        if self.due_date and self.status != 'paid':
            return self.due_date < timezone.now().date()
        return False

    def mark_as_paid(self):
        """Mark the expense as paid"""
        self.status = 'paid'
        self.paid_date = timezone.now().date()
        self.save()

    def get_days_until_due(self):
        """Get number of days until due date"""
        if self.due_date:
            delta = self.due_date - timezone.now().date()
            return delta.days
        return None
    
    