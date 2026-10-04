import os
import json
import base64
from typing import List, Dict

def extract_flashcards_from_pdf(pdf_path: str) -> List[Dict[str, str]]:
    """
    Extracts Flashcards from a handwritten PDF using Groq's Vision API.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    
    try:
        from pdf2image import convert_from_path
        from groq import Groq
        import io
        
        client = Groq(api_key=api_key)
        images = convert_from_path(pdf_path)
        
        system_prompt = """You are an expert mathematician. Extract flashcards from these handwritten notes on Ergodic Theory. 
Format the output as a JSON object containing an array named "flashcards", where each object has a 'question' and an 'answer'.
Use LaTeX formatting for any mathematical symbols and equations. Ensure the LaTeX uses standard math delimiters like $ and $$.
Return ONLY valid JSON."""

        # Convert first image for simplicity
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()
        base64_image = base64.b64encode(img_bytes).decode('utf-8')

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": system_prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                    ]
                }
            ],
            model="qwen/qwen3.8-27b",
            response_format={"type": "json_object"}
        )
        
        result_json = chat_completion.choices[0].message.content
        data = json.loads(result_json)
        
        # It should return {"flashcards": [...]}
        if "flashcards" in data:
            return data["flashcards"]
        elif isinstance(data, list):
            return data
        else:
            return []
        
    except Exception as e:
        print(f"Error during extraction: {e}")
        return []
