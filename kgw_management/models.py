from django.db import models

class KGWJobDetail(models.Model):
    order_date = models.DateField()
    job_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    item_description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    advanced = models.DecimalField(max_digits=10, decimal_places=2)
    due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Job {self.job_no} - {self.customer_name}"

class KGWJobExpenses(models.Model):
    #serial_number = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    job_no = models.CharField(max_length=100)
    item_detail = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    uom = models.CharField(max_length=20, blank=True, null=True)  # UOM stands for Unit of Measurement
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Expense for Job {self.job.job_no}"

class KGWCashIn(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Cash In on {self.date}"

class KGWDailyExpense(models.Model):
    date = models.DateField(blank=True, null=True)
    job_no = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    uom = models.CharField(max_length=20, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Daily Expense for Job {self.job.job_no} on {self.date}"

class KGWStuffOvertime(models.Model):
    #serial_number = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    stuff_name = models.CharField(max_length=255)
    overtime_hour = models.DecimalField(max_digits=5, decimal_places=2)
    overtime_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    snacks = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    all_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stuff_name} Overtime"


class OfficeMachineriesExpense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    uom = models.CharField(max_length=50, verbose_name="Unit of Measure")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.description}"
    

class KCTSellList(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.invoice_no} - {self.customer_name}"


class KCTCost(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.description} - {self.date}"

