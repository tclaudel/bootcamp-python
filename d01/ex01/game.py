class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        assert first_name and isinstance(first_name, str), "please give me a first name"
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"





