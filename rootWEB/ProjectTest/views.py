from django.shortcuts import render
from django.http import HttpResponse
import openai
import json



# Test 용으로 잘 작동하는지 확인하기 위한 파일 입니다. 

# Create your views here.

def funcTest(request):
    print(openapi_delle("Esther, a curious girl, builds a rocket with friends and launches it from her nature-surrounded town, reaching awe-inspiring heights in the sky. Journeying through space, she encounters marvelous sights but faces fuel shortage. Resourcefully finding a space station, she heads home, driven by her insatiable curiosity and wonder for the universe.",1,"1024x1024"))
    return render(request, 'ProjectTest/test.html')

def funcTestFinal(request):

    return render(request, 'ProjectTest/test_main.html')

def funcTestHome(request):
    return render(request, 'ProjectTest/test_home.html')

def funcTestResult(request):
    # print(request.GET)
    # print(request.method)
    # print(request.path)
    character_name = request.GET.get('character_name')
    character_age = request.GET.get('character_age')
    character_gender = request.GET.get('character_gender')
    character_personality = request.GET.get('character_personality')

    listener_age = request.GET.get('listener_age')
    listener_gender = request.GET.get('listener_gender')

    detail_mood = request.GET.get('detail_mood')
    detail_keyword = request.GET.get('detail_keyword')
    detail_length = request.GET.get('detail_length')

    context= {
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
    context['answer_chatgpt'] = openai_chatgpt(context['ask_str'])

    return render(request, 'ProjectTest/test_result.html',context)



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













# def funcOpenAI(request):
#     print(">>> check_ProjectTest_funcTest")
#
#     str_ask = '''
#     {예원}이란 이름을 가진 {5살} {여자} 아이를 위해 동화를 제작하려 해. {디즈니-주토피아, 디즈니-인어공주}가 이 아이가 제일 좋아하는 컨텐츠라고 말해줬어. 결과적으로 나는 그 아이를 위해 {활기넘치는} 동화를 제작하려 해. 동화의 길이는 총 {5개} 챕터로 구성해줘.
#     동화의 구성은 챕터 순차번호인 "chapter_idx", 챕터 타이틀인 "chapter_title" , 챕터 내용인 "chapter_content", 각 챕터의 분위기를 나타내는 "chapter_mood",  각 챕터가 발생한 장소를 설명한 "chapter_background"로 나타내줘.
#     "chapter_title"은 1개의 문장, "chapter_content"는 최소 5줄의 문장으로 구성해줬으면 해.
#     마지막으로 "character"이라는 변수에 주인공 이름인 "name"과 주인공 생김새인 "face"로 추가해줘.
#     또 주인공과 같이 나오는 조연들은 "sub_character"이라는 변수에 각 조연들의 이름을"sub_name", 조연들의 생김새는 "sub_face"에 넣어줘.
#     최종적으로 json 형식의 데이터를 나에게 주면 좋겠어. '''
#
#     fairytale_dic = openai_chatgpt(str_ask)
#     fairytale_dic = json.loads(fairytale_dic.replace('"','\"'))
#
#     print(type(fairytale_dic))
#     print(fairytale_dic)
#
#     print("check detail >> title ::")
#     print(fairytale_dic['title'])
#
#     print("check detail >> content ::")
#     print(fairytale_dic['content'])
#
#     img_src = openapi_delle("Draw a 5-year-old girl with bobbed hair playing in a playground. I would love to see the whole playground.",1,"1024x1024")
#     # img_src = openapi_delle(fairytale_dic['content'],1,"1024x1024")
#
#     print(img_src)
#
#     content = {
#         "fairytale_dic" : fairytale_dic,
#         "title" : fairytale_dic['title'],
#         "content": fairytale_dic['content'],
#         "img_src" : img_src
#     }
#
#     return render(request, 'ProjectTest/test.html', content)
#     # return render(request)
#
#
#
# def openai_chatgpt(question):
#
#     completion = openai.ChatCompletion.create(
#       model = 'gpt-3.5-turbo',
#       messages = [
#           {"role": "system", "content": "You are a helpful assistant."},
#           {"role": "user", "content": f"{question}"},
#       ],
#       temperature = 0
#     )
#
#     return completion['choices'][0]['message']['content']
#
# def openapi_delle(description, img_cnt , img_size):
#     response = openai.Image.create(
#         prompt = description,
#         n = img_cnt,
#         size = img_size
#     )
#
#     return response['data'][0]['url']