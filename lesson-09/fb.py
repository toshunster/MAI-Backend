from faker import Faker

def main():
    fake = Faker(locale="Ru_ru")
    for i in range(10):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'sentence': fake.sentence(),
            'text': fake.text()
        }
        print(doc)

    print(fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    print(fake.text(max_nb_chars=200, ext_word_list=None))

if __name__ == "__main__":
    main()
