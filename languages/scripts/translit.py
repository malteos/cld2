#!/usr/bin/env python3
"""Transliteration helpers used to model CHALIS-style non-standard orthography.

- sr_lat2cyr: Serbian Latin (Gaj) -> Serbian Cyrillic (1:1 standard mapping)
- cyr2lat_en: Cyrillic (ru/uk/bg/mk/sr) -> informal English-style Latin
  ("translit" as typed on the web, e.g. zh, kh, ts, ch, sh, shch, ya, yu)
- cyr2lat_cs: Cyrillic -> Czech-style Latin (ž, ch, c, č, š, šč, ja, ju)
- kk_cyr2arab: Kazakh Cyrillic -> Kazakh Arabic script (tote jazuw, simplified)
- strip_diacritics: remove combining marks (ČESKÝ -> CESKY, tiếng -> tieng)
"""
import sys
import unicodedata

_SR = {
    "lj": "љ", "nj": "њ", "dž": "џ", "Lj": "Љ", "LJ": "Љ", "Nj": "Њ", "NJ": "Њ", "Dž": "Џ", "DŽ": "Џ",
}
_SR1 = dict(zip("abvgdđežzijklmnoprstćufhcčš", "абвгдђежзијклмнопрстћуфхцчш"))
_SR1.update({k.upper(): v.upper() for k, v in list(_SR1.items())})


def sr_lat2cyr(s):
    out, i = [], 0
    while i < len(s):
        two = s[i:i + 2]
        if two in _SR:
            out.append(_SR[two]); i += 2
        else:
            out.append(_SR1.get(s[i], s[i])); i += 1
    return "".join(out)


# Common base mapping; language-specific overrides below.
_EN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "zh", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
    "щ": "shch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    # Ukrainian
    "є": "ye", "і": "i", "ї": "yi", "ґ": "g",
    # Serbian / Macedonian
    "ђ": "dj", "ј": "j", "љ": "lj", "њ": "nj", "ћ": "c", "џ": "dz", "ѓ": "gj", "ќ": "kj", "ѕ": "dz",
    "ѝ": "i", "ѐ": "e",
}
_EN_LANG = {
    "bg": {"щ": "sht", "ъ": "a", "х": "h", "ж": "zh", "ц": "ts"},
    "uk": {"г": "h", "и": "y", "х": "kh"},
    "sr": {"х": "h", "ц": "c", "ч": "c", "ш": "s", "ж": "z", "ћ": "c", "ђ": "dj"},
    "mk": {"х": "h", "ц": "c", "ж": "zh", "ш": "sh", "ч": "ch"},
}
_CS = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "jo", "ж": "ž", "з": "z",
    "и": "i", "й": "j", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "ch", "ц": "c", "ч": "č", "ш": "š",
    "щ": "šč", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "ju", "я": "ja",
}


def _map(s, table):
    out = []
    for ch in s:
        lo = ch.lower()
        if lo in table:
            r = table[lo]
            out.append(r.capitalize() if ch != lo and r else r)
        else:
            out.append(ch)
    return "".join(out)


def cyr2lat_en(s, lang="ru"):
    t = dict(_EN); t.update(_EN_LANG.get(lang, {}))
    return _map(s, t)


def cyr2lat_cs(s):
    return _map(s, _CS)


# Kazakh Cyrillic -> Arabic script (tote jazuw). Simplified: hamza (ٴ) is placed
# at word start for front-vowel words that contain no ك/گ/ە.
_KK_AR = {
    "а": "ا", "ә": "ا", "б": "ب", "в": "ۆ", "г": "گ", "ғ": "ع", "д": "د", "е": "ە", "ё": "يو",
    "ж": "ج", "з": "ز", "и": "ي", "й": "ي", "к": "ك", "қ": "ق", "л": "ل", "м": "م", "н": "ن",
    "ң": "ڭ", "о": "و", "ө": "و", "п": "پ", "р": "ر", "с": "س", "т": "ت", "у": "ۋ", "ұ": "ۇ",
    "ү": "ۇ", "ф": "ف", "х": "ح", "һ": "ھ", "ц": "تس", "ч": "چ", "ш": "ش", "щ": "شش",
    "ъ": "", "ы": "ى", "і": "ى", "ь": "", "э": "ە", "ю": "يۋ", "я": "يا",
}
_KK_FRONT = set("әөүі")


def kk_cyr2arab(text):
    words = []
    for w in text.split(" "):
        lo = w.lower()
        ar = "".join(_KK_AR.get(ch, ch) for ch in lo)
        if (set(lo) & _KK_FRONT) and not any(c in lo for c in "кгеэ") and ar and lo[0].isalpha():
            ar = "ٴ" + ar
        words.append(ar)
    return " ".join(words).replace(",", "،").replace("?", "؟")


def strip_diacritics(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))


if __name__ == "__main__":
    print(cyr2lat_en("Щастливо и хубаво", "bg"), "|", cyr2lat_cs("Москва щедрая"), "|",
          kk_cyr2arab("Қазақ тілі мен әдебиеті"), "|", strip_diacritics("Příliš žluťoučký kůň; Tiếng Việt"),
          "|", sr_lat2cyr("Ljubav i džem, đak"), file=sys.stdout)
