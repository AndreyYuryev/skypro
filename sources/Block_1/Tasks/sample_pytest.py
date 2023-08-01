import pytest


def task_46(in_text):
    text = in_text
    just_words = text.split()
    cleaned_words = []
    for word in just_words:
      if not word.isdigit():
        cleaned_words.append(word)

    text_cleaned = " ".join(cleaned_words)
    return text_cleaned

def test_task_46():
    input_text = '734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5'
    output_text = 'мне кажется за нами следят'
    assert output_text == task_46(in_text=input_text)

text = '734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5'
print(task_46(text))