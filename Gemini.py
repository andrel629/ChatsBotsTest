## minha chave de acesso
from google import genai
##
client =genai.Client(api_key="")##falta a apikey

x=1
contrato=True
exit_confere=0

print("Insira seus dados")
usuario=input('Escreva seu nome:\n')
idade=input("Escreva sua idade:\n")
Tipo=input("Me fale como sera nossa conversa:\n")

interacao = client.interactions.create(
        model='gemini-2.5-flash',
        input=f'Essa é sua primeira interação com {usuario}, que possui {idade} e deseja ter uma conversa {Tipo}, não precisa falar a idade e nem o tipo da conersa neste primeiro momento quero so um boa noite.',
        generation_config={
               "temperature": 0.65,
                "max_output_tokens": 500,
                "thinking_level": "high",
        }
    )
print(interacao.outputs[-1].text)
x=x+1

    
while  contrato==True:
    print("\n *********************************************************************************** \n")
    user=input("faça sua pergunta ou digite um numero para finalizar : \n")
    print("\n *********************************************************************************** \n")
    try:
            exit_confere=int(user)
    except:
            exit_confere=0
    
    if exit_confere==1:
            contrato=False
    else:
        if x%2==0:
                interacao2=client.interactions.create(
                    model='gemini-2.5-flash',
                    input=f'{user}, adicione uma linha sem nada no final',
                     generation_config={
                    "temperature": 0.65,
                    "max_output_tokens": 500,
                    "thinking_level": "high",
                },
                    previous_interaction_id=interacao.id
                )
                print(interacao2.outputs[-1].text)
                x=x+1
        else:
                interacao=client.interactions.create(
                    model='gemini-2.5-flash',
                    input=f'{user}, adicione linha sem nada no final',
                     generation_config={
                    "temperature": 0.65,
                    "max_output_tokens": 500,
                    "thinking_level": "high",
                },
                    previous_interaction_id=interacao2.id
                )
                print(interacao.outputs[-1].text)
                x=x+1

print('Sua conversa foi concluida')