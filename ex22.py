import sys

sys.argv = ('exercise22.py', 'utf-8', 'strict')
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()  # Remove trailing whitespace
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("language.txt", encoding="utf-8")
main(languages, input_encoding, error)
