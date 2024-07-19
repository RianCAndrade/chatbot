import openai

my_api = "SUA CHAVE API CHATGPT" #tua chave API do chatgpt

openai.api_key = my_api

def enviar_mensagem(mensagem, lista_mensagens = []):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    
    resposta = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )
    
    return resposta["choices"][0]["message"]

lista_mensagens = []
while True:
    perg = input('Digite uma pergunta: ')
    
    if (perg == "sair"):
        break
    else:
        resposta = enviar_mensagem(perg, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot: ", perg["content"])


print(enviar_mensagem("Em que ano Einstein publicou a teoria geral da relatividade?")) #tua pergunta ou duvida