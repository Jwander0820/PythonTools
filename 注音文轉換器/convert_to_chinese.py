class ConvertChinese:
    def __init__(self):
        self.mapping = {
            '1': 'ㄅ', '2': 'ㄉ', '3': 'ˇ', '4': 'ˋ', '5': 'ㄓ', '6': 'ˊ', '7': '˙', '8': 'ㄚ', '9': 'ㄞ', '0': 'ㄢ', '-': 'ㄦ',
            'q': 'ㄆ', 'w': 'ㄊ', 'e': 'ㄍ', 'r': 'ㄐ', 't': 'ㄔ', 'y': 'ㄗ', 'u': 'ㄧ', 'i': 'ㄛ', 'o': 'ㄟ', 'p': 'ㄣ',
            'a': 'ㄇ', 's': 'ㄋ', 'd': 'ㄎ', 'f': 'ㄑ', 'g': 'ㄕ', 'h': 'ㄘ', 'j': 'ㄨ', 'k': 'ㄜ', 'l': 'ㄠ', ';': 'ㄤ',
            'z': 'ㄈ', 'x': 'ㄌ', 'c': 'ㄏ', 'v': 'ㄒ', 'b': 'ㄖ', 'n': 'ㄙ', 'm': 'ㄩ', ',': 'ㄝ', '.': 'ㄡ', '/': 'ㄥ'
        }

    def eng2phonetic(self, text):
        chinese_text = ''
        for char in text:
            chinese_text += self.mapping.get(char.lower(), char)
        return chinese_text


if __name__ == '__main__':
    input_str = "5k4g4u ek7hk4g4m/42k7gj bj4"  # 這是一個測試用的輸入;ㄓㄜˋㄕˋㄧ ㄍㄜ˙ㄘㄜˋㄕˋㄩㄥˋㄉㄜ˙ㄕㄨ ㄖㄨˋ
    text = ConvertChinese().eng2phonetic(input_str)
    print(text)
