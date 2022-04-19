from snowballstemmer import TurkishStemmer


def snowball_stemmer(text):
    """
    A method that gets stem of the word
    :param text: string text
    :return: stems of the words in the text
    """
    result = ""
    turkStem = TurkishStemmer()
    for word in text.split():
        result += turkStem.stemWord(word) + " "
    return result.strip()


if __name__ == '__main__':
    stem = snowball_stemmer("geldim")
    print(stem)
    # output:   gel
