from crewai import Agent, Task, Crew, Process
from tools import PDFVectorStoreTool

pdf_tool = PDFVectorStoreTool(pdf_path='src/pdf/contrato.pdf')

support_agent = Agent(
    role='Agente de Suporte',
    goal='Responder perguntas sobre o sistema usando informações de um PDF.',
    tools=[pdf_tool]
)

support_task = Task(
    description="Responda às perguntas usando as informações do PDF.",
    expected_output='Resposta detalhada e precisa baseada nas informações do PDF.',
    tools=[pdf_tool],
    agent=support_agent,
)

# Configuração da crew
crew = Crew(
    agents=[support_agent],
    tasks=[support_task],
    process=Process.sequential
)
