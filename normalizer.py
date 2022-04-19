# Firtly, install this package
# pip install git+https://github.com/emres/turkish-deasciifier.git

from turkish.deasciifier import Deasciifier
import re


def asciify(text):
    """
    A method that fixes character according to English alphabet
    :param text: string text
    :return: fixed text
    """
    return text.replace("ı", 'i').replace('ü', 'u').replace('ö', 'o').replace('ş', 's').replace('ğ', 'g').replace('ç',
                                                                                                                  'c')


def deasciify(text):
    """
    A method that fixes character according to Turkish alphabet
    :param text: string text
    :return: fixed text
    """
    deasciified_text = Deasciifier(text)
    return deasciified_text.convert_to_turkish()


def rm_irrelevant_chars(text):
    """
    A method that removes irrelevant characters from text
    :param text: string text that includes irrelevant characters
    :return: cleaned text
    """
    text = re.sub('[0-9]|/|,|"|\'|;|\.|\?|:|\-|\*|\%|\+|\$|\<|\>|\|\@|\#|\^|\%|\{|\}|\=|\¾|\[|\]|\½|\£|\&|\|', "",
                  text).replace("\n", " ")
    return text


if __name__ == '__main__':
    a = asciify("Bugün güneşli bir gün.")
    print(a)
    # output:   Bugun gunesli bir gun.
    d = deasciify("Bugun guneslı bır gun.")
    print(d)
    # output:   Bugün güneşli bir gün.
    rm = rm_irrelevant_chars("Bu%g+ün ^gu'neş>li |b?ir g£#ün")
    print(rm)
    # output:   Bugün guneşli bir gün
    