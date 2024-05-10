# guIA tour
*Projeto de um programa para auxiliar no planejamento de viagens [Alura - IMERSÃO IA 2024].*

## Documentação e Apresentação do Projeto: Planejador de Viagens com GenerativeAI

### Introdução
Este projeto utiliza a API GenerativeAI do Google para criar um programa de planejamento de viagens personalizado. O programa coleta as preferências do usuário e gera um roteiro de viagem exclusivo com base nessas informações.

### Tecnologias Utilizadas
• **Python:** Linguagem de programação utilizada para desenvolver o programa.<br>
• **Google GenerativeAI API:** API que permite gerar texto criativo e personalizado com base em prompts e parâmetros.<br>
• **Google Colab:** Ambiente de desenvolvimento em nuvem usado para executar o código Python.

### Funcionamento
**1. Coleta de informações**<br>
O programa faz uma série de perguntas ao usuário para coletar informações sobre suas preferências de viagem, incluindo:<br>
• Destino<br>
• Duração da viagem<br>
• Companhia de viagem<br>
• Tipo de hospedagem<br>
• Orçamento<br>
• Atividades desejadas<br>
• Elementos essenciais<br>

**2. Geração do roteiro**<br>
As informações coletadas são utilizadas para criar um prompt para a API GenerativeAI. A API gera um roteiro de viagem personalizado com base no prompt e nos parâmetros de configuração.

**3. Apresentação do roteiro**<br>
O roteiro gerado é apresentado ao usuário.

### Código
O código Python apresentado utiliza a biblioteca google.generativeai para interagir com a API GenerativeAI. A função obter_destino() e outras funções similares coletam as informações do usuário.<br>
O dicionário viagem armazena as informações coletadas, que são então utilizadas para construir o prompt para a API. O modelo gemini-1.0-pro é utilizado para gerar o conteúdo, com um parâmetro de temperatura definido para 0.7, o que permite um certo grau de criatividade na geração do texto.<br>

### Apresentação para o Concurso

**Título:** Planejador de Viagens Personalizado com IA

**Descrição:** Este projeto utiliza a API GenerativeAI do Google para criar roteiros de viagem personalizados com base nas preferências do usuário. O programa coleta informações sobre o destino, duração, companhia, hospedagem, orçamento, atividades desejadas e elementos essenciais da viagem. Com base nessas informações, a API gera um roteiro único que atende às necessidades do usuário.

**Destaques:**
Personalização: O roteiro é gerado especificamente para cada usuário, levando em consideração suas preferências individuais.
Criatividade: A API GenerativeAI permite a criação de roteiros criativos e originais, que vão além dos roteiros turísticos tradicionais.
Facilidade de uso: O programa é fácil de usar e requer apenas que o usuário responda a algumas perguntas simples.

**Potencial:**
Este projeto tem o potencial de revolucionar a forma como as pessoas planejam suas viagens. Ele elimina a necessidade de pesquisas demoradas e permite que os usuários criem roteiros personalizados em minutos.

**Demonstração:**
Para demonstrar o projeto, você pode apresentar um exemplo de roteiro gerado para um destino específico, com base em um conjunto de preferências. Também é possível mostrar o código Python e explicar como ele funciona.

**Diferenciais:**
Integração com outras APIs: O projeto pode ser expandido para incluir a integração com outras APIs, como APIs de reserva de hotéis e voos, para oferecer uma experiência de planejamento de viagem completa.
Interface de usuário: Uma interface de usuário amigável pode ser desenvolvida para facilitar ainda mais o uso do programa.

## Conclusão
Este projeto demonstra o poder da API GenerativeAI do Google para criar aplicativos inovadores e úteis. O planejador de viagens personalizado é um exemplo de como a IA pode ser usada para melhorar a experiência do usuário e tornar as viagens mais acessíveis e agradáveis.
