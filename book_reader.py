import pyttsx3
from PyPDF2 import PdfReader
from googletrans import Translator
import argparse

def read_pdf(file_path, start_page, end_page):
    reader = PdfReader(file_path)
    text = ""
    for i in range(start_page - 1, end_page):
        if i < len(reader.pages):
            text += reader.pages[i+1].extract_text()
    return text

def split_text_by_periods(text, period_count=5):
    sentences = text.split('.')
    chunks = []
    for i in range(0, len(sentences), period_count):
        chunk = '.'.join(sentences[i:i + period_count]) + '.'
        chunks.append(chunk)
    return chunks

def text_to_speech(text, lang='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    if lang == 'en':
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    else:
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.ting-ting')
    engine.say(text)
    engine.runAndWait()

def main(pdf_path, start_page, end_page):
    translator = Translator()
    text = read_pdf(pdf_path, start_page, end_page)
    chunks = split_text_by_periods(text)
    for chunk in chunks:
        text_to_speech(chunk, 'en')
        translated = translator.translate(chunk, src='en', dest='zh-CN').text
        text_to_speech(translated, 'zh-CN')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read and translate PDF text.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument("start_page", type=int, help="Start page number.")
    parser.add_argument("end_page", type=int, help="End page number.")
    args = parser.parse_args()
    main(args.pdf_path, args.start_page, args.end_page)
