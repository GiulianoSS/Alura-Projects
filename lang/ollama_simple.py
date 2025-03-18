import subprocess

# Variables
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)

# Ollama's full folder path
ollama_path = r"C:\Users\giuli\AppData\Local\Programs\Ollama\ollama.exe"

# Executing Ollama localy
result = subprocess.run(
    [ollama_path, "run", "mistral", prompt],
    capture_output=True,
    text=True
)


if result.returncode == 0:
    print("Resposta")
    print(result.stdout.strip)
else:
    print(f"Erro ao executar o Ollama: {result.stderr}")

# Storing the generated response
roteiro_viagem = result.stdout.strip()  # Ajuste para pegar só a parte da resposta