s = "κςκ ωπν αζπλ ιησι χνοςνθ μσγθσρ λσθ ζπι ιηγ δςρθι ψγρθπζ ςζ ηςθιπρω θνθψγμιγκ πδ νθςζε γζμρωψιςπζ? τγ ζγςιηγρ. κςκ ωπν αζπλ ιησι χνοςνθ μσγθσρ λσθ ψρπξσξοω δονγζι ςζ εργγα? τγ ζγςιηγρ. ς οςαγ ηπλ εργγα μησρσμιγρ οππα ιηπνεη, γυγζ ςδ ς μσζ'ι ργσκ ιηγτ. οσμιδ{ς_ενγθθ_νθςζε_τσζω_εργγα_μησρσμιγρθ_κςκζ'ι_θιπψ_ωπν._λγοο_ψοσωγκ_ς_τνθι_θσω.μπζερσιθ!}"

chars = {}
count = 0
for c in s:
    if c not in (' ', ',', '.', '?', '!', "'", '"', '{', '}', '(', ')', '[', ']', ':', ';', '-', '_', '/', '\\', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        count += 1
        chars[c] = chars.get(c, 0) + 1
        
mapping = {
    'ο': 'l',
    'σ': 'a',
    'μ': 'c',
    'ι': 't',
    'δ': 'f',
    'η': 'h', #?
    'γ': 'e' # ?
}

for c in s:
    if c in mapping:
        print(mapping[c], end='')
    else:
        print(c, end='')

letters = sorted(chars.keys(), key=lambda x: chars[x] / count, reverse=True)
# print(letters);
