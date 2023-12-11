
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
# from openai import OpenAI
import json


# Create your views here.
# open_api_key = "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"
# open_api_key = "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"
# openai.api_key = open_api_key


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



 
 


        
    
# def ask_openai(message):
#     client = OpenAI()
#     response = client.chat.completions.create(
#     # response = openai.chat.completions.create(
#     # response = openai.ChatCompletion.create(
#     # model="gpt-4",
#     model="gpt-3.5-turbo",
#     messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message},
# #             {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
# #             {"role": "user", "content": "Where was it played?"}
            
# ]
    
# )
    
#     answer = response['choices'][0]['message']['content']
#     # answer = response.choice[0].text.strip()
#     return answer


# def getValue(request):
#     data = json.loads(request.body)
#     message = data["msg"] 
#     response = ask_openai(message)
#     print(response)
#     QuestionAnswer.objects.create(user = request.user, question=message, answer=response)
#     return JsonResponse({"msg": message, "res": response})
#     # return JsonResponse("it is working(views.py)", safe=False)



openai_api_key = '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'
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
    
# def ask_openai(message):
#     open_api_key = "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"
#     openai.api_key = open_api_key
#     # openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )

#     answer = response['choices'][0]['message']['content']
#     return answer

def getValue(request):
    data = json.loads(request.body)
    message = data.get("msg", "")  # Use get to handle missing keys gracefully

    if message:
        response = ask_openai(message)
        print(response)
        QuestionAnswer.objects.create(user=request.user, question=message, answer=response)
        return JsonResponse({"msg": message, "res": response})
    else:
        return JsonResponse({"error": "Invalid request data"}, status=400)  
    
