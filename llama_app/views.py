from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model directly
tokenizer = AutoTokenizer.from_pretrained("arcee-ai/Llama-3.1-SuperNova-Lite")
model = AutoModelForCausalLM.from_pretrained("arcee-ai/Llama-3.1-SuperNova-Lite")

def generate_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        
        # Tokenize l'entrée
        inputs = tokenizer(input_text, return_tensors="pt")
        
        # Générez la sortie
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=100)
        
        # Décodez la sortie
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return render(request, 'llama_app/index.html', {'input_text': input_text, 'generated_text': generated_text})
    
    return render(request, 'llama_app/index.html')