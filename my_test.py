class TestPhrase:
    def test_length_phrase(self):
        print("Пожалуйста введите фразу, не длинее 15 символов")
        phrase = input("Set a phrase: ")
        assert len(phrase) <= 14
