from django.contrib import admin
from .models import Team, Participant, Payment

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'college_name', 'district', 'domain','idea_ppt')
    search_fields = ('team_name', 'college_name', 'district')
    list_filter = ('domain',)
    ordering = ('team_name',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'team', 'gender')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('gender',)
    ordering = ('name',)
    autocomplete_fields = ['team']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'payment_person_name', 'team','receipt_image')
    search_fields = ('transaction_id', 'payment_person_name')
    ordering = ('transaction_id',)
    autocomplete_fields = ['team']