class India:
    def capital(self):
        print("Capital of India is New Delhi")

    def lang(self):
        print("Hindi is widely spoken in India")

    def develop(self):
        print("India a developing country")

class Usa:
    def capital(self):
        print("Capital of USA is Washington D.C.")

    def lang(self):
        print("English is widely spoken in USA")

    def develop(self):
        print("USA a developed country")

usa=Usa()
india=India()

for country in (usa,india):
    country.capital()
    country.lang()
    country.develop()
    print()