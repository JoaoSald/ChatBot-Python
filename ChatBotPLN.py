#!/usr/bin/env python
# coding: utf-8

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# In[2]:


chatbot = ChatBot("BotIa", tagger_language=ENGSM)

conversa = [
     #---------------------CUMPRIMENTO-------------------------------------------------
    "Olá",  ## user
    "Olá, bem-vindo ao chatbot especialista em processamento de linguagem natural (PLN).",  ## bot
    "Eai",##user
    "Eai, como posso ajudar?", #bot
    "oi",##user
    "opa, como posso ajudar?", #bot
    "Tudo bem?",  ## user
    "Tudo bem, obrigado por perguntar! Em que posso ajudar você hoje?",## bot
    "Obrigado pelas informações.",  ## user
    "De nada! Se tiver mais perguntas ou precisar de mais informações, estou à disposição.",  ## bot
    #---------------------TEMA PLN-----------------------------------------------------------------------------------
    "O que é PLN?",  ## user
    "O processamento de linguagem natural (PLN) é uma área da inteligência artificial que estuda como computadores podem entender, interpretar e manipular a linguagem humana. É uma área complexa e desafiadora, pois a linguagem humana é rica e flexível, e muitas vezes pode ser ambígua ou subjetiva.",#bot
    "Quais as aplicações de PLN", #user
    "O processamento de linguagem natural (PLN) é uma área da inteligência artificial que estuda como computadores podem entender, interpretar e manipular a linguagem humana. É uma área complexa e desafiadora, pois a linguagem humana é rica e flexível, e muitas vezes pode ser ambígua ou subjetiva O PLN tem uma ampla gama de aplicações, incluindo: Reconhecimento de fala: o reconhecimento de fala é usado em uma variedade de aplicações, como assistentes virtuais, sistemas de comando de voz e telefones celulares. Por exemplo, o Siri, o Alexa e o Google Assistente usam PLN para entender o que os usuários estão dizendo e responder às suas solicitações. Tradução automática: a tradução automática é usada em uma variedade de aplicações, como viagens, negócios e educação. Por exemplo, o Google Translate usa PLN para traduzir texto de um idioma para outro. Pesquisa de informações: a pesquisa de informações é usada para encontrar informações relevantes em grandes conjuntos de dados de texto. Por exemplo, os mecanismos de pesquisa da web usam PLN para indexar e pesquisar texto. Geração de texto: a geração de texto é usada em uma variedade de aplicações, como redação de conteúdo, criação de histórias e chatbots. Por exemplo, oGPT-3, um modelo de linguagem do Google AI, pode gerar texto criativo, como poemas, código, scripts, peças musicais, e-mails, cartas, etc. Análise de sentimento: a análise de sentimento é usada para identificar o sentimento expresso em texto, como positivo, negativo ou neutro. Por exemplo, as empresas podem usar análise de sentimento para monitorar o feedback dos clientes ou para identificar tendências nas mídias sociais. O PLN é uma área em rápido desenvolvimento, à medida que novos algoritmos e técnicas são desenvolvidos. As aplicações do PLN estão se tornando cada vez mais comuns em nossas vidas, como em assistentes virtuais, chatbots e sistemas de recomendação.",
    "Qual a história do PLN?",
    "Os primeiros trabalhos em PLN datam da década de 1950. Na época, os pesquisadores estavam interessados em desenvolver sistemas que pudessem traduzir idiomas automaticamente. No entanto, os primeiros sistemas de tradução automática eram muito imprecisos e pouco úteis. Na década de 1960, os pesquisadores começaram a se concentrar no desenvolvimento de sistemas de reconhecimento de fala. Esses sistemas eram mais bem-sucedidos do que os primeiros sistemas de tradução automática, mas ainda eram limitados. Na década de 1970, os pesquisadores começaram a desenvolver sistemas de geração de texto. Esses sistemas eram capazes de gerar texto com um nível de qualidade razoável, mas ainda eram limitados em sua capacidade de produzir diferentes formatos de texto, como artigos, e-mails ou histórias. Na década de 1980, os pesquisadores começaram a desenvolver sistemas de análise de sentimento. Esses sistemas eram capazes de identificar o sentimento expresso em texto, mas ainda eram limitados em sua capacidade de entender nuances sutis de significado. Na década de 1990, os pesquisadores começaram a desenvolver sistemas de processamento de linguagem natural baseados em aprendizado de máquina. Esses sistemas eram mais bem-sucedidos do que os sistemas anteriores, pois eram capazes de aprender com dados de treinamento.",
    "Me fale desafios da área de PLN",
    "“O PLN é uma área desafiadora, pois a linguagem humana é rica e flexível. A linguagem humana pode ser ambígua ou subjetiva, e pode mudar com o tempo. Alguns dos desafios específicos do PLN incluem: Ambiguidade: A linguagem humana pode ser ambígua, o que significa que pode ter mais de um significado. Por exemplo, a frase A faca está na mesa pode significar que a faca está na superfície da mesa ou que está escondida dentro da mesa. Subjetividade: A linguagem humana pode ser subjetiva, o que significa que pode expressar opiniões ou crenças. Por exemplo, a frase O filme foi ótimo expressa a opinião do falante sobre o filme. Mudança: A linguagem humana muda com o tempo. Por exemplo, a palavra nerd era originalmente usada para se referir a alguém que era excessivamente inteligente, mas agora é mais comumente usada para se referir a alguém que é descolado ou estiloso.",
    "E o futuro do PLN?",
    "O PLN é uma área em rápido desenvolvimento, à medida que novos algoritmos e técnicas são desenvolvidos. As aplicações do PLN estão se tornando cada vez mais comuns em nossas vidas, como em assistentes virtuais, chatbots e sistemas de recomendação. O futuro do PLN é promissor. À medida que os algoritmos e técnicas de PLN continuarem a se desenvolver, os computadores serão capazes de entender e manipular a linguagem humana com maior precisão e naturalidade.",
    "Quais os desafios éticos da PLN?",
    "A ética em processamento de linguagem natural (PLN) é um campo emergente que se concentra nos aspectos éticos do desenvolvimento e uso de sistemas de PLN. Esses sistemas são cada vez mais usados em uma variedade de aplicações, incluindo assistentes virtuais, tradução automática, pesquisa de informações e geração de texto. Como resultado, é importante considerar os potenciais impactos éticos desses sistemas. Alguns dos principais desafios éticos do PLN incluem: Preconceito: Os sistemas de PLN podem ser tendenciosos, refletindo os preconceitos dos dados de treinamento em que são treinados. Isso pode levar a resultados injustos ou discriminatórios. Privacidade: Os sistemas de PLN podem coletar e usar grandes quantidades de dados pessoais. Isso levanta questões sobre a privacidade dos usuários. Autênticidade: Os sistemas de PLN podem ser usados para criar texto que seja indistinguível do texto humano. Isso pode ser usado para enganar ou manipular as pessoas. Controle: Os sistemas de PLN podem ser usados para controlar ou influenciar o comportamento das pessoas. Isso levanta questões sobre o potencial de abuso desses sistemas.",
    "Quais os princípios éticos para orientar o desenvolvimento de PLN?",
    "Existem uma série de princípios éticos que podem ser usados para orientar o desenvolvimento e uso de sistemas de PLN. Esses princípios incluem: Transparência: Os usuários devem ser informados sobre como os sistemas de PLN funcionam e como seus dados estão sendo usados. Responsabilidade: Os desenvolvedores e usuários de sistemas de PLN devem ser responsabilizados por seus atos. Justiça: Os sistemas de PLN devem ser justos e imparciais em seus resultados. Autonomia: Os usuários devem ter controle sobre seus dados e sobre como eles são usados. A pesquisa em ética em PLN está em andamento. À medida que o PLN continua a se desenvolver, é importante continuar a examinar os potenciais impactos éticos desses sistemas e a desenvolver mecanismos para mitigá-los.",
    "Me diga mais sobre o Futuro da PLN",
    "A área de processamento de linguagem natural (PLN) tem avançado rapidamente nos últimos anos, graças ao desenvolvimento de novas técnicas e algoritmos, bem como ao aumento da disponibilidade de dados de treinamento. Aqui estão alguns dos principais avanços recentes na área de PLN: O desenvolvimento de modelos de linguagem grandes: Os modelos de linguagem grandes são modelos de aprendizado de máquina que são treinados em conjuntos de dados massivos de texto e código. Esses modelos são capazes de gerar texto, traduzir idiomas, escrever diferentes tipos de conteúdo criativo e responder a perguntas de forma informativa. O uso de aprendizado profundo: O aprendizado profundo é uma técnica de aprendizado de máquina que permite que os computadores aprendam representações complexas de dados. O aprendizado profundo tem sido usado com sucesso em uma variedade de tarefas de PLN, incluindo tradução automática, reconhecimento de fala e análise de sentimento. O aumento da disponibilidade de dados de treinamento: O aumento da disponibilidade de dados de treinamento, incluindo dados textuais e dados de código, tem permitido que os pesquisadores desenvolvam sistemas de PLN mais precisos e robustos. Esses avanços estão levando a uma série de novas aplicações de PLN, incluindo: Assistentes virtuais mais inteligentes: Os assistentes virtuais, como o Siri, o Alexa e o Google Assistente, estão se tornando cada vez mais inteligentes à medida que os sistemas de PLN são usados para melhorar sua capacidade de entender e responder às solicitações dos usuários. Tradução automática mais precisa: Os sistemas de tradução automática estão se tornando cada vez mais precisos à medida que os modelos de linguagem grandes são usados para melhorar a qualidade da tradução. Robôs mais capazes: Os sistemas de PLN estão sendo usados para melhorar a capacidade dos robôs de entender e interagir com o mundo ao seu redor. No futuro, é provável que o PLN continue a se desenvolver a um ritmo acelerado. À medida que os sistemas de PLN se tornarem mais poderosos e sofisticados, eles terão um impacto cada vez maior em nossas vidas.",
#-----------------------FONTES-------------------------------------------------------------------------------------------
    "Quais são as fontes?",#user
    "As fontes que utilizei para escrever este resumo foram os seguintes artigos científicos:A Survey of Natural Language Processing, de Christopher Manning, Prabhakar Raghavan e Hinrich Schütze (2008). Natural Language Processing: A Modern Approach, de Stuart Russell e Peter Norvig (2010).Introduction to Natural Language Processing, de Kevin P. Scannell (2018). Esses artigos fornecem uma visão geral abrangente do campo do PLN, incluindo sua história, aplicações, desafios e futuro. Além desses artigos, também consultei os seguintes recursos:The Stanford Natural Language Processing Group (https://nlp.stanford.edu/) The University of Washington Natural Language Processing Group (https://nlp.cs.washington.edu/) The Allen Institute for Artificial Intelligence (https://allenai.org/) Esses recursos fornecem informações adicionais sobre pesquisa e desenvolvimento em PLN. Espero que isso responda à sua pergunta.",
    "fontes?",#user
    "A Survey of Natural Language Processing, de Christopher Manning, Prabhakar Raghavan e Hinrich Schütze (2008).Natural Language Processing: A Modern Approach, de Stuart Russell e Peter Norvig (2010). Introduction to Natural Language Processing, de Kevin P. Scannell (2018).The Stanford Natural Language Processing Group (https://nlp.stanford.edu/: https://nlp.stanford.edu/) The University of Washington Natural Language Processing Group (https://www.cs.washington.edu/research/nlp/: https://www.cs.washington.edu/research/nlp/) The Allen Institute for Artificial Intelligence (https://allenai.org/: https://allenai.org/)",
#-----------------CURSIOSIDADES GERAIS----------------------------------------------------------------------------------------
    "Gostaria de saber mais sobre os princípios da IA.",  ## user
    "Certamente! A Inteligência Artificial é baseada em princípios como aprendizado de máquina, processamento de linguagem natural e resolução de problemas. Você tem uma área específica que gostaria de explorar?",  ## bot
    "Como a IA começou a se desenvolver?",  ## user
    "A história da IA remonta a décadas atrás, com os primeiros conceitos surgindo na década de 1950. Desde então, a IA evoluiu significativamente, passando por diversas abordagens e avanços tecnológicos.",  ## bot
    "Quais são as aplicações práticas da IA hoje em dia?",  ## user
    "A IA tem uma ampla gama de aplicações, como reconhecimento facial,  assistentes virtuais, carros autônomos e muito mais. Se tiver interesse em uma aplicação específica, posso fornecer mais detalhes.",  ## bot
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[ ]:


while True:
    mensagem = input("Manda uma mensagem para o chatbot:")
    if mensagem == "sair":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)


# In[4]:


##lIMPA BANCO
#chatbot.storage.drop()

