# 📘 Fine‑Tuning d’un Modèle Génératif sur des Logs Système

## 🧠 Présentation du Projet

Ce projet a pour objectif de fine‑tuner un petit modèle génératif (GPT‑2, DistilGPT‑2 ou LLaMA‑tiny) afin de générer automatiquement des **lignes de logs système réalistes**.  

Le projet permet de :

- Comprendre le principe du fine‑tuning d’un modèle de langage.
- Préparer un jeu de données de logs pour l’apprentissage supervisé.
- Entraîner un petit modèle génératif sur ces données.
- Évaluer la qualité et la cohérence des logs générés.
- Identifier les enjeux de sécurité liés aux données sensibles.

### Contexte

Les administrateurs système collectent de grands volumes de logs (SSH, Apache, Windows, etc.) pour détecter des comportements anormaux.  
Les modèles génératifs peuvent être utilisés pour :

- Simuler des journaux réalistes pour tester un SIEM.
- Compléter des datasets pour entraîner des systèmes de détection d’anomalies.
- Identifier des patterns rares ou suspects.

---

## 📂 Structure du Projet

├── data/
│ ├── logs_raw.txt # Données brutes
│ └── logs_clean.txt # Données nettoyées
├── model_logs/ # Checkpoints (à ignorer dans Git)
├── train.py # Script de fine-tuning
├── generate.py # Script pour générer des logs
├── requirements.txt # Dépendances Python
└── README.md # Documentation


---

## ⚙️ Prérequis

- Python 3.10+
- pip
- GPU recommandé (CUDA pour accélérer l’entraînement)

Installer les dépendances :

```bash
pip install -r requirements.txt
```


# 📘 Préparation des Données

- Nettoyer les logs (supprimer timestamps inutiles, caractères spéciaux, lignes vides)
- Homogénéiser le format (une ligne = un log)
- Anonymiser les données sensibles (IP internes, identifiants, etc.)

Exemple de log formaté :

Jan 12 08:42:10 server sshd[2140]: Failed password for root from 192.168.1.24 port 52214 ssh2


---

# 🏋️‍♂️ Entraînement du Modèle

```bash
python train.py \
  --model_name distilgpt2 \
  --dataset_path data/logs_clean.txt \
  --output_dir model_logs/
```

Les checkpoints seront sauvegardés dans model_logs/.

# 🧪 Génération de Logs

```bash
python generate.py \
  --model_dir model_logs/checkpoint-XX \
  --num_lines 20
````
# 📊 Évaluation

- **Pertinence syntaxique** : Les logs générés ressemblent-ils à de vrais logs ?
- **Cohérence** : Structure correcte (timestamp, service, PID, action, IP…)
- **Diversité** : Le modèle ne répète pas les mêmes lignes
- **Sécurité** : Pas de fuite de données sensibles, pas de reproduction exacte de logs critiques

---

# 🔐 Sécurité & Éthique

- Toujours anonymiser les données avant entraînement.
- Ne pas publier de logs réels non anonymisés.
- Utiliser le modèle uniquement pour testing et recherche.

---

# 🚀 Objectifs Pédagogiques

- Comprendre le fine-tuning d’un modèle génératif.
- Préparer un dataset spécialisé pour l’entraînement.
- Fine-tuner un petit LLM pour générer des logs.
- Évaluer la qualité des générations.
- Identifier les risques liés aux données sensibles.

---

# 🤝 Auteur

Projet réalisé par **yamdev07**  
Dans le cadre du **TP Chapitre 1 – IA Générative & Sécurité Systèmes**.
