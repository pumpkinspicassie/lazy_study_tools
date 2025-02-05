import pyttsx3
import PyPDF2
from googletrans import Translator

from PyPDF2 import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
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
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha' if lang == 'en' else 'com.apple.speech.synthesis.voice.ting-ting')
    engine.say(text)
    engine.runAndWait()

def main(pdf_path):
    translator = Translator()
    text = read_pdf(pdf_path)
    chunks = split_text_by_periods(text)
    for chunk in chunks:
        text_to_speech(chunk, 'en')
        translated = translator.translate(chunk, src='en', dest='zh-CN').text
        text_to_speech(translated, 'zh-CN')
if __name__ == "__main__":
    pdf_path = '/Users/cassielu/Documents/course/computational_game_theory/CGT_notes_24_v2 - Copy.pdf'  # 替换为你的PDF文件路径
    main(pdf_path)
