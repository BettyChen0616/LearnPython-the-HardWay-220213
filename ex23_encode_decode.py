import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() #e stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages, input_encoding, error)

'''
Decode Bytes, Encode Strings
b'\xe4\xb8\xad\xe6\x96\x87'.decode() => '中文'
'中文'.encode() => b'\xe4\xb8\xad\xe6\x96\x87'

b'T\xc3\xbcrk\xc3\xa7e' <===> Türkçe # b'' => byte string
b'\xd0\xa3\xd0\xba\xd1\x80\xd0\xb0\xd1\x97\xd0\xbd\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0' <===> Українська
b'\xd8\xa7\xd8\xb1\xd8\xaf\xd9\x88' <===> اردو
b'Ti\xe1\xba\xbfng Vi\xe1\xbb\x87t' <===> Tiếng Việt
b'V\xc3\xb5ro' <===> Võro
b'\xe6\x96\x87\xe8\xa8\x80' <===> 文言
b'\xe5\x90\xb4\xe8\xaf\xad' <===> 吴语
b'\xd7\x99\xd7\x99\xd6\xb4\xd7\x93\xd7\x99\xd7\xa9' <===> ייִדיש
b'\xe4\xb8\xad\xe6\x96\x87' <===> 中文

(base) % python3.8
>>> 0b1011010
90
>>> ord('Z')
90
>>> chr(90)
'Z'
>>> quit()
'''
