import datetime

from django.shortcuts import render
# import http response
from django.http import JsonResponse,HttpResponse
import openai
from .models import *
import uuid

# Create your views here.

def chatgptprompt(request,PromptInput):
    if (request.method == "GET"):
        openai.api_key = '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'

        model = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": PromptInput},

            ]
        )

        reply = response['choices'][0]['message']['content']
        tokens = response['usage']['total_tokens']
        cost = tokens*0.002
        P_Id = uuid.uuid4()
        while Prompt.objects.filter(P_Id=P_Id).exists():
            P_Id = uuid.uuid4()

        P = Prompt.objects.create(P_Id=P_Id , Date=datetime.date , Promt_message = PromptInput,
                          Response= reply,cost=cost,Token=tokens , Modelused=model)

        P.save()
        response = HttpResponse(reply, content_type='text/plain' )
        print(response)

        return response

def dall_e(request,PromptInput):
    if (request.method == "GET"):
        openai.api_key = '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'

        model = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": PromptInput},

            ]
        )

        reply = response['choices'][0]['message']['content']
        tokens = response['usage']['total_tokens']
        cost = tokens*0.002
        P_Id = uuid.uuid4()
        while Prompt.objects.filter(P_Id=P_Id).exists():
            P_Id = uuid.uuid4()

        P = Prompt.objects.create(P_Id=P_Id , Date=datetime.date , Promt_message = PromptInput,
                          Response= reply,cost=cost,Token=tokens , Modelused=model)

        P.save()
        response = HttpResponse(reply, content_type='text/plain' )
        print(response)

        return response



def chatgpthtml(request):
    if (request.method == "GET"):
        return render(request, 'chatgpt.html')
    elif (request.method == "POST"):
        return render(request, 'chatgpt.html')

def usage(request):
    if (request.method == "GET"):
        Ps = Prompt.objects.all()
        Total = 0
        Tokens = 0
        for p in Ps:
            Total += p.cost
            Tokens += p.Token

        res = {
            'Total':Total,
            'Tokens':Tokens
        }
        return HttpResponse(res, content_type='text/')
