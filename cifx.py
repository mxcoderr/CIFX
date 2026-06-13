class Alphabet:
    @staticmethod
    def parse(text: str):
        if '-' not in text:
            return None

        left, right = map(str.strip, text.split('-', 1))

        if not left or not right:
            return None

        return left, right

    def __init__(self, text: str):
        self.characters = self.parse(text)


class Coder:
    def __init__(self, alphabet: Alphabet):
        if not alphabet or not alphabet.characters:
            raise ValueError("Invalid alphabet format")

        self.src, self.dst = alphabet.characters

    def encode(self, text: str) -> str:
        """Заменяет src → dst"""
        return text.replace(self.src, self.dst)

    def decode(self, text: str) -> str:
        """Заменяет dst → src"""
        return text.replace(self.dst, self.src)


class CIFX:
    def alphabet(self, text: str):
        return Alphabet(text)

    def coder(self, alphabet: Alphabet):
        return Coder(alphabet)

    def imode(self, coder: Coder, input_text=">>> "):
        while True:
            target = input(input_text)

            choice = input("1=Encode | 2=Decode | q=Quit: ").strip()

            if choice == "1":
                print(coder.encode(target))

            elif choice == "2":
                print(coder.decode(target))

            elif choice in ("q", "quit"):
                break

            else:
                print("Invalid option")


# example usage:   
# cifx = CIFX()
# ab = cifx.alphabet("в - л")
# coder = cifx.coder(ab)
# cifx.imode(coder)
    
