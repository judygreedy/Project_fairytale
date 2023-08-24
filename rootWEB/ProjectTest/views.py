from django.shortcuts import render
from django.http import HttpResponse
import openai

openai.api_key = ""


# Create your views here.
def funcTest(request):
    print(">>> check_ProjectTest_funcTest")


    str_ask = " '초록사과의 과수원 대모험'으로 3개의 챕터로 구성된 동화를 제작해줘. dictionary 구성은  1) 챕터의 위치를 알수 있는 chapt, 2) 챕터의 제목을 알 수 있는 title, 3) 챕터의 내용을 넣은 content, 4) 이미지로 출력하고 싶어서 그런데 챕터의 내용을 이미지 설명하듯이 background에 넣어서 부탁해. 최종적으로 한개의 dictionary 형태로 대답 부탁해. dictionary 값 제외하고는 대괄호는 쓰지 말아줘"
    fairytale_dic = openai_chatgpt(str_ask)
    print(fairytale_dic)

    img_src = openapi_delle("cat in the box",1,"1024x1024")
    print(img_src)

    content = {
        "fairytale_dic" : fairytale_dic,
        "img_src" : img_src
    }

    return render(request, 'ProjectTest/test.html', content)

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