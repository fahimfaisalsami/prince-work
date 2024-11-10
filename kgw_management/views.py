from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import KGWJobDetail, KGWJobExpenses, KGWDailyExpense, KGWCashIn, KGWStuffOvertime
from .forms import KGWJobDetailForm, KGWJobExpensesForm, KGWDailyExpenseForm, KGWCashInForm, KGWStuffOvertimeForm
from django.shortcuts import render
from django.db.models import Q  # Import Q for complex queries

def index(request):
    return render(request, 'kgw_management/index.html')

# Views for KGW Job Detail
class JobListView(ListView):
    model = KGWJobDetail
    template_name = 'kgw_management/job_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search query
        if query:
            # Filter based on the job number (or any other field you want)
            queryset = queryset.filter(Q(job_no__icontains=query))
        return queryset

class JobDetailView(DetailView):
    model = KGWJobDetail
    template_name = 'kgw_management/job_detail.html'

class JobCreateView(CreateView):
    form_class = KGWJobDetailForm  # Use the customized form
    template_name = 'kgw_management/job_form.html'
    success_url = reverse_lazy('job-list')

class JobUpdateView(UpdateView):
    model = KGWJobDetail
    form_class = KGWJobDetailForm  # Use the customized form
    template_name = 'kgw_management/job_form.html'
    success_url = reverse_lazy('job-list')

class JobDeleteView(DeleteView):
    model = KGWJobDetail
    template_name = 'kgw_management/job_confirm_delete.html'
    success_url = reverse_lazy('job-list')


# Views for KGW Job Expenses
class JobExpenseListView(ListView):
    model = KGWJobExpenses
    template_name = 'kgw_management/job_expense_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search query
        if query:
            # Filter based on the job number (or any other field you want)
            queryset = queryset.filter(
            Q(item_detail__icontains=query) |
            Q(job_no__icontains=query))
        return queryset
    
class JobExpenseDetailView(DetailView):
    model = KGWJobExpenses
    template_name = 'kgw_management/job_expense_detail.html'

class JobExpenseCreateView(CreateView):
    form_class = KGWJobExpensesForm  # Use the customized form
    template_name = 'kgw_management/job_expense_form.html'
    success_url = reverse_lazy('job-expense-list')

class JobExpenseUpdateView(UpdateView):
    model = KGWJobExpenses
    form_class = KGWJobExpensesForm  # Use the customized form
    template_name = 'kgw_management/job_expense_form.html'
    success_url = reverse_lazy('job-expense-list')

class JobExpenseDeleteView(DeleteView):
    model = KGWJobExpenses
    template_name = 'kgw_management/job_expense_confirm_delete.html'
    success_url = reverse_lazy('job-expense-list')


# Views for KGW Daily Expense
class DailyExpenseListView(ListView):
    model = KGWDailyExpense
    template_name = 'kgw_management/daily_expense_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search query
        if query:
            # Filter based on the job number (or any other field you want)
            queryset = queryset.filter(Q(job_no__icontains=query))
        return queryset
    
class DailyExpenseDetailView(DetailView):
    model = KGWDailyExpense
    template_name = 'kgw_management/daily_expense_detail.html'

class DailyExpenseCreateView(CreateView):
    form_class = KGWDailyExpenseForm  # Use the customized form
    template_name = 'kgw_management/daily_expense_form.html'
    success_url = reverse_lazy('daily-expense-list')

class DailyExpenseUpdateView(UpdateView):
    model = KGWDailyExpense
    form_class = KGWDailyExpenseForm  # Use the customized form
    template_name = 'kgw_management/daily_expense_form.html'
    success_url = reverse_lazy('daily-expense-list')

class DailyExpenseDeleteView(DeleteView):
    model = KGWDailyExpense
    template_name = 'kgw_management/daily_expense_confirm_delete.html'
    success_url = reverse_lazy('daily-expense-list')


# Views for KGW Cash In
class CashInListView(ListView):
    model = KGWCashIn
    template_name = 'kgw_management/cash_in_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search query
        if query:
            # Filter based on the job number (or any other field you want)
            queryset = queryset.filter(
            Q(description__icontains=query) |
            Q(amount__icontains=query) |
            Q(note__icontains=query) |
            Q(date__icontains=query)  # You can also filter by date if needed
        )
        return queryset
    
class CashInDetailView(DetailView):
    model = KGWCashIn
    template_name = 'kgw_management/cash_in_detail.html'

class CashInCreateView(CreateView):
    form_class = KGWCashInForm  # Use the customized form
    template_name = 'kgw_management/cash_in_form.html'
    success_url = reverse_lazy('cash-in-list')

class CashInUpdateView(UpdateView):
    model = KGWCashIn
    form_class = KGWCashInForm  # Use the customized form
    template_name = 'kgw_management/cash_in_form.html'
    success_url = reverse_lazy('cash-in-list')

class CashInDeleteView(DeleteView):
    model = KGWCashIn
    template_name = 'kgw_management/cash_in_confirm_delete.html'
    success_url = reverse_lazy('cash-in-list')


