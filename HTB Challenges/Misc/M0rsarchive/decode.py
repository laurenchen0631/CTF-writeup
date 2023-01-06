from PIL import Image
from zipfile import ZipFile

translate = {
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.-.-.-': '.',
    '--..--': ',',
    '---...': ':',
    '-.-.-.': ';',
    '..--..': '?',
    '-.-.--': '!',
    '-....-': '-',
    '..--.-': '_',
    '-.--.': '(',
    '-.--.-': ')',
    '.----.': '\'',
    '.-..-.': '\"',
    '-...-': '=',
    '.-.-.': '+',
    '-..-.': '/',
    '.--.-.': '@'
}

def morse_decode(image):
    width, height = morse_image.size
    pixel_data = morse_image.load()
    background_color = pixel_data[0,0]
    code = ""
    for line in range(height):
        morse_char = ""
        pixel_count = 0
        found = False
        for i in range(width):
            if pixel_data[i, line] != background_color:
                pixel_count += 1
                found = True
                continue
            if pixel_count == 0:
                continue
            
            if pixel_count == 1:
                morse_char += "."
                pixel_count = 0
            elif pixel_count == 3:
                morse_char += "-"
                pixel_count = 0
        
        if found:
            code += translate.get(morse_char)
    return code

for i in range(999, -1, -1):
    try:
        morse_image = Image.open('flag/pwd.png')
    except IOError:
        print("error: could not open file")
        exit()
    
    with ZipFile(f"./flag/flag_{i}.zip", "r") as zip:
        pwd = morse_decode(morse_image)
        print(i, pwd)
        zip.extractall(pwd=pwd.encode())
        