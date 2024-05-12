{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRBfF+tazYV41VpDspeN8w",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/D-NET0/guIA_tour/blob/main/guIA_tour.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importando o SDK"
      ],
      "metadata": {
        "id": "LW99bm5t4zfw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "userdata.get('secret_key')\n",
        "api_key = userdata.get('secret_key')\n",
        "genai.configure(api_key=api_key)"
      ],
      "metadata": {
        "id": "3UAZq4-Cs8Wy"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Funções para coletar informações da viagem"
      ],
      "metadata": {
        "id": "zZWL1_P85Gu2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def obter_destino():\n",
        "  return input(\"Para onde você quer viajar? \")\n",
        "\n",
        "def obter_duracao():\n",
        "  return input(\"Quanto tempo de viagem? \")\n",
        "\n",
        "def obter_companhia():\n",
        "  return input(\"Outras pessoas vão com você? Se sim, informe os nomes e idade aproximada de todos. \")\n",
        "\n",
        "def obter_hospedagem():\n",
        "  return input(\"Que tipo de hospedagem você procura (Hostel, Pousada, Hotel, Resort, etc)? \")\n",
        "\n",
        "def obter_orcamento():\n",
        "  return input(\"Quanto ao investimento, que tipo de viagem você procura (Econômica, Standard ou Luxo)? \")\n",
        "\n",
        "def obter_atividades():\n",
        "  return input(\"Que tipo de atividades você quer fazer (Culturais, Esportivas, Gastronômicas, Ecoturismo, etc)? \")\n",
        "\n",
        "def obter_essenciais():\n",
        "  return input(\"O que não pode faltar nesta viagem? \")"
      ],
      "metadata": {
        "id": "AcD0zD3gtDp_"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Coletar informações da viagem"
      ],
      "metadata": {
        "id": "2d4CsSR-5L97"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "viagem = {}\n",
        "viagem['destino'] = obter_destino()\n",
        "viagem['duracao'] = obter_duracao()\n",
        "viagem['companhia'] = obter_companhia()\n",
        "viagem['hospedagem'] = obter_hospedagem()\n",
        "viagem['orcamento'] = obter_orcamento()\n",
        "viagem['atividades'] = obter_atividades()\n",
        "viagem['essenciais'] = obter_essenciais()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uBYxEhMYtIhW",
        "outputId": "d070c228-8179-41b4-bc3e-475888a0b235"
      },
      "execution_count": 6,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Para onde você quer viajar? Recife\n",
            "Quanto tempo de viagem? 3\n",
            "Outras pessoas vão com você? Se sim, informe os nomes e idade aproximada de todos. Neto, 43 anos\n",
            "Que tipo de hospedagem você procura (Hostel, Pousada, Hotel, Resort, etc)? Hostel\n",
            "Quanto ao investimento, que tipo de viagem você procura (Econômica, Standard ou Luxo)? Standard\n",
            "Que tipo de atividades você quer fazer (Culturais, Esportivas, Gastronômicas, Ecoturismo, etc)? Culturais e gastrpmômicas\n",
            "O que não pode faltar nesta viagem? IRB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Implementar a geração do roteiro com genai"
      ],
      "metadata": {
        "id": "SRHXpwSU5wxM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model_name = \"gemini-1.0-pro\"\n",
        "generation_config = {\n",
        "  \"temperature\": 0.5,\n",
        "}\n",
        "\n",
        "model = genai.GenerativeModel(model_name='gemini-1.0-pro',\n",
        "                              generation_config=generation_config)\n",
        "\n",
        "prompt = f\"Crie um roteiro de viagem para {viagem['destino']} com duração de {viagem['duracao']} para {viagem['companhia']}, considerando hospedagem tipo {viagem['hospedagem']}, orçamento {viagem['orcamento']} e atividades {viagem['atividades']}. Não pode faltar {viagem['essenciais']}.\"\n",
        "\n",
        "response = model.generate_content(prompt)\n",
        "\n",
        "print(response.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 798
        },
        "id": "qIXRKDSLxEys",
        "outputId": "691376f2-82f8-4ec6-9d26-ac971fff8fd1"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "**Roteiro de Viagem para Recife (3 Dias)**\n",
            "\n",
            "**Público-alvo:** Neto, 43 anos\n",
            "\n",
            "**Orçamento:** Standard\n",
            "\n",
            "**Tipo de Hospedagem:** Hostel\n",
            "\n",
            "**Foco:** Atividades Culturais e Gastronômicas\n",
            "\n",
            "**Dia 1**\n",
            "\n",
            "* **Manhã:**\n",
            "    * Chegue ao Aeroporto Internacional do Recife (REC) e pegue um táxi ou Uber para o hostel no bairro de Boa Viagem.\n",
            "    * Faça o check-in no hostel e deixe sua bagagem.\n",
            "* **Tarde:**\n",
            "    * Visite o Instituto Ricardo Brennand (IRB), um museu que abriga uma vasta coleção de arte, armas e armaduras.\n",
            "    * Explore os jardins do IRB, que oferecem vistas panorâmicas da cidade.\n",
            "* **Noite:**\n",
            "    * Jante no Restaurante Oficina do Sabor, conhecido por sua culinária nordestina autêntica.\n",
            "    * Passeie pelo calçadão de Boa Viagem, apreciando a vista do mar e a vida noturna.\n",
            "\n",
            "**Dia 2**\n",
            "\n",
            "* **Manhã:**\n",
            "    * Visite o Museu do Homem do Nordeste, que exibe a história e a cultura da região Nordeste do Brasil.\n",
            "    * Descubra a arte e a cultura local no Mercado de São José, um mercado movimentado com artesanato, alimentos e lembranças.\n",
            "* **Tarde:**\n",
            "    * Faça um passeio de barco pelo Rio Capibaribe, passando por pontos turísticos como o Marco Zero e o Parque das Esculturas.\n",
            "    * Visite o Recife Antigo, o centro histórico da cidade, com ruas de paralelepípedos, igrejas coloniais e restaurantes charmosos.\n",
            "* **Noite:**\n",
            "    * Experimente a culinária local no Restaurante Boi Preto, especializado em pratos tradicionais nordestinos.\n",
            "    * Assista a um show de forró, um gênero musical popular na região, em uma das casas de shows do Recife Antigo.\n",
            "\n",
            "**Dia 3**\n",
            "\n",
            "* **Manhã:**\n",
            "    * Visite a Praia de Boa Viagem, uma das praias mais populares da cidade, para relaxar e aproveitar o sol.\n",
            "    * Faça compras de lembranças e artesanato na Feira de Artesanato de Boa Viagem.\n",
            "* **Tarde:**\n",
            "    * Explore o Jardim Botânico do Recife, um oásis verde com uma variedade de plantas e flores.\n",
            "    * Visite o Museu Cais do Sertão, que conta a história da cultura sertaneja do Nordeste.\n",
            "* **Noite:**\n",
            "    * Jante no Restaurante Coco Bambu, conhecido por seus frutos do mar frescos e pratos regionais.\n",
            "    * Retorne ao hostel para fazer o check-out e pegar um táxi ou Uber para o aeroporto para o seu voo de volta.\n"
          ]
        }
      ]
    }
  ]
}