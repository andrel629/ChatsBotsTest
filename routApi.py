import requests
import json

api_key=""




x=input("faça sua pergunta:\n")


resp=requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization":f"Bearer {api_key}"   
    },
    data=json.dumps({
        "model":"xiaomi/mimo-v2-flash:free", ##modelo de ia
        "messages":[
            {
                "role":"user",
                "content":x
            }    
        ],
        "reasoning":{ ##salvar o raciocinio da IA
            "enabled":True
            }
    })##converte para uma string legivel no servidor
) ##requerimento via post

if resp.status_code==200:
    resposta=resp.json()
    resposta=resposta['choices'][0]['message'] ### a resposta da IA esta aqui 

    repet_message=[
        {   ##repetir o dialogo
            "role":"user",
            "content":x
        },
        {  ##pegando a resposta que a IA me deu e reinviando como contexto  
            "role":"assistant",
            "content":resposta.get('content'),
            "reasoning_details": resposta.get('reasoning_details')
        },
        {
            "role":"user",
            "content":"tem certeza disso?"
        }
    ]

    respostaFinal = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
        "Authorization":f"Bearer {api_key}"   
        },
         data=json.dumps({
            "model": "xiaomi/mimo-v2-flash:free",
            "messages": repet_message,  
            "reasoning": {"enabled": True}
        })
        )

    if respostaFinal.status_code==200:
        r=respostaFinal.json()
        print(r['choices'][0]['message']['content'])
    
    else:
        print(f'{respostaFinal.status_code} : {respostaFinal.text}')
else:
    print(f'{resp.status_code} : {resp.text}')