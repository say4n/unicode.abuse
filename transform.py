import random
import unicodedata


class Transformer:
    def __init__(self):
        self.udb = list(chr(n) for n in range(0x10FFFF))

    def __get_variant(self, character):
        return random.choice(
            list(
                filter(
                    lambda ch: unicodedata.normalize("NFKC", ch) == character, self.udb
                )
            )
        )

    def transform(self, source):
        return "".join(map(self.__get_variant, source))


if __name__ == "__main__":
    t = Transformer()
    print(t.transform("self"))
