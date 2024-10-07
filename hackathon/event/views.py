from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Participant, Payment
from .forms import TeamForm, ParticipantForm, PaymentForm
from django.forms import modelformset_factory  # Import modelformset_factory from django.forms

def home(request):
    # Hackathon and College Information
    context = {
        'college_name': 'Government Engineering College Hassan',
        'college_description': 'Government Engineering College Hassan is a leading institution known for its innovation and excellence in education.',
        'hackathon_name': 'Tech-Trivia 2024',
        'hackathon_date': 'October 18-19, 2024',
        'hackathon_description': 'Tech-Trivia 2024 is a 24-hour coding competition where developers, students, and tech enthusiasts come together to solve real-world problems.',
        'sponsors': ['Kothati Timbers', 'Aluminis of GECH', 'Parvam']
    }
    return render(request, 'home.html', context)

def register(request):
    ParticipantFormSet = modelformset_factory(Participant, form=ParticipantForm, extra=4)  # For 4 participants

    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        formset = ParticipantFormSet(request.POST)

        if team_form.is_valid() and formset.is_valid():
            team = team_form.save()

            participants = formset.save(commit=False)
            for participant in participants:
                participant.team = team
                participant.save()

            return redirect('payment', team_id=team.id)

    else:
        team_form = TeamForm()
        formset = ParticipantFormSet(queryset=Participant.objects.none())

    return render(request, 'register.html', {'team_form': team_form, 'formset': formset})

def payment(request, team_id):
    
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.team = team
            payment.save()
            
            # Get the team leader's email (assuming it's the first participant in the team)
            team_leader_email = team.participants.first().email

            # Send confirmation email
            send_mail(
                'Registration Successful!',
                f'Thank you for registering, {team.participants.first().name}!\n\n'
                f'Team Name: {team.team_name}\n'
                f'College Name: {team.college_name}\n',
                settings.EMAIL_HOST_USER,  # From email
                [team_leader_email],  # To email (team leader)
                fail_silently=False,
            )
            
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'Payment_form': form,'team': team})

def payment_success(request):
    print("completed successfully")
    return redirect('home')
