from utils import BasicWord, Player, load_random_word


URL_JSON = 'https://jsonkeeper.com/b/LJHI'
def main():
    word = load_random_word(URL_JSON)
    if word is None:
        print("Слово не загрузилось")
        return


if __name__ == '__main__':
    main()
