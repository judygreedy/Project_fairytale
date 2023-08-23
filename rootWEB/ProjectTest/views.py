from django.shortcuts import render
from django.http import HttpResponse
import openai

openai.api_key = ""


# Create your views here.
def funcTest(request):
    print(">>> check_ProjectTest_funcTest")
    #print(openai_chatgpt("아메리카노 어린이 대모험 으로 챕터 3개인 동화를 제작해줘. dictionary 형태로 부탁해"))
    print(openapi_delle("고양이",1,"1024x1024"))


    return render(request, 'ProjectTest/test.html')

def openai_chatgpt(question):

    completion = openai.ChatCompletion.create(
      model = 'gpt-3.5-turbo',
      messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": f"{question}"},
      ],
      temperature = 0
    )

    return completion['choices'][0]['message']['content']

def openapi_delle(description, img_cnt , img_size):
    response = openai.Image.create(
        prompt = description,
        n= img_cnt,
        size = img_size
    )

    return response['data'][0]['url']