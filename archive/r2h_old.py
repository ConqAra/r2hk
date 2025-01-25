import re
import sys

hiragana = {
    'a' : 'あ',
    'i' : "い",
    'u' : "う",
    'e' : "え",
    'o' : "お",
    'ka' : 'か',
    'ki' : 'き',
    'ku' : 'く',
    'ke' : 'け',
    'ko' : 'こ',
    'ga' : 'が',
    'gi' : 'ぎ',
    'gu' : 'ぐ',
    'ge' : 'げ',
    'go' : 'ご',
    'sa' : 'さ',
    'si' : 'し',
    'su' : 'す',
    'se' : 'せ',
    'so' : 'そ',
    'za' : 'ざ',
    'zi' : 'じ',
    'zu' : 'ず',
    'ze' : 'ぜ',
    'zo' : 'ぞ',
    'ta' : 'た',
    'ti' : 'ち',
    'tu' : 'つ',
    'tsu' : 'つ',
    'te' : 'て',
    'to' : 'と',
    'da' : 'だ',
    'di' : 'ぢ',
    'du' : 'づ',
    'de' : 'で',
    'do' : 'ど',
    'na' : 'な',
    'ni' : 'に',
    'nu' : 'ぬ',
    'ne' : 'ね',
    'no' : 'の',
    'ha' : 'は',
    'hi' : 'ひ',
    'hu' : 'ふ',
    'fu' : 'ふ',
    'he' : 'へ',
    'ho' : 'ほ',
    'ba' : 'ば',
    'bi' : 'び',
    'bu' : 'ぶ',
    'be' : 'べ',
    'bo' : 'ぼ',
    'pa' : 'ぱ',
    'pi' : 'ぴ',
    'pu' : 'ぷ',
    'pe' : 'ぺ',
    'po' : 'ぽ',
    'ma' : 'ま',
    'mi' : 'み',
    'mu' : 'む',
    'me' : 'め',
    'mo' : 'も',
    'ya' : 'や',
    'yu' : 'ゆ',
    'yo' : 'よ',
    'ra' : 'ら',
    'ri' : 'り',
    'ru' : 'る',
    're' : 'れ',
    'ro' : 'ろ',
    'wa' : 'わ',
    'wo' : 'を'
}

def main():
    input_string = input("convert:")
  
    input_string_words = list()
    print(input_string_words)

    constant = ['k', 'g', 's', 'z', 't', 'd', 'n', 'h', 'b', 'p', 'm', 'y', 'r', 'w']

    word_list = re.findall(r'[kgsztdnhbpmyrw][aeiou]|[aeiou]', input_string)

    max_len = 0
    for word in word_list:
        max_len += len(word)
        
    if max_len != len(input_string):
        sys.exit("error")

    output_string = ""

    for word in word_list:
        output_string += hiragana[word]

    print(output_string)

main()