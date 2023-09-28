from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from app import *

def ask(cq, q):
    import openai
    openai.api_key="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"
    
    # 心靈雞湯
    cresponse = openai.Completion.create(
        model="curie:ft-yzu-2023-02-16-12-52-04",
        prompt=q,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["END"]
    )                     
    cstory = cresponse['choices'][0]['text']
    cstory = translate_text(cstory, 'zh-tw')
    
    # AI小幫手
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
                {"role": "user", "content": q}
            ]
    )
    aistory = completion["choices"][0]["message"]["content"]   

    # 最終結果
    question = "請幫我融合兩段話:\n({})\n({})".format(cstory, aistory)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
                {"role": "user", "content": question}
            ]
    )
    story = completion["choices"][0]["message"]["content"] 
    return story    