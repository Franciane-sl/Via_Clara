# Via Clara

**Atendimento inteligente para quem está na estrada.**

O Via Clara é um sistema de atendimento virtual desenvolvido com arquitetura multiagente para auxiliar usuários de rodovias e pedágios. O projeto utiliza agentes especializados para responder dúvidas, orientar sobre contestações de cobranças e consultar informações financeiras demonstrativas.

O objetivo é demonstrar como agentes de Inteligência Artificial podem trabalhar de forma integrada para oferecer um atendimento organizado, especializado e eficiente.

## Funcionalidades

O sistema possui três agentes especializados e um agente orquestrador.

### 1. Agente de dúvidas (`doubts_agent`)

Responsável por responder perguntas relacionadas a:
- Tarifas de pedágio.
- Formas de pagamento.
- Funcionamento de tags de pagamento automático.
- Isenções.
- Informações gerais sobre rodovias.

Utiliza uma base de conhecimento em JSON para fornecer informações ao modelo de linguagem.

### 2. Agente de contestações (`contestation_agent`)

Responsável por orientar usuários que identificam possíveis problemas em cobranças, como:
- Cobrança duplicada.
- Cobrança não reconhecida.
- Valor divergente.
- Possível cobrança indevida para usuário com direito à isenção.
- Falhas na tag de pagamento automático.

As orientações são baseadas em informações cadastradas em uma base de conhecimento.

### 3. Agente financeiro (`billing_agent`)

Responsável por consultar informações financeiras demonstrativas, como:
- Débitos pendentes.
- Pagamentos realizados.
- Tarifas de pedágio cadastradas.
- Total de débitos pendentes.

As consultas são realizadas diretamente em Python, utilizando dados armazenados em arquivos JSON, sem depender de respostas geradas por IA para apresentar valores financeiros.

### 4. Agente orquestrador (`orchestrator`)

Responsável por identificar a intenção da mensagem do usuário e encaminhá-la ao agente especializado correspondente.

O fluxo de atendimento é:

1. O usuário envia uma mensagem.
2. O orquestrador identifica a intenção.
3. A solicitação é encaminhada ao agente responsável.
4. O agente processa a solicitação.
5. A resposta é apresentada ao usuário.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Ollama:** execução local de modelos de linguagem.
- **Qwen 2.5 1.5B:** modelo de linguagem utilizado no atendimento.
- **JSON:** armazenamento das bases de conhecimento e dados demonstrativos.
- **python-dotenv:** gerenciamento de variáveis de ambiente.
- **pytest:** ferramenta para testes automatizados.

## Estrutura do projeto

```text
Via_Clara/
│
├── agents/
│   ├── doubts_agent.py
│   ├── contestation_agent.py
│   ├── billing_agent.py
│   └── orchestrator.py
│
├── config/
│   └── settings.py
│
├── data/
│   ├── faq.json
│   ├── contestation_reasons.json
│   ├── customers.json
│   └── tariffs.json
│
├── tools/
│   ├── knowledge_base.py
│   └── operations.py
│
├── utils/
│   └── ollama_client.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior.
- Ollama.
- Git.

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Franciane-sl/Via_Clara.git
```

### 2. Acessar a pasta do projeto

```bash
cd Via_Clara
```

### 3. Criar um ambiente virtual

Windows:

```powershell
python -m venv .venv
```

### 4. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar o Ollama

Instale o Ollama e baixe o modelo utilizado pelo projeto:

```bash
ollama pull qwen2.5:1.5b
```

Inicie o servidor Ollama:

```bash
ollama serve
```

### 7. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência.

Configuração:

```env
OLLAMA_MODEL=qwen2.5:1.5b
OLLAMA_HOST=http://localhost:11434
```

O arquivo `.env` contém configurações locais e não deve ser enviado ao repositório.

### 8. Executar o projeto

Com o ambiente virtual ativado e o Ollama em execução, utilize:

```bash
python main.py
```

## Exemplos de utilização

O Via Clara pode responder a diferentes tipos de solicitações.

**Dúvidas sobre pedágios:**

```text
Usuário: Como funciona uma tag de pedágio?
```

**Contestações:**

```text
Usuário: Fui cobrado duas vezes no mesmo pedágio.
```

**Consultas financeiras:**

```text
Usuário: Quais são meus débitos pendentes?
Via Clara: Informe seu ID demonstrativo.

Usuário: 1
```

O sistema apresenta os débitos cadastrados para o cliente demonstrativo.

Para encerrar o atendimento:

```text
Usuário: sair
```

## Dados demonstrativos

O projeto utiliza dados fictícios armazenados em arquivos JSON para simular clientes, débitos, pagamentos e tarifas.

Esses dados são utilizados exclusivamente para demonstração das funcionalidades do sistema.

As tarifas apresentadas não representam valores oficiais de concessionárias.

## Limitações do MVP

- O atendimento é realizado exclusivamente pelo terminal.
- Não possui banco de dados integrado.
- Não possui autenticação de usuários.
- Não realiza pagamentos reais.
- Não registra contestações oficialmente.
- Não consulta informações em tempo real de concessionárias.
- As respostas dos agentes que utilizam modelos de linguagem podem apresentar limitações de precisão.

## Autora

Desenvolvido por [Franciane](https://github.com/Franciane-sl).
