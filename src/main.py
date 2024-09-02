# src/main.py

import os
from dotenv import load_dotenv
from crew import crew  # Importa a configuração da crew

load_dotenv()

def start_support():
    print("Bem-vindo ao suporte! Pergunte suas dúvidas sobre o sistema.")
    while True:
        question = input("Cliente: ")
        if question.lower() in ["sair", "exit"]:
            print("Encerrando o atendimento. Obrigado!")
            break
        
        result = crew.kickoff(inputs={'question': question})
        print(f"Suporte: {result}")

if __name__ == "__main__":
    start_support()
