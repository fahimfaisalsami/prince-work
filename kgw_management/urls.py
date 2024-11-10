from django.urls import path
from . import views
from .views import index

from .views import (
    OfficeExpenseListView, 
    OfficeExpenseDetailView, 
    OfficeExpenseCreateView, 
    OfficeExpenseUpdateView, 
    OfficeExpenseDeleteView
)

urlpatterns = [
    
    path('', index, name='index'),  # This links the index view to the root URL
    
    # Job Details
    path('jobs/', views.JobListView.as_view(), name='job-list'),
    path('jobs/new/', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),

    # Job Expenses
    path('job-expenses/', views.JobExpenseListView.as_view(), name='job-expense-list'),
    path('job-expenses/new/', views.JobExpenseCreateView.as_view(), name='job-expense-create'),
    path('job-expenses/<int:pk>/', views.JobExpenseDetailView.as_view(), name='job-expense-detail'),
    path('job-expenses/<int:pk>/update/', views.JobExpenseUpdateView.as_view(), name='job-expense-update'),
    path('job-expenses/<int:pk>/delete/', views.JobExpenseDeleteView.as_view(), name='job-expense-delete'),

    # Daily Expenses
    path('daily-expenses/', views.DailyExpenseListView.as_view(), name='daily-expense-list'),
    path('daily-expenses/new/', views.DailyExpenseCreateView.as_view(), name='daily-expense-create'),
    path('daily-expenses/<int:pk>/', views.DailyExpenseDetailView.as_view(), name='daily-expense-detail'),
    path('daily-expenses/<int:pk>/update/', views.DailyExpenseUpdateView.as_view(), name='daily-expense-update'),
    path('daily-expenses/<int:pk>/delete/', views.DailyExpenseDeleteView.as_view(), name='daily-expense-delete'),

    # Cash In
    path('cash-in/', views.CashInListView.as_view(), name='cash-in-list'),
    path('cash-in/new/', views.CashInCreateView.as_view(), name='cash-in-create'),
    path('cash-in/<int:pk>/', views.CashInDetailView.as_view(), name='cash-in-detail'),
    path('cash-in/<int:pk>/update/', views.CashInUpdateView.as_view(), name='cash-in-update'),
    path('cash-in/<int:pk>/delete/', views.CashInDeleteView.as_view(), name='cash-in-delete'),

    # Staff Overtime
    path('staff-overtime/', views.StaffOvertimeListView.as_view(), name='staff-overtime-list'),
    path('staff-overtime/new/', views.StaffOvertimeCreateView.as_view(), name='staff-overtime-create'),
    path('staff-overtime/<int:pk>/', views.StaffOvertimeDetailView.as_view(), name='staff-overtime-detail'),
    path('staff-overtime/<int:pk>/update/', views.StaffOvertimeUpdateView.as_view(), name='staff-overtime-update'),
    path('staff-overtime/<int:pk>/delete/', views.StaffOvertimeDeleteView.as_view(), name='staff-overtime-delete'),

    path('office-expense/', OfficeExpenseListView.as_view(), name='office-expense-list'),
    path('office-expense/<int:pk>/', OfficeExpenseDetailView.as_view(), name='office-expense-detail'),
    path('office-expense/create/', OfficeExpenseCreateView.as_view(), name='office-expense-create'),
    path('office-expense/update/<int:pk>/', OfficeExpenseUpdateView.as_view(), name='office-expense-update'),
    path('office-expense/delete/<int:pk>/', OfficeExpenseDeleteView.as_view(), name='office-expense-delete'),

    # KCT Sell List
    path('kct-sell-list/', views.KCTSellListView.as_view(), name='kct-sell-list'),
    path('kct-sell-list/new/', views.KCTSellCreateView.as_view(), name='kct-sell-create'),
    path('kct-sell-list/<int:pk>/', views.KCTSellDetailView.as_view(), name='kct-sell-detail'),
    path('kct-sell-list/<int:pk>/update/', views.KCTSellUpdateView.as_view(), name='kct-sell-update'),
    path('kct-sell-list/<int:pk>/delete/', views.KCTSellDeleteView.as_view(), name='kct-sell-delete'),

    # KCT Cost
    path('kct-cost/', views.KCTCostListView.as_view(), name='kct-cost-list'),  # List view
    path('kct-cost/create/', views.KCTCostCreateView.as_view(), name='kct-cost-create'),  # Create view
    path('kct-cost/update/<int:pk>/', views.KCTCostUpdateView.as_view(), name='kct-cost-update'),  # Update view
    path('kct-cost/delete/<int:pk>/', views.KCTCostDeleteView.as_view(), name='kct-cost-delete'),  # Delete view

]
