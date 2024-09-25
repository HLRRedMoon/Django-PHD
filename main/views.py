from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tutorial
from datetime import datetime
import joblib 
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from main.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Prediction
# Create your views here.
def welcome(request):
    return render(request, 'main/welcome.html')

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('main/welcome')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:welcome')
        else:
            messages.error(request, 'Username OR password does not exist')
           
    
    return render(request, 'main/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('main:welcome')


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect('main:welcome')
    else:
        form = UserCreationForm()
    return render(request, 'main/signin.html', {'form': form})

# def signin(request):
#     return render(request, 'main/signin.html')

# def login(request):
#     return render(request, 'main/login.html')
# def specialist(request):
#     # return HttpResponse("Hello <h1>HLR</h1>, Welcome to your site! ")
#     # return render(request=request, template_name="main/index.html", 
#     #               context={"tutorials": Tutorial.objects.all})
#     return render(request, 'main/index.html')

def profile(request):
    return render(request=request, template_name="main/profile.html", 
                  context={"tutorials": Tutorial.objects.all})


def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def prediction(request):
    if request.method == 'POST':
        # Extract data from request
        birthdate_str = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        chest_pain = request.POST.get('chest-pain')
        res_blood = request.POST.get('res-blood',"0")
        Cholesterol = request.POST.get('Cholesterol',"0")
        fasting = request.POST.get('fasting')
        electrocardiographic = request.POST.get('electrocardiographic')
        maximum = request.POST.get('maximum',"0")
        exang = request.POST.get('exang')
        ST = request.POST.get('ST',"0.0")
        slope = request.POST.get('slope')
        CA = request.POST.get('CA')
        thalassemia = request.POST.get('thalassemia')
        
        if not birthdate_str:
            return render(request, 'main/index.html', {'error': 'Birthdate is required.'})
            # messages.error(request, 'Birthdate is required.')
        # Convert birthdate string to datetime object
        try:
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')  # Make sure the format matches your input
        except ValueError:
            return render(request, 'main/index.html', {'error': 'Invalid birthdate format.'})
            # messages.error(request, 'Invalid birthdate format.')
        # Calculate age
        age = calculate_age(birthdate)

        # Convert other data as required
        try:
            features = [
                age,
                int(gender),
                int(chest_pain),
                float(res_blood),
                float(Cholesterol),
                int(fasting),
                int(electrocardiographic),
                float(maximum),
                int(exang),
                float(ST),
                int(slope),
                int(CA),
                int(thalassemia)
        ]

        except ValueError:
            return render(request, 'main/index.html', {'error': 'Invalid input format. Please check your entries.'})
            # messages.error(request, 'Invalid input format. Please check your entries.')
        # Load your model
        model = joblib.load("main/models/ML/RF_model.pkl")
        predict_name = "Specialist"

        # Make prediction
        prediction = model.predict_proba([features])[:, 1]
        if request.user.is_authenticated:
            # Save the prediction to the database
            Prediction.objects.create(
                user=request.user,
                prediction_result=str(prediction[0]*100),
                prediction_name = predict_name,
            )
        context = {
            'prediction':prediction[0]*100,
            'age': age,
            'gender': gender,
            'chest_pain':chest_pain,
            'res_blood':res_blood,
            'Cholesterol':Cholesterol,
            'fasting':fasting,
            'electrocardiographic':electrocardiographic,
            'maximum':maximum,
            'exang':exang,
            'ST':ST,
            'slope':slope,
            'CA':CA,
            'thalassemia':thalassemia,
        }
        return render(request, 'main/result.html', context)
        # return render(request, 'main/result.html', {'prediction': prediction[:, 1]})

    return render(request, 'main/index.html')

def calculate_age_in_days(birthdate):
    today = datetime.today()
    age_delta = today - birthdate
    return age_delta.days

def prediction_public(request):
    if request.method == 'POST':
        # Extract data from request
        birthdate_str = request.POST.get('birthdate')
        height = request.POST.get('height',"0")
        weight = request.POST.get('weight',"0")
        ap_hi = request.POST.get('ap_hi',"0")
        ap_lo = request.POST.get('ap_lo',"0")
        Cholesterol = request.POST.get('Cholesterol')
        smoke = request.POST.get('smoke')
        alco = request.POST.get('alco')
        active = request.POST.get('active')
        
        if not birthdate_str:
            return render(request, 'main/index.html', {'error': 'Birthdate is required.'})
            # messages.error(request, 'Birthdate is required.')
        # Convert birthdate string to datetime object
        try:
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')  # Make sure the format matches your input
        except ValueError:
            return render(request, 'main/index.html', {'error': 'Invalid birthdate format.'})
            # messages.error(request, 'Invalid birthdate format.')
        # Calculate age
        age = calculate_age_in_days(birthdate)

        # Convert other data as required
        try:
            features = [
                age,
                int(height),
                float(weight),
                int(ap_hi),
                int(ap_lo),
                int(Cholesterol),
                int(smoke),
                int(alco),
                int(active),
        ]
        except ValueError:
            return render(request, 'main/index.html', {'error': 'Invalid input format. Please check your entries.'})
        # Load your model
        model = joblib.load("main/models/ML/RF_kaggle_model.pkl")
        predict_name = "Public"
        # Make prediction
        prediction = model.predict([features])
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Save the prediction to the database
            Prediction.objects.create(
                user=request.user,
                prediction_result=str(prediction[0]*100),
                prediction_name = predict_name,
            )
        context = {
            'prediction':prediction[0]*100,
            'age': age,
            'height': height,
            'weight':weight,
            'ap_hi':ap_hi,
            'ap_lo':ap_lo,
            'Cholesterol':Cholesterol,
            'smoke':smoke,
            'alco':alco,
            'active':active,
        }
        return render(request, 'main/result.html', context)
        # return render(request, 'main/result.html', {'prediction': prediction[:, 1]})

    return render(request, 'main/public.html')

@login_required
def view_history(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-prediction_date')
    return render(request, 'main/history.html', {'predictions': predictions})

def delete_prediction(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id, user=request.user)  # Ensures ownership
    if request.method == 'POST':  # Confirm that the deletion is intentional
        prediction.delete()
        # Redirect to the history page or wherever you think is appropriate
        return redirect('main:history')
    