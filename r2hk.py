import re
import tkinter as tk
from tkinter import messagebox

# uncomment everything (except for this) for a dark theme version of the gui!

hiragana = {
    'a': 'あ',
    'i': 'い',
    'u': 'う',
    'e': 'え',
    'o': 'お',
    'ka': 'か',
    'ki': 'き',
    'ku': 'く',
    'ke': 'け',
    'ko': 'こ',
    'ga': 'が',
    'gi': 'ぎ',
    'gu': 'ぐ',
    'ge': 'げ',
    'go': 'ご',
    'sa': 'さ',
    'si': 'し',
    'su': 'す',
    'se': 'せ',
    'so': 'そ',
    'za': 'ざ',
    'zi': 'じ',
    'zu': 'ず',
    'ze': 'ぜ',
    'zo': 'ぞ',
    'chi': 'ち',
    'ta': 'た',
    'ti': 'ち',
    'tu': 'つ',
    'tsu': 'つ',
    'te': 'て',
    'to': 'と',
    'da': 'だ',
    'di': 'ぢ',
    'du': 'づ',
    'de': 'で',
    'do': 'ど',
    'na': 'な',
    'ni': 'に',
    'nu': 'ぬ',
    'ne': 'ね',
    'no': 'の',
    'ha': 'は',
    'hi': 'ひ',
    'hu': 'ふ',
    'fu': 'ふ',
    'he': 'へ',
    'ho': 'ほ',
    'ba': 'ば',
    'bi': 'び',
    'bu': 'ぶ',
    'be': 'べ',
    'bo': 'ぼ',
    'pa': 'ぱ',
    'pi': 'ぴ',
    'pu': 'ぷ',
    'pe': 'ぺ',
    'po': 'ぽ',
    'ma': 'ま',
    'mi': 'み',
    'mu': 'む',
    'me': 'め',
    'mo': 'も',
    'ya': 'や',
    'yu': 'ゆ',
    'yo': 'よ',
    'ra': 'ら',
    'ri': 'り',
    'ru': 'る',
    're': 'れ',
    'ro': 'ろ',
    'wa': 'わ',
    'wo': 'を',
    'n': 'ん',
    'tt' : 'っ',
    'vu' : 'ゔ',
    'ji' : 'じ',
    'shi': 'し',
    'sakuon': 'っ'
}

katakana = {
    'a': 'ア',
    'i': 'イ',
    'u': 'ウ',
    'e': 'エ',
    'o': 'オ',
    'ka': 'カ',
    'ki': 'キ',
    'ku': 'ク',
    'ke': 'ケ',
    'ko': 'コ',
    'ga': 'ガ',
    'gi': 'ギ',
    'gu': 'グ',
    'ge': 'ゲ',
    'go': 'ゴ',
    'sa': 'サ',
    'si': 'シ',
    'su': 'ス',
    'se': 'セ',
    'so': 'ソ',
    'za': 'ザ',
    'zi': 'ジ',
    'zu': 'ズ',
    'ze': 'ゼ',
    'zo': 'ゾ',
    'chi': 'チ',
    'ta': 'タ',
    'ti': 'チ',
    'tu': 'ツ',
    'tsu': 'ツ',
    'te': 'テ',
    'to': 'ト',
    'da': 'ダ',
    'di': 'ヂ',
    'du': 'ヅ',
    'de': 'デ',
    'do': 'ド',
    'na': 'ナ',
    'ni': 'ニ',
    'nu': 'ヌ',
    'ne': 'ネ',
    'no': 'ノ',
    'ha': 'ハ',
    'hi': 'ヒ',
    'hu': 'フ',
    'fu': 'フ',
    'he': 'ヘ',
    'ho': 'ホ',
    'ba': 'バ',
    'bi': 'ビ',
    'bu': 'ブ',
    'be': 'ベ',
    'bo': 'ボ',
    'pa': 'パ',
    'pi': 'ピ',
    'pu': 'プ',
    'pe': 'ペ',
    'po': 'ポ',
    'ma': 'マ',
    'mi': 'ミ',
    'mu': 'ム',
    'me': 'メ',
    'mo': 'モ',
    'ya': 'ヤ',
    'yu': 'ユ',
    'yo': 'ヨ',
    'ra': 'ラ',
    'ri': 'リ',
    'ru': 'ル',
    're': 'レ',
    'ro': 'ロ',
    'wa': 'ワ',
    'wo': 'ヲ',
    'n': 'ン'
}

punctuation = {
    '.':'。',
    '!': '！',
    '?': '？',
    ',': '、',
    '~': '〜',
    '-': 'ー',
    '0': '０',
    '1': '１',
    '2': '２',
    '3': '３',
    '4': '４',
    '5': '５',
    '6': '６',
    '7': '７',
    '8': '８',
    '9': '９',
    '%': '％',
    '(': '（',
    ')': '）',
}

