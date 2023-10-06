from googletrans import Translator

print("Translating Inserted English Text into Indian Regional Languages")
while True:
    print("\nplease wait.....")
    x = input("please enter the text for translation: ")
    print("please select the regional language from given choices below:-")
    print("1) Tamil\n2) Telugu\n3) Hindi\n4) Gujarati\n5) Kannada\n6) Bengali\n7) Marathi\n8) Exit")

    n = int(input("enter the regional language number according to above data: "))
    translator = Translator()

    if n == 1:
        a = translator.translate(x, src='en', dest='ta')
        print("Translated Tamil text: ", a.text)
    if n == 2:
        b = translator.translate(x, src='en', dest='te')
        print("Translated Telugu text: ", b.text)
    if n == 3:
        c = translator.translate(x, src='en', dest='hi')
        print("Translated Hindi text: ", c.text)
    if n == 4:
        d = translator.translate(x, src='en', dest='gu')
        print("Translated Gujarati text: ", d.text)
    if n == 5:
        e = translator.translate(x, src='en', dest='kn')
        print("Translated Kannada text: ", e.text)
    if n == 6:
        f = translator.translate(x, src='en', dest='bn')
        print("Translated Bengali text: ", f.text)
    if n == 7:
        g = translator.translate(x, src='en', dest='mr')
        print("Translated Marathi text: ", g.text)
    if n == 8:
        break
    if n < 1 or n > 8:
        print("please enter valid choice")

