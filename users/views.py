from django.shortcuts import render
from allauth.account.decorators import verified_email_required


@verified_email_required
def user_settings(request):
    return render(request, 'user_settings.html')