from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import whisper
import numpy as np
import tempfile
import os

def landing(request):
    return render(request, "landing.html")

def gestures(request):
    return render(request, "gestures.html")

def home(request):
    return render(request, "home.html")

def speech_to_text(request):
    return render(request, "speech_to_text.html")

def gesture_recognition(request):
    return render(request, "gesture_recognition.html")

def chatbot(request):
    return render(request, "chatbot.html")

def text_to_speech(request):
    return render(request, "text_to_speech.html")

def video_tutorials(request):
    return render(request, "video_tutorials.html")

def text_to_speech(request):
    return render(request, "text_to_speech.html")

@csrf_exempt
def transcribe_audio(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
    try:
        audio_file = request.FILES.get('audio')
        model_name = request.POST.get('model', 'small')
        
        if not audio_file:
            return JsonResponse({'error': 'No audio file provided'}, status=400)
        
        # Save the audio file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            for chunk in audio_file.chunks():
                temp_audio.write(chunk)
            temp_audio_path = temp_audio.name
        
        try:
            # Load Whisper model
            model = whisper.load_model(model_name)
            
            # Transcribe audio
            result = model.transcribe(temp_audio_path)
            
            # Clean up temporary file
            os.unlink(temp_audio_path)
            
            return JsonResponse({'text': result['text']})
            
        except Exception as e:
            if os.path.exists(temp_audio_path):
                os.unlink(temp_audio_path)
            raise e
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