# Views for KGW Staff Overtime
class StaffOvertimeListView(ListView):
    model = KGWStuffOvertime
    template_name = 'kgw_management/staff_overtime_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        query = self.request.GET.get('q')  # Get the search query
        if query:
            # Filter based on the job number (or any other field you want)
            queryset = queryset.filter(Q(stuff_name__icontains=query))
        return queryset
    
class StaffOvertimeDetailView(DetailView):
    model = KGWStuffOvertime
    template_name = 'kgw_management/staff_overtime_detail.html'

class StaffOvertimeCreateView(CreateView):
    form_class = KGWStuffOvertimeForm  # Use the customized form
    template_name = 'kgw_management/staff_overtime_form.html'
    success_url = reverse_lazy('staff-overtime-list')

class StaffOvertimeUpdateView(UpdateView):
    model = KGWStuffOvertime
    form_class = KGWStuffOvertimeForm  # Use the customized form
    template_name = 'kgw_management/staff_overtime_form.html'
    success_url = reverse_lazy('staff-overtime-list')

class StaffOvertimeDeleteView(DeleteView):
    model = KGWStuffOvertime
    template_name = 'kgw_management/staff_overtime_confirm_delete.html'
    success_url = reverse_lazy('staff-overtime-list')


from django.urls import reverse_lazy
from .models import OfficeMachineriesExpense
from .forms import OfficeMachineriesExpenseForm
from django.db.models import Q

class OfficeExpenseListView(ListView):
    model = OfficeMachineriesExpense
    template_name = 'kgw_management/office_expense_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(description__icontains=query))
        return queryset

class OfficeExpenseDetailView(DetailView):
    model = OfficeMachineriesExpense
    template_name = 'kgw_management/office_expense_detail.html'

class OfficeExpenseCreateView(CreateView):
    model = OfficeMachineriesExpense
    form_class = OfficeMachineriesExpenseForm
    template_name = 'kgw_management/office_expense_form.html'
    success_url = reverse_lazy('office-expense-list')

class OfficeExpenseUpdateView(UpdateView):
    model = OfficeMachineriesExpense
    form_class = OfficeMachineriesExpenseForm
    template_name = 'kgw_management/office_expense_form.html'
    success_url = reverse_lazy('office-expense-list')

class OfficeExpenseDeleteView(DeleteView):
    model = OfficeMachineriesExpense
    template_name = 'kgw_management/office_expense_confirm_delete.html'
    success_url = reverse_lazy('office-expense-list')


from .models import KCTSellList
from .forms import KCTSellListForm

# List View for KCT Sell List
class KCTSellListView(ListView):
    model = KCTSellList
    template_name = 'kgw_management/kct_sell_list.html'
    context_object_name = 'sell_items'

# Detail View for KCT Sell List
class KCTSellDetailView(DetailView):
    model = KCTSellList
    template_name = 'kgw_management/kct_sell_detail.html'
    context_object_name = 'sell_item'

# Create View for KCT Sell List
class KCTSellCreateView(CreateView):
    model = KCTSellList
    form_class = KCTSellListForm
    template_name = 'kgw_management/kct_sell_form.html'
    success_url = reverse_lazy('kct-sell-list')

# Update View for KCT Sell List
class KCTSellUpdateView(UpdateView):
    model = KCTSellList
    form_class = KCTSellListForm
    template_name = 'kgw_management/kct_sell_form.html'
    success_url = reverse_lazy('kct-sell-list')

# Delete View for KCT Sell List
class KCTSellDeleteView(DeleteView):
    model = KCTSellList
    template_name = 'kgw_management/kct_sell_confirm_delete.html'
    success_url = reverse_lazy('kct-sell-list')


from .models import KCTCost
from .forms import KCTCostForm

# View to list all KCTCost entries
class KCTCostListView(ListView):
    model = KCTCost
    template_name = 'kgw_management/kct_cost_list.html'
    context_object_name = 'kct_cost_list'
    paginate_by = 10  # Number of items per page

    def get_queryset(self):
        # You can customize the query if needed, for example:
        return KCTCost.objects.all()

# View to create a new KCTCost entry
class KCTCostCreateView(CreateView):
    model = KCTCost
    form_class = KCTCostForm
    template_name = 'kgw_management/kct_cost_form.html'
    success_url = reverse_lazy('kct-cost-list')  # Redirect to the list page after success

# View to update an existing KCTCost entry
class KCTCostUpdateView(UpdateView):
    model = KCTCost
    form_class = KCTCostForm
    template_name = 'kgw_management/kct_cost_form.html'
    success_url = reverse_lazy('kct-cost-list')  # Redirect to the list page after success

# View to delete a KCTCost entry
class KCTCostDeleteView(DeleteView):
    model = KCTCost
    template_name = 'kgw_management/kct_cost_confirm_delete.html'  # Confirmation page before deletion
    success_url = reverse_lazy('kct-cost-list')  # Redirect to the list page after deletion

