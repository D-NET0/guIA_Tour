<a href="https://colab.research.google.com/drive/1N1_u7PpCICRKax2LCQ5u9Kzkt2gsgHvP?usp=sharing">
  <img src="https://i.ibb.co/JRrvV43/gu-IA-tour-logo.png" width="480" align="right">
</a>
<br><br><br>

# 🗺guIAtour
*Planejador de Viagens com GenerativeAI [Alura - IMERSÃO IA 2024].*<br>
[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N1_u7PpCICRKax2LCQ5u9Kzkt2gsgHvP?usp=sharing)<br>

## 💡 Introdução

Planejar uma viagem pode ser uma tarefa emocionante, mas também desafiadora. Com tantas opções de destinos, atividades, hospedagem e transporte, organizar todos os detalhes para criar um itinerário coeso e memorável pode se tornar um processo complexo e demorado.

Este projeto surge para simplificar o planejamento de viagens, utilizando o poder da inteligência artificial. Através da API GenerativeAI do Google, desenvolvemos um programa que coleta as preferências do usuário e gera um roteiro de viagem personalizado, adaptado às suas necessidades.

Imagine poder descrever seus sonhos de viagem - o destino ideal, as atividades que você sempre quis experimentar, o tipo de companhia e orçamento - e receber um roteiro detalhado e pronto para uso!  É exatamente isso que este programa oferece: uma solução inteligente para transformar o planejamento de viagens em um processo mais fácil, rápido e personalizado.

Este projeto utiliza a API GenerativeAI do Google para criar um programa de planejamento de viagens personalizado. O programa coleta as preferências do usuário e gera um roteiro de viagem exclusivo com base nessas informações.

## 🤨 Problema

Criar um roteiro de viagem que atenda às necessidades e expectativas de todos os viajantes pode ser um desafio, especialmente quando se trata de conciliar diferentes interesses, orçamentos e estilos de viagem. 

A pesquisa e comparação de opções de voos, hospedagem, passeios e restaurantes podem consumir muito tempo e energia. Além disso, garantir que o itinerário seja coerente, otimizado em termos de tempo e custo, e inclua todas as informações relevantes exige atenção aos detalhes. 

Muitas vezes, os viajantes acabam recorrendo a agências de viagens, que podem oferecer soluções personalizadas, mas com custos adicionais. 

##  😊 Solução

O guIAtour oferece uma solução inovadora para o planejamento de viagens, automatizando a criação de roteiros personalizados utilizando a API do Google GenerativeAI. O programa funciona em três etapas principais:

1. **Coleta de Informações:** O guIAtour realiza uma série de perguntas ao usuário para entender suas preferências de viagem. As informações coletadas incluem:
    * Destino
    * Duração da viagem
    * Companhia de viagem (nomes e idades)
    * Tipo de hospedagem
    * Orçamento
    * Atividades desejadas
    * Elementos essenciais da viagem 

2. **Geração do Roteiro:** Com base nas informações coletadas, o programa constrói um *prompt* detalhado para a API GenerativeAI.  A API utiliza algoritmos avançados de inteligência artificial para gerar um roteiro de viagem único e personalizado, levando em consideração todos os detalhes fornecidos pelo usuário.

3. **Apresentação do Roteiro:** O roteiro gerado é apresentado ao usuário de forma clara e organizada. 

## ⚙️ Arquitetura

O guIAtour é um programa Python que utiliza a biblioteca `google.generativeai` para interagir com a API GenerativeAI do Google. 

O código é estruturado em funções que coletam as informações do usuário, constroem o *prompt* para a API, e processam a resposta da API para apresentar o roteiro.

## 🚀 Tecnologias

* **Python:** Linguagem de programação utilizada para desenvolver o programa.
* **Google GenerativeAI API:** API que permite gerar texto criativo e personalizado com base em prompts e parâmetros.
* **Google Colab:** Ambiente de desenvolvimento em nuvem usado para executar o código Python.

## 💻 Instalação

Para utilizar o guIAtour, você precisa:

1. Ter uma conta Google e acesso ao Google Colab.
2. Obter uma chave de API para o Google GenerativeAI.
3. Copiar o código do projeto para um notebook no Google Colab.
4. Configurar a chave da API no código.

## 🕹️ Uso

1. Execute o código no Google Colab.
2. Responda às perguntas do programa sobre suas preferências de viagem.
3. Aguarde a geração do roteiro personalizado.
4. Visualize o roteiro gerado.

<a href="https://colab.research.google.com/drive/1N1_u7PpCICRKax2LCQ5u9Kzkt2gsgHvP?usp=sharing">
  <img src="https://i.ibb.co/JRrvV43/gu-IA-tour-logo.png" width="200">
</a>

*Clique na imagem acima para abrir a aplicação no Google Colab e começar a planejar sua viagem!*

## 🧪 Exemplos

**Exemplo de Prompt:**

![image](https://github.com/D-NET0/guIA_tour/assets/169196681/ab877dc0-daee-44d5-b861-248e7982393b)

**Exemplo de Roteiro Gerado:**

![image](https://github.com/D-NET0/guIA_tour/assets/169196681/00a32e54-a4ed-4e31-b054-8f0d20241efa)

## 📈 Status

O projeto guIAtour está em desenvolvimento contínuo, com planos de adicionar recursos como:

* Integração com APIs de reserva de voos e hotéis.
* Sugestões de restaurantes e atividades com base nas preferências do usuário.
* Visualização do roteiro em um mapa interativo.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* e enviar *pull requests*.

## 📞 Contatos

<a href="https://www.linkedin.com/in/dilermando-neto-b585849b/">
  <img src="https://i.ibb.co/YkQZk4G/icon-linkedin.png" width="50"></a>

<a href="https://www.instagram.com/netox">
  <img src="https://i.ibb.co/2Zdf23d/icon-instagram.png" width="50"></a>

<a href="https://wa.me/5581996066911">
  <img src="https://i.ibb.co/WfhJNCz/icon-whatsapp.png" width="50"></a>

<a href="https://t.me/dilermandoneto">
  <img src="https://i.ibb.co/q7kyjjb/icon-telegram.png" width="50"></a>

<a href="mailto:dilermando.neto@gmail.com">
  <img src="https://i.ibb.co/mvS9hFX/icon-email.png" width="50">
</a>
