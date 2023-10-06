from googletrans import Translator

def translate_text(src_lang, dest_lang, text):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

print("Translating Inserted English Text into Indian Regional Languages")

while True:
    print("\nPlease wait.....")
    x = input("Please enter the text for translation: ")

    print("Please select the regional language from the given choices below:")
    print("1) Tamil\n2) Telugu\n3) Hindi\n4) Gujarati\n5) Kannada\n6) Bengali\n7) Marathi\n8) Exit")

    n = int(input("Enter the regional language number according to the above data: "))

    if 1 <= n <= 7:
        languages = ['ta', 'te', 'hi', 'gu', 'kn', 'bn', 'mr']
        translated_text = translate_text('en', languages[n-1], x)
        print(f"Translated text: {translated_text}")
    elif n == 8:
        break
    else:
        print("Please enter a valid choice.")

