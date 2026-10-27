from translate_service import Category

breakdown_backup = {
    "pc": {
        "translation": "after meals",
        "category": Category.VERB,
    },
    "pchs": {
        "translation": "after meals and at bedtime",
        "category": Category.VERB,
        "similar": ["pc&hs"]
    },
    "au": {
        "translation": "in each ear",
        "category": Category.ROUTE
    },
    "apl": {
        "translation": "applicatorful",
        "category": Category.FORM
    },
    "ou": {
        "translation": "in each eye",
        "category": Category.ROUTE
    },
    "app": {
        "translation": "apply",
        "category": Category.VERB
    },
    "ien": {
        "translation": "in each nostril",
        "category": Category.ROUTE
    },
    "ar": {
        "translation": "arthritis",
        "category": Category.DIAGNOSIS
    },
    "al": {
        "translation": "in the left ear",
        "category": Category.ROUTE
    },
    "ud": {
        "translation": "as directed",
        "category": Category.VERB
    },
    "ad": {
        "translation": "in the right ear",
        "category": Category.ROUTE
    },
    "hs": {
        "translation": "at bedtime",
        "category": Category.FREQUENCY
    },
    "os": {
        "translation": "in the left eye",
        "category": Category.ROUTE
    },
    "stat": {
        "translation": "at once",
        "category": Category.FREQUENCY
    },
    "od": {
        "translation": "in the right eye",
        "category": Category.ROUTE
    },
    "inf": {
        "translation": "inflammation",
        "category": Category.DIAGNOSIS
    },
    "bp": {
        "translation": "blood pressure",
        "category": Category.DIAGNOSIS
    },
    "inh": {
        "translation": "inhale",
        "category": Category.VERB
    },
    "ac": {
        "translation": "before meals",
        "category": Category.FREQUENCY
    },
    "achs": {
        "translation": "before meals and at bedtime",
        "category": Category.FREQUENCY,
        "similar": ["ac&hs"]
    },
    "inj": {
        "translation": "inject",
        "category": Category.VERB,
        "similar": ["ij"]
    },
    "bm": {
        "translation": "bowel movement",
        "category": Category.DIAGNOSIS
    },
    "medap": {
        "translation": "injection administered by pharmacist",
        "category": Category.VERB
    },
    "po": {
        "translation": "by mouth",
        "category": Category.ROUTE
    },
    "ir": {
        "translation": "insert",
        "category": Category.VERB
    },
    "ins": {
        "translation": "instil",
        "category": Category.VERB
    },
    "r": {
        "translation": "into the rectum",
        "category": Category.ROUTE
    },
    "cap": {
        "translation": "capsule",
        "category": Category.FORM,
        "similar": ["caps"]
    },
    "pv": {
        "translation": "into the vagina",
        "category": Category.ROUTE
    },
    "ci": {
        "translation": "circulation",
        "category": Category.DIAGNOSIS
    },
    "ju": {
        "translation": "juice",
        "category": Category.FORM
    },
    "con": {
        "translation": "constipation",
        "category": Category.DIAGNOSIS
    },
    "medcp": {
        "translation": "consultation provided by",
        "category": Category.VERB
    },
    "n": {
        "translation": "night",
        "category": Category.FREQUENCY
    },
    "cr": {
        "translation": "crush",
        "category": Category.VERB
    },
    "crm": {
        "translation": "cream",
        "category": Category.FORM
    },
    "ss": {
        "translation": "one half",
        "category": Category.QUANTITY
    },
    "dy": {
        "translation": "daily",
        "category": Category.FREQUENCY
    },
    "qbid": {
        "translation": "one or two times daily",
        "category": Category.FREQUENCY
    },
    "d": {
        "translation": "day",
        "category": Category.FREQUENCY
    },
    "ds": {
        "translation": "days",
        "category": Category.FREQUENCY
    },
    "pa": {
        "translation": "pain",
        "category": Category.DIAGNOSIS
    },
    "di": {
        "translation": "diarrhea",
        "category": Category.DIAGNOSIS
    },
    "pl": {
        "translation": "place",
        "category": Category.VERB
    },
    "dr": {
        "translation": "drink",
        "category": Category.VERB
    },
    "pf": {
        "translation": "puffs",
        "category": Category.VERB
    },
    "gtt": {
        "translation": "drop",
        "category": Category.FORM
    },
    "gtts": {
        "translation": "drops",
        "category": Category.FORM
    },
    "ra": {
        "translation": "rash",
        "category": Category.DIAGNOSIS
    },
    "medra": {
        "translation": "refer to adaptation form",
        "category": Category.VERB
    },
    "qd": {
        "translation": "each day",
        "category": Category.FREQUENCY,
        "similar": ["q1d"]
    },
    "medro": {
        "translation": "refer to opinions form",
        "category": Category.VERB
    },
    "qpm": {
        "translation": "each evening",
        "category": Category.FREQUENCY
    },
    "qam": {
        "translation": "each morning",
        "category": Category.FREQUENCY
    },
    "sw": {
        "translation": "shake well",
        "category": Category.VERB
    },
    "q": {
        "translation": "every",
        "category": Category.FREQUENCY
    },
    "sb": {
        "translation": "shortness of breath",
        "category": Category.DIAGNOSIS
    },
    "q1h": {
        "translation": "every hour",
        "category": Category.FREQUENCY,
        "similar": ["q1"]
    },
    "sp": {
        "translation": "sparingly",
        "category": Category.VERB
    },
    "q2d": {
        "translation": "every second day",
        "category": Category.FREQUENCY
    },
    "supp": {
        "translation": "suppository",
        "category": Category.FORM
    },
    "q2h": {
        "translation": "every 2 hours",
        "category": Category.FREQUENCY
    },
    "q3h": {
        "translation": "every 3 hours",
        "category": Category.FREQUENCY
    },
    "tbl": {
        "translation": "tablespoon",
        "category": Category.QUANTITY
    },
    "q4h": {
        "translation": "every 4 hours",
        "category": Category.FREQUENCY
    },
    "tbls": {
        "translation": "tablespoonfuls",
        "category": Category.QUANTITY
    },
    "q6h": {
        "translation": "every 6 hours",
        "category": Category.FREQUENCY
    },
    "tab": {
        "translation": "tablet",
        "category": Category.FORM
    },
    "q8h": {
        "translation": "every 8 hours",
        "category": Category.FREQUENCY
    },
    "tabs": {
        "translation": "tablets",
        "category": Category.FORM
    },
    "q12h": {
        "translation": "every 12 hours",
        "category": Category.FREQUENCY
    },
    "t": {
        "translation": "take",
        "category": Category.VERB
    },
    "q2-3h": {
        "translation": "every 2-3 hours",
        "category": Category.FREQUENCY
    },
    "tsp": {
        "translation": "teaspoon",
        "category": Category.QUANTITY
    },
    "q2-4h": {
        "translation": "every 2-4 hours",
        "category": Category.FREQUENCY
    },
    "tsps": {
        "translation": "teaspoonfuls",
        "category": Category.QUANTITY
    },
    "q4-6h": {
        "translation": "every 4-6 hours",
        "category": Category.FREQUENCY
    },
    "tqid": {
        "translation": "three or four times daily",
        "category": Category.FREQUENCY
    },
    "tid": {
        "translation": "three times daily",
        "category": Category.FREQUENCY
    },
    "fe": {
        "translation": "fever",
        "category": Category.DIAGNOSIS
    },
    "btid": {
        "translation": "two or three times daily",
        "category": Category.FREQUENCY
    },
    "fl": {
        "translation": "fluids",
        "category": Category.FORM,
        "similar": ["fld"]
    },
    "admx": {
        "translation": "to a maximum of",
        "category": Category.QUANTITY
    },
    "f": {
        "translation": "for",
        "category": Category.DIAGNOSIS
    },
    "aa": {
        "translation": "to affected area",
        "category": Category.ROUTE
    },
    "qid": {
        "translation": "four times daily",
        "category": Category.FREQUENCY
    },
    "bid": {
        "translation": "twice daily",
        "category": Category.FREQUENCY
    },
    "g": {
        "translation": "give",
        "category": Category.VERB
    },
    "sl": {
        "translation": "under the tongue",
        "category": Category.ROUTE
    },
    "uf": {
        "translation": "until finished",
        "category": Category.DURATION
    },
    "hd": {
        "translation": "headache",
        "category": Category.DIAGNOSIS
    },
    "aq": {
        "translation": "water",
        "category": Category.FORM
    },
    "h": {
        "translation": "hour",
        "category": Category.FREQUENCY,
        "similar": ["hr","hor"]
    },
    "prn": {
        "translation": "as needed",
        "category": Category.DURATION
    },
    "hrs": {
        "translation": "hours",
        "category": Category.FREQUENCY,
    },
    "prnf": {
        "translation": "when necessary for",
        "category": Category.DURATION
    },
    "c": {
        "translation": "with",
        "category": Category.VERB
    },
    "cf": {
        "translation": "with food",
        "category": Category.VERB
    },
    "cc": {
        "translation": "with meals",
        "category": Category.VERB
    },
    "s": {
        "translation": "without",
        "category": Category.VERB
    },
    "i-ii": {
        "translation": "1 to 2",
        "category": Category.QUANTITY
    },
    "mcg": {
        "translation": "Microgram",
        "category": Category.QUANTITY,
        "similar": ["μg"]
    },
    "mg": {
        "translation": "Milligram",
        "category": Category.QUANTITY
    },
    "gm": {
        "translation": "gram",
        "category": Category.QUANTITY
    },
    "kg": {
        "translation": "Kilogram",
        "category": Category.QUANTITY
    },
    "ml": {
        "translation": "Milliliter",
        "category": Category.QUANTITY
    },
    "l": {
        "translation": "Liter",
        "category": Category.QUANTITY
    },
    "meq": {
        "translation": "Milliequivalent",
        "category": Category.QUANTITY
    },
    "mm": {
        "translation": "Millimoles",
        "category": Category.QUANTITY
    },
    "tbs": {
        "translation": "Tablespoonful",
        "category": Category.QUANTITY,
        "similar": ["tble","tbsp"]
    },
    "oz": {
        "translation": "Ounce",
        "category": Category.QUANTITY,
        "similar": ["℥"]
    },
    "floz": {
        "translation": "Fluid Ounce",
        "category": Category.QUANTITY
    },
    "pt": {
        "translation": "pint",
        "category": Category.QUANTITY
    },
    "qt": {
        "translation": "Quart",
        "category": Category.QUANTITY
    },
    "gal": {
        "translation": "Gallon",
        "category": Category.QUANTITY
    },
    "gr": {
        "translation": "Grain",
        "category": Category.QUANTITY
    },
    "lb": {
        "translation": "pound",
        "category": Category.QUANTITY,
        "similar": ["℔"]
    },
    "qs": {
        "translation": "Quantity Sufficient (add enough to make)",
        "category": Category.QUANTITY
    },
    "qty": {
        "translation": "quantity",
        "category": Category.QUANTITY,
        "similar": ["#"]
    },
    "u": {
        "translation": "unit",
        "category": Category.QUANTITY
    },
    "qod": {
        "translation": "Every Other Day",
        "category": Category.FREQUENCY
    },
    "qhs": {
        "translation": "At Bedtime",
        "category": Category.FREQUENCY
    },
    "aft": {
        "translation": "Afternoon",
        "category": Category.FREQUENCY
    },
    "am": {
        "translation": "Morning",
        "category": Category.FREQUENCY
    },
    "pm": {
        "translation": "Evening",
        "category": Category.FREQUENCY,
        "similar": ['noct']
    },
    "atc": {
        "translation": "Around The Clock",
        "category": Category.FREQUENCY
    },
    "min": {
        "translation": "Minute",
        "category": Category.FREQUENCY
    },
    "dai": {
        "translation": "Daily",
        "category": Category.FREQUENCY
    },
    "w": {
        "translation": "Week",
        "category": Category.FREQUENCY
    },
    "wk": {
        "translation": "Weekly",
        "category": Category.FREQUENCY
    },
    "sc": {
        "translation": "Subcutaneously",
        "category": Category.ROUTE,
        "similar": ["sq","sub-q"]
    },
    "top": {
        "translation": "Topically",
        "category": Category.ROUTE,
        "similar": ["toply"]
    },
    "id": {
        "translation": "Intradermaly",
        "category": Category.ROUTE
    },
    "im": {
        "translation": "Intramuscularly",
        "category": Category.ROUTE
    },
    "it": {
        "translation": "Intrathecaly",
        "category": Category.ROUTE
    },
    "ivpb": {
        "translation": "Intravenous Piggy Back",
        "category": Category.ROUTE
    }

}