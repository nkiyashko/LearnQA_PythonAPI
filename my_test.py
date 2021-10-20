class TestPhrase:
    def test_length_phrase(self):
        phrase = input("Пожалуйста введите фразу, не длинее 15 символов: ")
        assert len(phrase) <= 14, f"Фраза оказалась 15 символов или длиннее"
