# Ergodic Flashcards Agent Plan

## 1. Analisi Temporale e Riepilogo degli Audio
Gli audio inviati da Matteo sono stati analizzati in ordine cronologico basandosi sui metadati (timestamp):

1. **Audio 1 (14:42): L'Idea Iniziale**
   Matteo sta studiando teoria ergodica (matematica pura) su appunti scritti a mano (PDF). L'idea era di usare Claude o un'API per estrarre il contenuto, generare domande per flashcard in formato LaTeX e caricarle in automatico su un sito web esterno chiamato "Noji". Il problema principale menzionato è l'autenticazione/login sul sito.
   
2. **Audio 2 (15:57): La Motivazione e l'Efficienza**
   Matteo riflette sul tempo risparmiato (circa 2 ore al giorno). Ribadisce che servirebbe fare chiamate API (forse Enterprise) per bypassare il login manuale su Noji. L'obiettivo è automatizzare il passaggio: appunti manoscritti -> flashcard LaTeX -> salvataggio e caricamento.

3. **Audio 3 (17:57): Il Ripensamento (La Soluzione)**
   C'è un cambio di direzione. Rendendosi conto delle limitazioni di interfacciarsi con il sito web chiuso di Noji, Matteo propone di creare direttamente un'**applicazione locale** (o web app personale) che integri sia l'estrazione intelligente (da PDF a flashcard in LaTeX) sia l'algoritmo di Spaced Repetition (SRS), bypassando del tutto Noji.

## 2. Il Piano (Well-Structured Plan)
Alla luce dell'ultimo audio, il piano è sviluppare un'applicazione completa stand-alone chiamata **Ergodic Flashcards** che farà da "Noji privato" potenziato dall'AI.

### Funzionalità Core:
1. **Generatore di Flashcard (LLM-based)**:
   - Input: un file PDF di appunti manoscritti.
   - Processo: conversione del PDF in immagini, da passare a un modello multimodale (es. Gemini, GPT-4o o Claude) per l'estrazione intelligente del testo.
   - Output: generazione strutturata di Q&A in formato LaTeX (JSON).
2. **Spaced Repetition System (SRS)**:
   - Implementazione dell'algoritmo SM-2 (standard di settore, come Anki) per gestire le revisioni giornaliere.
   - Salvataggio locale in un database leggero (SQLite o file JSON locale).
3. **Interfaccia Utente (Web UI)**:
   - Utilizzo di `Streamlit` (ideale per il rendering nativo di LaTeX e per creare interfacce in Python velocemente).
   - Modalità "Genera" (Upload PDF -> Estrazione).
   - Modalità "Studio" (Visualizzazione Flashcard, rendering equazioni, pulsanti per lo scoring e lo scheduling).

### Tecnologie Scelte (dopo ricerca online e GitHub):
- **Algoritmo SRS**: SM-2 o librerie minime come `simple-spaced-repetition`. Lo scriveremo da zero per maggiore flessibilità e assenza di dipendenze complesse.
- **LLM**: Utilizzeremo il tool multimodale per analizzare immagini/PDF ed estrarre le flashcard in LaTeX.
- **Frontend/App**: `Streamlit` (renderizza bene il LaTeX con `st.latex` e `st.markdown`).
- **PDF Processing**: `pdf2image` o librerie simili.

## 3. Architettura del Progetto
La directory `/Users/emanuelediluzio/repos/ergodic-flashcards` conterrà:
- `app.py`: L'applicazione Streamlit principale.
- `srs_engine.py`: La logica per lo Spaced Repetition (Algoritmo SM-2).
- `llm_generator.py`: La logica di prompt e comunicazione con il modello per processare il PDF.
- `db.json`: File per salvare il progresso delle flashcard.
- `requirements.txt`: Le dipendenze (streamlit, pdf2image, google-genai, ecc.).

## 4. Esecuzione
Vado in modalità `/goal`, creo i file necessari, li testo e configuro tutto fino ad ottenere un'app funzionante.
