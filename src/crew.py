from crewai import Agent, Task, Crew, Process
from chat.chat import build_chat

#Construção do chat para resgatar inteligencia do PDF
pdf_tool = build_chat()

# Agente supervisor
support_supervisor = Agent(
  role='Supervisor do setor de suporte',
  goal='Orienta os agentes conforme necessário, passando a informação para eles e retornando json com a resposta\
    final destes mesmo.'
)

# Agente de suporte, funcionário
support_agent = Agent(
    role='Agente de Suporte',
    goal='Responder perguntas sobre o sistema usando informações de um PDF.',
    tools=[pdf_tool]
)

# Agente de confirmação de informação, funcionário
support_agent_confirmed_information = Agent(
  role='Agente de confirmação das informações',
  goal='Confirmar as informações vindas do support_agent usando informações do PDF.',
  tools=[pdf_tool]
)

# Task dos agentes
support_task = Task(
    description="Responda às perguntas usando as informações do PDF.",
    expected_output='Resposta detalhada e precisa baseada nas informações do PDF.',
    tools=[pdf_tool],
    agent=[support_agent, support_agent_confirmed_information]
)

# Criação do vexame de agentes de suporte
crew = Crew(
    agents=[support_supervisor, support_agent_confirmed_information, support_agent],
    tasks=[support_task],
    process=Process.sequential
)