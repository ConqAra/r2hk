import re
import tkinter as tk
from tkinter import messagebox
from awthemes import AwthemesStyle

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
    'chi': 'た',
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
    'tt' : 'っ',
    'vu' : 'ゔ',
    'ji' : 'じ',
    'shi': 'し'
}

compounds = {
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

def r2h(input_string):
    input_string = input_string.lower().replace(" ", "")

    for compound, hiragana_char in compounds.items():
        input_string = input_string.replace(compound, compound[0] + compound[1:].lower())

    word_list = re.findall(r'(ky[auo]|gy[auo]|sh[auo]|j[auo]|ch[iauo]|jy[auo]|ny[auo]|hy[auo]|by[auo]|py[auo]|my[auo]|ry[auo]|shi|tsu|tu|[kgztdnhbpmyrwvsj][aiueot]|[aiueon~.!?,-~0123456789)(]|[kgyshjcdtbnmry][yaoue]{2,3})', input_string)
    
    max_len = sum(len(word) for word in word_list)
    if max_len != len(input_string):
        messagebox.showerror("error", "invalid input string!")
        return ""

    output_string = ""
    
    for word in word_list:
        if word == 'tsu' or word == 'tu':
            output_string += hiragana['tsu']
        elif word in compounds:
            output_string += compounds[word]
        else:
            output_string += hiragana.get(word, "")
    
    return output_string

def on_convert_button_click(event=None):
    input_text = input_entry.get() 
    if input_text:  
        result = r2h(input_text)
        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, result) 
    else:
        messagebox.showwarning("error", "no text")

# gui, uncomment for dark theme
root = tk.Tk()
root.title("romanji to hiragana converter")
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