hira_compounds = {
    'kya': 'きゃ',
    'kyu': 'きゅ',
    'kyo': 'きょ',
    'gya': 'ぎゃ',
    'gyu': 'ぎゅ',
    'gyo': 'ぎょ',
    'sha': 'しゃ',
    'shu': 'しゅ',
    'sho': 'しょ',
    'ja': 'じゃ',
    'ju': 'じゅ',
    'jo': 'じょ',
    'cha': 'ちゃ',
    'chu': 'ちゅ',
    'cho': 'ちょ',
    'jya': 'ぢゃ',
    'jyu': 'ぢゅ',
    'jyo': 'ぢょ',
    'nya': 'にゃ',
    'nyu': 'にゅ',
    'nyo': 'にょ',
    'hya': 'ひゃ',
    'hyu': 'ひゅ',
    'hyo': 'ひょ',
    'bya': 'びゃ',
    'byu': 'びゅ',
    'byo': 'びょ',
    'pya': 'ぴゃ',
    'pyu': 'ぴゅ',
    'pyo': 'ぴょ',
    'mya': 'みゃ',
    'myu': 'みゅ',
    'myo': 'みょ',
    'rya': 'りゃ',
    'ryu': 'りゅ',
    'ryo': 'りょ'
}

kata_compounds = {
    'kya': 'キャ',
    'kyu': 'キュ',
    'kyo': 'キョ',
    'gya': 'ギャ',
    'gyu': 'ギュ',
    'gyo': 'ギョ',
    'sha': 'シャ',
    'shu': 'シュ',
    'sho': 'ショ',
    'ja': 'ジャ',
    'ju': 'ジュ',
    'jo': 'ジョ',
    'cha': 'チャ',
    'chu': 'チュ',
    'cho': 'チョ',
    'jya': 'ヂャ',
    'jyu': 'ヂュ',
    'jyo': 'ヂョ',
    'nya': 'ニャ',
    'nyu': 'ニュ',
    'nyo': 'ニョ',
    'hya': 'ヒャ',
    'hyu': 'ヒュ',
    'hyo': 'ヒョ',
    'bya': 'ビャ',
    'byu': 'ビュ',
    'byo': 'ビョ',
    'pya': 'ピャ',
    'pyu': 'ピュ',
    'pyo': 'ピョ',
    'mya': 'ミャ',
    'myu': 'ミュ',
    'myo': 'ミョ',
    'rya': 'リャ',
    'ryu': 'リュ',
    'ryo': 'リョ'
}

def convert_word(word, is_katakana=False):
    if is_katakana:
        return kata_compounds.get(word, katakana.get(word, ""))
    else:
        return hira_compounds.get(word, hiragana.get(word, ""))

def r2h(input_string):
    input_string = re.sub(r'\swa\s', 'ha', input_string)

    output_string = ""
    is_katakana = False

    word_idx = 0
    while word_idx < len(input_string):
        char = input_string[word_idx]

        if char == "*":
            is_katakana = not is_katakana
            word_idx += 1
            continue

        if char in punctuation:
            output_string += punctuation[char]
            word_idx += 1
        else:
            match = re.match(r'(ky[auo]|gy[auo]|sh[auo]|j[auo]|ch[iauo]|jy[auo]|ny[auo]|hy[auo]|by[auo]|py[auo]|my[auo]|ry[auo]|shi|tsu|tu|sakuon|[kgztdnhbpmyrwvsj][aiueot]|[aiueon~.!?,-~0123456789)(]|[kgyshjcdtbnmry][yaoue]{2,3})', input_string[word_idx:])

            if match:
                word = match.group(0)
                output_string += convert_word(word, is_katakana)
                word_idx += len(word)
            else:
                word_idx += 1

    return output_string

def on_convert_button_click(event=None):
    input_text = input_entry.get() 
    if input_text:  
        result = r2h(input_text)
        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, result) 
    else:
        messagebox.showwarning("error", "no text")

root = tk.Tk()
root.title("romaji to hiragana converter")
# from awthemes import AwthemesStyle
# style = AwthemesStyle(root)
# themes = style.theme_names()
# style.theme_use("awdark")
# root.configure(bg=style.lookup("TFrame", "background"))
font_style = ('Arial', 18)

input_entry = tk.Entry(root, width=20, font=font_style)
input_entry.pack(pady=10)
input_entry.bind('<Return>', on_convert_button_click)

convert_button = tk.Button(root, text="convert", command=on_convert_button_click, font=('Arial', 12)#, bg=style.lookup("TButton", "background"), fg=style.lookup("TButton", "foreground")
)
convert_button.pack(pady=10)

result_text = tk.Text(root, height=4, width=40, wrap=tk.WORD, font=font_style)
result_text.pack(pady=10)

root.mainloop()
