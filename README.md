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

Installation Pour installer et exécuter le Chatbot Langchain, suivez ces étapes :

Clonez le dépôt git clone https://github.com/Abicakci/chat_PDF.git

Créez un environnement virtuel pip install virtualenv python -m venv \Scripts\activate

Installez les dépendances à l'aide de requirements.txt pip install -r requirements.txt

Ajoutez votre clé OpenAI en créant un fichier .env dans le dossier et ajoutez ce qui suit : OPENAI_API_KEY="<votre clé>"

Pour utiliser l'approche HuggingFace, ajouter la clé d'API HuggingFace dans votre fichier .env : HUGGINGFACEHUB_API_TOKEN="<votre clé>"

Exécutez l'application streamlit run app.py

REMARQUE : Veuillez garder à l'esprit que vous devez vérifier les exigences matérielles pour le modèle que vous choisissez en fonction de votre machine, car les embeddings et le modèle s'exécuteront localement sur votre système et seront chargés dans votre RAM. Assurez-vous de faire des recherches avant d'exécuter le code avec n'importe quel modèle choisi.

Utilisation Téléchargez des documents PDF : Utilisez la barre latérale de l'application pour télécharger un ou plusieurs fichiers PDF. Posez des questions : Dans l'interface principale du chat, saisissez vos questions relatives au contenu des PDF téléchargés. Recevez des réponses : Le chatbot générera des réponses en fonction des informations extraites des PDF.

![image](https://github.com/Abicakci/chat_PDF/assets/121668685/6fcffdb1-e9c2-40b1-b324-a10811050ba2)




