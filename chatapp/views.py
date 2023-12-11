
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date, timedelta
from .models import QuestionAnswer
import openai
from .models import QuestionAnswer 
from django.http import JsonResponse
import json




@login_required(login_url='signin')
def index(request):
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    seven_days_ago = date.today() - timedelta(days=7)
    
    questions = QuestionAnswer.objects.filter(user=request.user)
    t_questions = questions.filter(created=today)
    y_questions = questions.filter(created=yesterday)
    s_questions = questions.filter(created__gte=seven_days_ago, created__lte=today)
    
    context = {"t_questions":t_questions, "y_questions": y_questions, "s_questions": s_questions}

    return render(request, "chatapp/index.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    context = {"form": form}
    return render(request, "chatapp/signup.html", context)


def signin(request):
    err = None
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        
        else:
            err = "Invalid Credentials"
        
        
    context = {"error": err}
    return render(request, "chatapp/signin.html", context)


def signout(request):
    logout(request)
    return redirect("signin")




openai_api_key = 'Create your own api key'
# openai_api_key = ''
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.completions.create( 
        model = "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        
    )
    
    answer = response.choices[0].text.strip()
    return answer
    


def getValue(request):
    data = json.loads(request.body)
    message = data.get("msg", "")  

    if message:
        response = ask_openai(message)
        print(response)
        QuestionAnswer.objects.create(user=request.user, question=message, answer=response)
        return JsonResponse({"msg": message, "res": response})
    else:
        return JsonResponse({"error": "Invalid request data"}, status=400)  
    
