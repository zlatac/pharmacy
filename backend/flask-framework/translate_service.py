from enum import Enum, IntEnum
import json

with open('data.json', 'r', encoding="utf-8") as file:
    raw_data = file.read()
    sig_code_translations = json.loads(raw_data)

sample_prescription: str = 'i-ii tble ou b.d.s. '

class Category(IntEnum):
    # order gotten from https://d20ohkaloyme4g.cloudfront.net/img/document_thumbnails/0f4e58c50e65b6643b78d89ff80cf57b/thumb_1200_1553.png
    VERB = 1 # instruction to patient
    QUANTITY = 2 # amount given to patient
    FORM = 3 # how the medication comes
    ROUTE = 4 # how the medication will go into the body
    FREQUENCY = 5 # how often the medication is taken
    DURATION = 6 # how long patient is on the medication
    DIAGNOSIS =  7 # what the medication is used for


roman_numerals = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, }

translation_keys = {}

for (key, val) in sig_code_translations.items():
    translation_keys[key] = key
    if 'similar' in val:
        for similar_code in val['similar']:
            translation_keys[similar_code] = key


extracted_keys = list(translation_keys.keys())
roman_numeral_keys = list(roman_numerals.keys())
all_prescription_keys = extracted_keys + roman_numeral_keys


def decipher_prescription(codes_to_translate: str) -> dict:

    output_map: list[dict[str, int | str | list]] = []
    result_string_map: list[str] = []
    code_table = {}

    for code in codes_to_translate.lower().split(' '):
        if code in translation_keys:
            output_map.append(sig_code_translations[translation_keys[code]])
            code_table[code] = sig_code_translations[translation_keys[code]]
        if code in roman_numerals:
            numeral_values = {'translation': roman_numerals[code], 'category': Category.QUANTITY.name}
            output_map.append(numeral_values)
            code_table[code] = numeral_values

    output_map.sort(key = lambda item: Category[item['category']])

    for item in output_map:
        result_string_map.append(str(item['translation']))

    if len(result_string_map) > 0:
        return {'fullTranslation': ', '.join(result_string_map), 'table': code_table}
    else:
        return {}

# print(decipher_prescription(sample_prescription))