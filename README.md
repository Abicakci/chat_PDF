# chat_PDF
Chatbot avec pdf

Description
Le chatbot Langchain pour PDF est une application conversationnelle alimentée par des modèles OpenAI et Hugging Face.
Son objectif est de fournir une interface de chat permettant aux utilisateurs de poser des questions sur le contenu d'un document PDF et de recevoir des réponses pertinentes extraites de ce document.

Fonctionnalités
Prise en charge d'un seul PDF : Les utilisateurs peuvent télécharger un seul document PDF pour effectuer des recherches d'informations.
Recherche conversationnelle : Le chatbot utilise des techniques de recherche conversationnelle pour fournir des réponses pertinentes et contextuelles aux questions des utilisateurs.
Modèles linguistiques : Le chatbot intègre des modèles OpenAI et Hugging Face pour comprendre et générer du langage naturel, améliorant ainsi la qualité des conversations.
Extraction de texte PDF : Le document PDF est traité pour extraire son contenu textuel, qui est utilisé pour l'indexation et la recherche.
Découpage de texte : Le texte extrait est divisé en morceaux plus petits pour améliorer l'efficacité de la recherche et fournir des réponses plus précises.
Installation

Pour installer et exécuter le chatbot Langchain, suivez ces étapes :
Clonez le dépôt : git clone https://github.com/Abicakci/chat_multi_pdf.git
Créez un environnement virtuel : pip install virtualenv puis python -m venv <nom_environnement>, enfin, activez l'environnement virtuel avec <nom_environnement>\Scripts\activate
Installez les dépendances à partir du fichier requirements.txt : pip install -r requirements.txt
Ajoutez votre clé OpenAI dans un fichier .env dans le dossier du projet avec : OPENAI_API_KEY="<votre_clé>"
Pour utiliser l'approche HuggingFace, ajoutez la clé d'API HuggingFace dans votre fichier .env : HUGGINGFACEHUB_API_TOKEN="<votre_clé>"

Exécutez l'application : streamlit run app.py

Remarque : Assurez-vous de vérifier les exigences matérielles pour le modèle choisi en fonction de votre machine, car les embeddings et le modèle s'exécuteront localement sur votre système et seront chargés dans votre RAM.

Utilisation
Téléchargez un document PDF en utilisant la barre latérale de l'application.
Posez des questions dans l'interface principale du chat en saisissant vos questions relatives au contenu du PDF téléchargé.
Recevez des réponses générées par le chatbot en fonction des informations extraites du PDF.

![image](https://github.com/Abicakci/chat_PDF/assets/121668685/6fcffdb1-e9c2-40b1-b324-a10811050ba2)




