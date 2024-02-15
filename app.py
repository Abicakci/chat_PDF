# Importation des bibliothèques nécessaires pour le fonctionnement de l'application.
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# Charge les variables d'environnement à partir du fichier .env 
load_dotenv()

# Fonction pour traiter le texte extrait du PDF.
def process_text(text):
    # Initialise un objet pour diviser le texte en morceaux, avec des paramètres spécifiques pour la taille et le chevauchement des morceaux.
    text_splitter = CharacterTextSplitter(
        separator="\n",  # Utilise un saut de ligne comme séparateur pour diviser le texte.
        chunk_size=1000,  # Taille de chaque morceau de texte.
        chunk_overlap=200,  # Nombre de caractères que les morceaux de texte peuvent se chevaucher.
        length_function=len  # Fonction utilisée pour mesurer la longueur du texte 
    )
    chunks = text_splitter.split_text(text)  # Divise le texte en morceaux.
    
    # Convertit les morceaux de texte en embeddings vectoriels pour former une base de connaissances.
    embeddings = OpenAIEmbeddings()  # Utilise OpenAI pour les embeddings.
    knowledgeBase = FAISS.from_texts(chunks, embeddings)  # Crée la base de connaissances avec FAISS.
    
    return knowledgeBase

# Fonction principale de l'application Streamlit.
def main():
    st.title("Chat avec le PDF 💬")  # Définit le titre de l'application.
    
    # Crée un champ de téléchargement de fichier pour permettre à l'utilisateur d'uploader un document PDF.
    pdf = st.file_uploader('Charger le document PDF', type='pdf')
    
    # Si un fichier PDF est uploadé :
    if pdf is not None:
        pdf_reader = PdfReader(pdf)  # Lit le fichier PDF.
        text = ""  # Initialise une variable pour stocker le texte du PDF.
        for page in pdf_reader.pages:  # Parcourt chaque page du PDF.
            text += page.extract_text()  # Extrait et ajoute le texte de la page à la variable text.
        
        # Crée l'objet base de connaissances à partir du texte du PDF.
        knowledgeBase = process_text(text)
        
        # Crée un champ pour saisir une question sur le contenu du PDF.
        query = st.text_input('Ask a question to the PDF')
        # Crée bouton pour annuler requête.
        cancel_button = st.button('Cancel')
        
        # Si l'utilisateur clique sur Annuler, arrête l'exécution de l'application.
        if cancel_button:
            st.stop()
        
        # Si une question est posée :
        if query:
            # Effectue une recherche de similitude dans la base de connaissances pour trouver les textes pertinents.
            docs = knowledgeBase.similarity_search(query)
            llm = OpenAI()  # Initialise le modèle de langage d'OpenAI.
            chain = load_qa_chain(llm, chain_type='stuff')  # Charge une chaîne de traitement pour le question-réponse.
            
            # Exécute la chaîne de traitement Question/reponse avec les documents pertinents et la question.
            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                
                
            st.write(response)  # Affiche la réponse à la question de l'utilisateur.
            
# Vérifie si le fichier est le point d'entrée 
if __name__ == "__main__":
    main()
