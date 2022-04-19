import nltk as nltk


def sentence_tokenizer(text):
    """
    A method that splits text into sentences.
    :param text: string text
    :return: list of sentences
    """
    return nltk.tokenize.sent_tokenize(text)


def word_tokenizer(sent):
    """
    A method that splits text into words.
    :param sent: string sentence
    :return: list of words
    """
    return nltk.tokenize.word_tokenize(sent)


if __name__ == '__main__':
    snt = sentence_tokenizer("Hi John. Have a nice day!")
    print(snt)
    # output:   ['Hi John.', 'Have a nice day!']
    wrd = word_tokenizer("Have a nice day")
    print(wrd)
    # output:   ['Have', 'a', 'nice', 'day']
