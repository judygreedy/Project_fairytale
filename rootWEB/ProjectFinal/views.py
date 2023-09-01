from django.shortcuts import render

import json
import openai

openai.api_key = "FINAL_!"

# Create your views here.

def func_Make(request):
    return render(request, 'ProjectFinal/make.html')

def func_Fairytale(request):
    character_name = request.GET.get('character_name')
    character_age = request.GET.get('character_age')
    character_gender = request.GET.get('character_gender')
    character_personality = request.GET.get('character_personality')

    listener_age = request.GET.get('listener_age')
    listener_gender = request.GET.get('listener_gender')

    detail_mood = request.GET.get('detail_mood')
    detail_keyword = request.GET.get('detail_keyword')
    detail_length = request.GET.get('detail_length')

    context = {
        "character_name": character_name,
        "character_age": character_age,
        "character_gender": character_gender,
        "character_personality": character_personality,

        "listener_age": listener_age,
        "listener_gender": listener_gender,

        "detail_mood": detail_mood,
        "detail_keyword": detail_keyword,
        "detail_length": detail_length
    }

    context['ask_str'] = make_question(context)
    # context['answer_chatgpt'] = openapi_chatgpt(context['ask_str'])
    context['answer_chatgpt'] ="test_text"

    print(context)
    return render(request, 'ProjectFinal/fairytale.html', context)

##############################################################

def func_Index(request):
    return render(request, 'ProjectFinal/index.html')

def func_About(request):
    character_name = request.GET.get('character_name')
    character_age = request.GET.get('character_age')
    character_gender = request.GET.get('character_gender')
    character_personality = request.GET.get('character_personality')

    listener_age = request.GET.get('listener_age')
    listener_gender = request.GET.get('listener_gender')

    detail_mood = request.GET.get('detail_mood')
    detail_keyword = request.GET.get('detail_keyword')
    detail_length = request.GET.get('detail_length')

    context = {
        "character_name": character_name,
        "character_age": character_age,
        "character_gender": character_gender,
        "character_personality": character_personality,

        "listener_age": listener_age,
        "listener_gender": listener_gender,

        "detail_mood": detail_mood,
        "detail_keyword": detail_keyword,
        "detail_length": detail_length
    }

    context['ask_str'] = make_question(context)
    context['answer_chatgpt'] = openapi_chatgpt(context['ask_str'])

    print(context['answer_chatgpt'])
    return render(request, 'ProjectFinal/about.html', context)

def func_Blog(request):
    return render(request, 'ProjectFinal/blog.html')

def func_Contact(request):
    return render(request, 'ProjectFinal/contact.html')

def func_Services(request):
    return render(request, 'ProjectFinal/services.html')


def openapi_chatgpt(question):

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
        n = img_cnt,
        size = img_size
    )
    return response['data'][0]['url']


def make_question(input_info):
    result_str = f"Can you make a story in the form of 'dictionary'(python) using the following conditions by {input_info['detail_length']} chapters? Each chapter should include"
    result_str += f"(1) ‘chapter_number’ (2) ‘chapter_title‘ (3) ‘chapter_content’ (at least 5 sentences) (4) ‘chapter_atmosphere’ (5) ‘chapter_background’"
    result_str += f"1. Characters 1-1. Main character 1-1-1. name: {input_info['character_name']} 1-1-2. gender: {input_info['character_gender']} 1-1-3. characteristics: {input_info['character_personality']}"
    #     result_str += f"1-2. Sub character 1-2-1. name: {} 1-2-2. gender: {} 1-2-3. characteristics: {}"
    result_str += f"2. Target audience 2-1. age: {input_info['listener_age']} 2-2. gender: {input_info['listener_gender']}"
    result_str += f"3. Story 3-1. keyword: {input_info['detail_keyword']} 3-2. atmosphere: {input_info['detail_mood']} 3-3. the number of chapters: {input_info['detail_length']}"

    return result_str
