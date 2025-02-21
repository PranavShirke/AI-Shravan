#! python3.7

import argparse
import os
import numpy as np
import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta
from collections import deque
from time import sleep
from sys import platform


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="small", help="Model to use",
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--non_english", action='store_true',
                        help="Don't use the English model.")
    parser.add_argument("--energy_threshold", default=1000, type=int,
                        help="Energy level for mic detection.")
    parser.add_argument("--record_timeout", default=1.5, type=float,
                        help="Recording interval in seconds.")
    parser.add_argument("--phrase_timeout", default=2, type=float,
                        help="Silence duration before starting a new line.")
    
    if 'linux' in platform:
        parser.add_argument("--default_microphone", default='pulse', type=str,
                            help="Default microphone. Use 'list' to view options.")

    args = parser.parse_args()

    # Set up variables
    phrase_time = None
    data_queue = deque()
    transcription = []
    
    recorder = sr.Recognizer()
    recorder.energy_threshold = args.energy_threshold
    recorder.dynamic_energy_threshold = False

    # Selecting Microphone
    mic = None
    if 'linux' in platform:
        mic_name = args.default_microphone
        if mic_name == 'list':
            print("Available microphone devices:")
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                print(f"{index}: {name}")
            return
        else:
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                if mic_name in name:
                    mic = sr.Microphone(sample_rate=16000, device_index=index)
                    break
    if mic is None:
        mic = sr.Microphone(sample_rate=16000)

    # Load Whisper Model
    model_name = args.model if args.non_english else f"{args.model}.en"
    audio_model = whisper.load_model(args.model)


    record_timeout = args.record_timeout
    phrase_timeout = args.phrase_timeout

    with mic:
        recorder.adjust_for_ambient_noise(mic)

    def record_callback(_, audio: sr.AudioData):
        """Threaded callback to handle audio recording"""
        data_queue.append(audio.get_raw_data())

    recorder.listen_in_background(mic, record_callback, phrase_time_limit=record_timeout)
    print("Model loaded.\nListening...")

    while True:
        try:
            now = datetime.utcnow()

            if data_queue:
                phrase_complete = False
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    phrase_complete = True
                phrase_time = now

                # Process audio
                audio_data = b''.join(data_queue)
                data_queue.clear()

                audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

                result = audio_model.transcribe(audio_np)
                text = result['text'].strip()

                if phrase_complete:
                    transcription.append(text)
                elif transcription:
                    transcription[-1] = text
                else:
                    transcription.append(text)

                # Print transcription without clearing screen
                print("\n".join(transcription), flush=True)

                # Free memory
                del audio_np, audio_data

            else:
                sleep(0.3)

        except KeyboardInterrupt:
            break

    print("\nFinal Transcription:")
    print("\n".join(transcription))


if __name__ == "__main__":
    main()
