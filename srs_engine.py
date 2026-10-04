import json
import os
from datetime import datetime, timedelta

DB_FILE = 'flashcards.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def sm2(quality, repetitions, easiness, interval):
    """
    SuperMemo-2 algorithm.
    quality: 0-5
      5 - perfect response
      4 - correct response after a hesitation
      3 - correct response recalled with serious difficulty
      2 - incorrect response; where the correct one seemed easy to recall
      1 - incorrect response; the correct one remembered
      0 - complete blackout
    """
    if quality >= 3:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = round(interval * easiness)
        repetitions += 1
    else:
        repetitions = 0
        interval = 1
    
    easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    if easiness < 1.3:
        easiness = 1.3
        
    return repetitions, easiness, interval

def add_flashcard(question, answer):
    db = load_db()
    card = {
        'id': len(db) + 1,
        'question': question,
        'answer': answer,
        'repetitions': 0,
        'easiness': 2.5,
        'interval': 0,
        'next_review': datetime.now().isoformat()
    }
    db.append(card)
    save_db(db)

def add_multiple_flashcards(cards):
    db = load_db()
    for card_data in cards:
        card = {
            'id': len(db) + 1,
            'question': card_data.get('question', ''),
            'answer': card_data.get('answer', ''),
            'repetitions': 0,
            'easiness': 2.5,
            'interval': 0,
            'next_review': datetime.now().isoformat()
        }
        db.append(card)
    save_db(db)

def get_due_cards():
    db = load_db()
    now = datetime.now()
    due_cards = []
    for card in db:
        if datetime.fromisoformat(card['next_review']) <= now:
            due_cards.append(card)
    return due_cards

def update_card(card_id, quality):
    db = load_db()
    for card in db:
        if card['id'] == card_id:
            rep, ease, interval = sm2(quality, card['repetitions'], card['easiness'], card['interval'])
            card['repetitions'] = rep
            card['easiness'] = ease
            card['interval'] = interval
            next_date = datetime.now() + timedelta(days=interval)
            card['next_review'] = next_date.isoformat()
            break
    save_db(db)
