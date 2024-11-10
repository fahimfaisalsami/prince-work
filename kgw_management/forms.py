from django import forms
from .models import KGWJobDetail, KGWJobExpenses, KGWDailyExpense, KGWCashIn, KGWStuffOvertime

# Form for KGW Job Detail
class KGWJobDetailForm(forms.ModelForm):
    class Meta:
        model = KGWJobDetail
        fields = '__all__'
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def save(self, commit=True):
        # First save the JobDetail instance
        job_detail = super().save(commit=commit)

        # Now create or update related Job Expenses
        KGWJobExpenses.objects.create(
            date=job_detail.order_date,
            job_no=job_detail.job_no,
            item_detail=None, 
            quantity=None, 
            unit_price=None, 
            total=None, 
            uom = None
        )

        # Create or update related Daily Expense
        KGWDailyExpense.objects.create(
            date=job_detail.order_date, 
            job_no=job_detail.job_no, 
            detail=None, 
            quantity=None, 
            unit_price=None, 
            total=None,
            uom = None
        )

        return job_detail

# Form for KGW Job Expenses
class KGWJobExpensesForm(forms.ModelForm):
    class Meta:
        model = KGWJobExpenses
        fields = ['date', 'job_no', 'item_detail', 'quantity', 'uom', 'unit_price', 'total', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# Form for KGW Daily Expense
class KGWDailyExpenseForm(forms.ModelForm):
    class Meta:
        model = KGWDailyExpense
        fields = ['date', 'job_no', 'detail', 'quantity', 'uom', 'unit_price', 'total']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# Form for KGW Cash In
class KGWCashInForm(forms.ModelForm):
    class Meta:
        model = KGWCashIn
        fields = ['date', 'description', 'amount', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# Form for KGW Stuff Overtime
class KGWStuffOvertimeForm(forms.ModelForm):
    class Meta:
        model = KGWStuffOvertime
        fields = ['date', 'stuff_name', 'overtime_hour', 'overtime_amount', 'total', 'snacks', 'all_total']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

from .models import OfficeMachineriesExpense

class OfficeMachineriesExpenseForm(forms.ModelForm):
    class Meta:
        model = OfficeMachineriesExpense
        fields = ['date', 'description', 'quantity', 'uom', 'unit_price', 'total', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        

from .models import KCTSellList

class KCTSellListForm(forms.ModelForm):
    class Meta:
        model = KCTSellList
        fields = ['date', 'invoice_no', 'customer_name', 'item_description', 'quantity', 'unit_price', 'total', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

from .models import KCTCost

class KCTCostForm(forms.ModelForm):
    class Meta:
        model = KCTCost
        fields = ['date', 'description', 'amount', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }

