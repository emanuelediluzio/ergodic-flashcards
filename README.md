<div align="center">
  <img src="logo.png" alt="Ergodic Flashcards Logo" width="200" />
  <h1>Ergodic Flashcards</h1>
  <p><em>Un sistema di Spaced Repetition (SRS) locale e autonomo, potenziato dall'IA multimodale.</em></p>
</div>

---

**Ergodic Flashcards** è un'applicazione progettata per studenti e matematici (con focus su Teoria Ergodica e materie STEM) che permette di caricare appunti matematici scritti a mano in PDF e convertirli automaticamente in **flashcards (Domanda/Risposta)** scritte in **LaTeX**. 

L'app include un motore di ripasso spaziato (basato sull'algoritmo **SuperMemo-2**) che bypassa piattaforme web chiuse (come Noji o AnkiWeb), mantenendo database e file **100% in locale sul tuo computer**, garantendo efficienza, privacy e velocità.

## ✨ Funzionalità
- **Upload PDF Multimodale**: Carica i tuoi appunti e lascia che la Vision AI di **Groq (Qwen 3.8B 27B)** legga la tua calligrafia e le formule matematiche.
- **Supporto LaTeX Nativo**: Tutte le flashcard sono generate e renderizzate perfettamente con il rendering matematico standard.
- **Study Mode Locale**: Ripassa le tue carte ogni giorno senza login o abbonamenti web.

---

## 🚀 Guida all'Installazione (Passo per Passo)

Il progetto è costruito in Python ed esegue un'app Streamlit locale. Ecco come installarlo su **Mac** e su **Windows**.

### Prerequisiti
Assicurati di aver installato:
- **Python 3.8+** (Scaricalo da python.org)
- **Poppler** (Necessario per leggere i PDF, vedi istruzioni sotto)

### 🍎 Installazione su Mac (macOS)
1. Apri il **Terminale**.
2. Installa le librerie di sistema necessarie per processare i PDF:
   ```bash
   brew install poppler
   ```
3. Clona questo repository ed entra nella cartella:
   ```bash
   git clone https://github.com/emanuelediluzio/ergodic-flashcards.git
   cd ergodic-flashcards
   ```
4. Crea un ambiente virtuale e attivalo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Installa i pacchetti Python richiesti:
   ```bash
   pip install -r requirements.txt
   ```

### 🪟 Installazione su Windows
1. Apri **PowerShell** o il **Prompt dei comandi**.
2. Scarica e installa Poppler per Windows (puoi usare [Conda](https://docs.conda.io/) con `conda install -c conda-forge poppler` oppure scaricare i binari manualmente e aggiungerli alle Variabili d'Ambiente PATH).
3. Clona questo repository ed entra nella cartella:
   ```cmd
   git clone https://github.com/emanuelediluzio/ergodic-flashcards.git
   cd ergodic-flashcards
   ```
4. Crea un ambiente virtuale e attivalo:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```
5. Installa i pacchetti Python richiesti:
   ```cmd
   pip install -r requirements.txt
   ```

---

## 🔑 Configurazione della API Key di Groq

Per funzionare, l'estrattore IA ha bisogno di chiamare il modello visivo di Groq. Attualmente, il codice è testato e impostato di default con una chiave fornita nel codice (`gsk_...`), ma è **fortemente consigliato** impostarla come Variabile d'Ambiente per sicurezza e per poterla cambiare in futuro.

**Su Mac / Linux:**
```bash
export GROQ_API_KEY="la_tua_chiave_api_gsk_..."
```

**Su Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="la_tua_chiave_api_gsk_..."
```

*(In alternativa, puoi creare un file `.env` o modificare direttamente la variabile `api_key` nel file `llm_generator.py` alla riga 9 se il progetto è solo per uso privato e non caricato pubblicamente).*

---

## ▶️ Come Avviare l'Applicazione

Una volta completati i passaggi precedenti, avvia l'app assicurandoti che l'ambiente virtuale sia attivo:

```bash
streamlit run app.py
```

Si aprirà automaticamente il tuo browser predefinito all'indirizzo `http://localhost:8501`. 

### Come si usa:
1. Vai nel menu **"Generate Flashcards"**.
2. Trascina il tuo PDF degli appunti.
3. Attendi i pochi secondi dell'estrazione (vedrai i palloncini di successo).
4. Vai nel menu **"Study"** e inizia il tuo ripasso spaziato (valutando le risposte da *0 - Blackout* a *5 - Easy*).
