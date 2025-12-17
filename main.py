import pyttsx3
import sys
import os

def text_to_speech_from_file(file_path: str, output_path: str = None):
    if not os.path.isfile(file_path):
        print(f"Файл '{file_path}' не найден.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    if not text:
        print("Файл пуст.")
        return

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if 'ru' in voice.languages or 'russian' in voice.name.lower() or 'ру' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        print("Русский голос не найден — используется голос по умолчанию.")

    engine.setProperty('rate', 180)   # скорость речи (~150–200)
    engine.setProperty('volume', 1.0) # громкость (0.0–1.0)

    if output_path:
        print(f"Озвучиваю текст и сохраняю в '{output_path}'...")
        try:
            engine.save_to_file(text, output_path)
            engine.runAndWait()
            print(f"Успешно сохранено в '{output_path}'")
        except Exception as e:
            print(f"Ошибка при сохранении аудио: {e}")
    else:
        print("Воспроизведение текста...")
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.wav"

    text_to_speech_from_file(input_file, output_file)