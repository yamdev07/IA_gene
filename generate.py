from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Charger le modèle et le tokenizer
model = GPT2LMHeadModel.from_pretrained("./model_logs")
tokenizer = GPT2Tokenizer.from_pretrained("./model_logs")

# Prompt initial pour générer les logs
prompt = "Nov 12 14:32:21 server sshd[24511]:"

# Tokenization avec attention mask
inputs = tokenizer(prompt, return_tensors="pt", padding=True)

# Génération de plusieurs logs
outputs = model.generate(
    **inputs,  # passe input_ids + attention_mask
    max_length=120,  # longueur maximale de chaque log
    num_return_sequences=5,  # nombre de logs à générer
    do_sample=True,  # échantillonnage aléatoire
    top_p=0.95,  # nucleus sampling
    temperature=0.8,  # contrôle la "créativité"
    pad_token_id=tokenizer.eos_token_id  # pour éviter les warnings
)

# Affichage clair des logs générés
for i, output in enumerate(outputs):
    generated_text = tokenizer.decode(output, skip_special_tokens=True)

    # Formattage pour éviter que le texte déborde sur une seule ligne
    print(f"\n--- Log généré #{i + 1} ---\n{generated_text}\n{'-' * 50}")
