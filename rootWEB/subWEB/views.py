from django.shortcuts import render

import openai
import json

API_KEY = "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"

'''
---------------------------------------------------------------------------------
link : [url]/test/main
func : func_main
- main 화면 
'''
def func_main(request):
    print('>> func_main() call')
    return render(request, 'subWEB/index.html')

'''
---------------------------------------------------------------------------------
link : [url]/
func : func_openai
- openai 사용 위한 함수 
- 참조 링크 : https://platform.openai.com/docs/guides/gpt
'''
def func_openai(question):
    openai.api_key = API_KEY

    completion = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        message=[
            {"role":"user", "content":f"{question}"}
        ]
    )

    return completion['choices'][0]['message']['content']
