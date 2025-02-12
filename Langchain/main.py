from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Configuração do modelo LLaMA
model_name = "adalbertojunior/Llama-3-8B-Instruct-Portuguese-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carregar o modelo e movê-lo explicitamente para a GPU (CUDA)
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             torch_dtype=torch.float16,
                                             low_cpu_mem_usage=True)

# Garantir que o modelo seja movido para a GPU
model = model.to("cuda")

# Configurar o pipeline de geração de texto
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,
)

# Definir as variáveis
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"
destino = "Florianópolis"

# Criar o prompt
prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias para Florianópolis, para uma família com {numero_de_criancas} crianças que gostam de {atividade}."

# Gerar a resposta usando o pipeline configurado
outputs = pipe(prompt)

# Extrair e imprimir a resposta gerada
resposta = outputs[0]['generated_text']
print(resposta)