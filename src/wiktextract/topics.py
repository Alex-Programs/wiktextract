# List of valid topics and canonicalization & generalization mappings
# for topics
#
# Copyright (c) 2020-2022 Tatu Ylonen.  See file LICENSE and https://ylonen.org

# Set of valid topic tags.  (Other tags may be canonicalized to these)
valid_topics = set([
    "Buddhism",
    "Catholicism",
    "Chinese-cuisine",
    "Christianity",
    "Internet",
    "Islam",
    "LGBT",
    "acrobatics",
    "aeronautics",
    "aerospace",
    "agriculture",
    "alternative-medicine",
    "anatomy",
    "anthropology",
    "arachnology",
    "archeology",
    "architecture",
    "arithmetic",
    "art-history",
    "arts",
    "astrology",
    "astronomy",
    "astrophysics",
    "automotive",
    "ball-games",
    "beverages",
    "biochemistry",
    "biology",
    "board-games",
    "botany",
    "broadcasting",
    "business",
    "card-games",
    "carpentry",
    "cartography",
    "cause",
    "chemistry",
    "cities",
    "color",
    "combinatorics",
    "comics",
    "commerce",
    "communications",
    "computing",
    "construction",
    "cooking",
    "copyright",
    "cosmology",
    "countries",
    "court",
    "crafts",
    "criminology",
    "cryptocurrency",
    "cryptography",
    "cuisine",
    "demography",
    "dancing",
    "dentistry",
    "diving",
    "dogs",
    "dramaturgy",
    "drugs",
    "ecology",
    "economics",
    "education",
    "electrical-engineering",
    "electricity",
    "electromagnetism",
    "energy",
    "engineering",
    "entertainment",
    "entomology",
    "epistemology",
    "ethnography",
    "falconry",
    "fantasy",
    "fashion",
    "film",
    "finance",
    "food",
    "football",
    "fortifications",
    "freemasonry",
    "games",
    "gemology",
    "geography",
    "geology",
    "geometry",
    "government",
    "hairdressing",
    "heading",
    "healthcare",
    "histology",
    "history",
    "hobbies",
    "horology",
    "horses",
    "horseracing",
    "human-sciences",
    "hunting",
    "hydrology",
    "ichthyology",
    "ideology",
    "information",
    "information-science",
    "intellectual-property",
    "jewelry",
    "journalism",
    "law",
    "law-enforcement",
    "lifestyle",
    "linguistics",
    "literature",
    "location",
    "mammals",
    "management",
    "manga",
    "manner",
    "manufacturing",
    "marketing",
    "martial-arts",
    "masonry",
    "mathematics",
    "meats",
    "mechanical-engineering",
    "media",
    "medicine",
    "metallurgy",
    "meteorology",
    "metrology",
    "microbiology",
    "military",
    "mineralogy",
    "mining",
    "monarchy",
    "morphology",
    "music",
    "mysticism",
    "mythology",
    "natural-sciences",
    "naturism",
    "nautical",
    "navy",
    "neurology",
    "neuroscience",
    "nobility",
    "number-theory",
    "oceanography",
    "oenology",
    "ophthalmology",
    "organization",
    "origin",
    "ornithology",
    "paleontology",
    "pathology",
    "performing-arts",
    "petrology",
    "pets",
    "pharmacology",
    "philosophy",
    "phonology",
    "photography",
    "physical-sciences",
    "physics",
    "physiology",
    "planets",
    "political-science",
    "politics",
    "programming",
    "position",
    "publishing",
    "pulmonology",
    "prefectures",
    "printing",
    "property",
    "pseudoscience",
    "psychiatry",
    "psychology",
    "radio",
    "radiology",
    "railways",
    "real-estate",
    "region",
    "religion",
    "scholarly",
    "science-fiction",
    "sciences",
    "sexuality",
    "skating",
    "skiing",
    "social-science",
    "socialism",
    "sociology",
    "software",
    "source",
    "spiritualism",
    "sports",
    "state",
    "states",
    "statistics",
    "taxonomy",
    "telecommunications",
    "telegraphy",
    "telephony",
    "television",
    "temperature",
    "textiles",
    "theater",
    "theology",
    "time",
    "tools",
    "topology",
    "tourism",
    "toxicology",
    "transport",
    "typography",
    "units-of-measure",
    "urbanism",
    "vehicles",
    "video-games",
    "visual-arts",
    "weaponry",
    "weather",
    "weekdays",
    "wrestling",
    "writing",
    "zoology",
])

# Translation map for topics.
# XXX revisit this mapping.  Create more fine-tuned hierarchy
# XXX or should probably not try to generalize here
topic_generalize_map = {
    "(sport)": "sports",
    "card games": "games",
    "cards": "card-games",
    "board-games": "games",
    "game of Go": "board-games",
    "Scrabble": "board-games",
    "ball games": "ball-games",
    "ball-games": "games sports",
    "sports": "hobbies",
    "dice": "games",
    "rock paper scissors": "games",
    '"manner of action"': "manner",
    "manner of action": "manner",
    "planets of the Solar system": "planets",
    "planets": "astronomy",
    "continents": "region",
    "countries of Africa": "countries",
    "countries of Europe": "countries",
    "countries of Asia": "countries",
    "countries of South America": "countries",
    "countries of North America": "countries",
    "countries of Central America": "countries",
    "countries of Oceania": "countries",
    "countries": "geography",
    "country": "region",
    "the country": "countries",
    "regions of Armenia": "region",
    "region around the Ruppel river": "region",
    "geographical region": "region",
    "winegrowing region": "region",
    "the historical region": "region",
    "region": "location",
    "states of India": "states",
    "states of Australia": "states",
    "states": "region",
    "city": "cities",
    "cities": "region",
    "prefectures of Japan": "prefectures",
    "prefecture": "region",
    "software": "computing",
    "Windows": "software",
    "Linux": "software",
    "secret": "information",
    "mail": "information",
    "billiards": "games",
    "blackjack": "games",
    "backgammon": "games",
    "bridge": "games",
    "darts": "games",
    "scientific": "sciences",
    "scholarly": "sciences",
    "academia": "scholarly",
    "medicine": "sciences",
    "traditional medicine": "medicine",
    "human-sciences": "sciences",
    "anthropology": "human-sciences",
    "geography": "natural-sciences",
    "biology": "natural-sciences",
    "physical-sciences": "natural-sciences",
    "engineering": "physical-sciences",
    "drafting": "engineering",
    "CAD": "engineering computing",
    "mathematics": "sciences",
    "maths": "mathematics",
    "computing": "engineering mathematics",
    "anthropodology": "anthropology",
    "ornithology": "biology",
    "ornitology": "ornithology",
    "Ornithology": "ornithology",
    "birdwatching": "ornithology",
    "entomology": "biology",
    "insects": "entomology",
    "anatomy": "medicine",
    "Anatomy": "anatomy",
    "health": "medicine",
    "emergency medicine": "medicine",
    "bone": "anatomy",
    "body": "anatomy",
    "neuroanatomy": "anatomy neurology",
    "neurotoxicology": "neurology toxicology",
    "neurobiology": "neurology",
    "neurophysiology": "physiology neurology",
    "nephrology": "medicine",
    "hepatology": "medicine",
    "endocrinology": "medicine",
    "gynaecology": "medicine",
    "mammology": "medicine",
    "urology": "medicine",
    "neurology": "medicine neuroscience",
    "neuroscience": "medicine",
    "gerontology": "medicine",
    "andrology": "medicine",
    "phycology": "botany",
    "planktology": "botany",
    "oncology": "medicine",
    "hematology": "medicine",
    "physiology": "medicine",
    "gastroenterology": "medicine",
    "surgery": "medicine",
    "ophthalmology": "medicine",
    "opthalmology": "ophthalmology",
    "pharmacology": "medicine",
    "pharmaceuticals": "pharmacology",
    "drugs": "pharmacology",
    "cytology": "biology medicine",
    "healthcare": "government",
    "cardiology": "medicine",
    "dentistry": "medicine",
    "odontology": "dentistry",
    "pathology": "medicine",
    "toxicology": "medicine",
    "dermatology": "medicine",
    "epidemiology": "medicine",
    "psychiatry": "medicine psychology",
    "psychoanalysis": "medicine psychology",
    "phrenology": "medicine psychology",
    "psychology": "human-sciences",
    "sociology": "social-science",
    "social science": "social-science",
    "social sciences": "social-science",
    "in transactional analysis": "social-science",
    "social-science": "human-sciences",
    "hydraulics": "engineering",
    "demographics": "demography",
    "immunology": "medicine",
    "immunologic sense": "immunology",
    "anesthesiology": "medicine",
    "xenobiology": "biology",
    "sinology": "human-sciences",
    "psychopathology": "psychiatry",
    "histopathology": "pathology histology",
    "histology": "biology",
    "patology": "pathology",
    "virology": "microbiology",
    "bacteriology": "microbiology",
    "parapsychology": "pseudoscience",
    "psyschology": "psychology error-misspelling",
    "printing technology": "printing",
    "litography": "lithography",
    "lithography": "printing",
    "iconography": "art-history",
    "art-history": "history",
    "geomorphology": "geology",
    "phytopathology": "botany pathology",
    "bryology": "botany",
    "opthalmology": "medicine",
    "embryology": "medicine",
    "illness": "medicine",
    "parasitology": "medicine",
    "teratology": "medicine",
    "speech therapy": "medicine",
    "speech pathology": "medicine",
    "radiology": "medicine",
    "radiography": "radiology",
    "vaccinology": "medicine",
    "traumatology": "medicine",
    "microbiology": "biology",
    "pulmonology": "medicine",
    "obstetrics": "medicine",
    "pneumology": "pulmonology",
    "strong topology": "topology",
    "sociobiology": "social-science biology",
    "radio technology": "electrical-engineering radio",
    "authorship": "writing film",
    "volcanology": "geology",
    "gemmology": "gemology",
    "gem-cutting": "jewelry",
    "gemology": "geology jewelry",
    "jewelry": "lifestyle",
    "jewellery": "jewelry",
    "conchology": "zoology",
    "comics": "literature",
    "anime": "film",
    "manga": "comics",
    "codicology": "history",
    "zoology": "biology",
    "zootomy": "zoology",
    "botany": "biology",
    "malacology": "biology",
    "taxonomy": "biology",
    "biological category": "taxonomy",
    "geology": "geography",
    "mineralogy": "geology chemistry",
    "mineralology": "mineralogy",
    "biochemistry": "microbiology chemistry",
    "immunochemistry": "biochemistry immunology",
    "petrochemistry": "petrology chemistry",
    "linguistics": "human-sciences",
    "language": "linguistics",
    "grammar": "linguistics",
    "syntax": "linguistics",
    "semantics": "linguistics",
    "epistemology": "philosophy",
    "ontology": "epistemology",
    "etymology": "linguistics",
    "ethnology": "anthropology",
    "ethnography": "anthropology",
    "historical ethnography": "ethnography history",
    "entertainment industry": "entertainment economics",
    "electrochemistry": "chemistry",
    "classical studies": "history",
    "textual criticism": "linguistics",
    "nanotechnology": "engineering",
    "electromagnetism": "physics electrical-engineering",
    "biotechnology": "engineering medicine",
    "systems theory": "mathematics",
    "computer games": "games",
    "graphic design": "arts",
    "criminology": "law human-sciences",
    "penology": "criminology",
    "pragmatics": "linguistics",
    "morphology": "linguistics",
    "phonology": "linguistics",
    "phonetics": "phonology",
    "prosody": "phonology",
    "lexicography": "linguistics",
    "lexicology": "lexicography",
    "narratology": "linguistics",
    "linguistic": "linguistics",
    "translation studies": "linguistics",
    "semiotics": "linguistics",
    "dialectology": "linguistics",
    "ortography": "linguistics",
    "typography": "publishing",
    "letterpress typography": "typography",
    "psycholinguistics": "linguistics psychology",
    "sociolinguistics": "linguistics sociology",
    "beekeeping": "agriculture",
    "officialese": "government",
    "hairdressing": "crafts",
    "wagonmaking": "crafts",
    "smithwork": "crafts",
    "papermaking": "crafts",
    "hairstyle": "hairdressing",
    "textiles": "manufacturing",
    "weaving": "textiles",
    "quilting": "textiles",
    "knitting": "textiles",
    "sewing": "textiles",
    "dressmaking": "textiles",
    "cutting": "textiles",
    "furniture": "lifestyle",
    "freemasonry": "lifestyle",
    "Freemasonry": "freemasonry",
    "caving": "hobbies",
    "country dancing": "dancing",
    "dance": "dancing",
    "dancing": "sports",
    "hip-hop": "dancing",
    "cheerleading": "sports",
    "bowling": "sports",
    "athletics": "sports",
    "performing-arts": "arts sports",
    "acrobatics": "performing-arts",
    "castells": "acrobatics",
    "circus": "performing-arts",
    "juggling": "performing-arts",
    "martial arts": "martial-arts",
    "martial-arts": "sports military",
    "judo": "martial-arts",
    "skydiving": "sports",
    "meterology": "meteorology",
    "meteorology": "climatology",
    "climatology": "natural-sciences",
    "weather": "meteorology",
    "climate": "meteorology",
    "cryptozoology": "zoology",
    "lepidopterology": "zoology",
    "nematology": "zoology",
    "campanology": "history",
    "vexillology": "history",
    "phenomenology": "philosophy",
    "seismology": "geology",
    "astronomy": "natural-sciences",
    "cosmology": "astronomy",
    "astrogeology": "astronomy geology",
    "areology": "astronomy geology",
    "stratigraphy": "geology",
    "orography": "geology",
    "stenography": "writing",
    "graphonomics": "writing",
    "scriptwriting": "writing",
    "orthography": "writing",
    "palynology": "chemistry microbiology",
    "lichenology": "botany",
    "seasons": "weather",
    "information technology": "computing",
    "algebra": "mathematics",
    "calculus": "mathematics",
    "arithmetics": "mathematics",
    "statistics": "mathematics",
    "modelling": "mathematics",
    "geometry": "mathematics",
    "logic": "mathematics philosophy",
    "trigonometry": "mathematics",
    "mathematical analysis": "mathematics",
    "ethics": "philosophy",
    "existentialism": "philosophy",
    "religion": "lifestyle",
    "philosophy": "human-sciences",
    "shipping": "transport economics",
    "railways": "transport",
    "trains": "railways",
    "automotive": "vehicles",
    "automobile": "automotive",
    "vehicles": "transport",
    "tourism": "transport lifestyle",
    "travel": "tourism lifestyle",
    "travel industry": "tourism",
    "parliamentary procedure": "government",
    "espionage": "government military",
    "food": "lifestyle",
    "cuisine": "food",
    "Chinese cuisine": "Chinese-cuisine",
    "Indian Chinese cuisine": "Chinese-cuisine",
    "seafood": "cuisine",
    "culinary": "cuisine",
    "vegetable": "food",
    "beverages": "food",
    "beer": "beverages",
    "brewing": "beverages manufacturing",
    "enology": "oenology",
    "oenology": "beverages",
    "wine": "oenology",
    "sewage treatment": "engineering",
    "cooking": "food",
    "baking": "cooking",
    "Indian cookery": "cooking cuisine",
    "sexuality": "lifestyle",
    "seduction community": "sexuality",
    "BDSM": "sexuality",
    "LGBT": "sexuality",
    "sexual orientations": "sexuality",
    "romantic orientations": "sexuality",
    "prostitution": "sexuality",
    "sexology": "sexuality",
    "biblical": "religion",
    "ecclesiastical": "religion",
    "genetics": "biology medicine",
    "medical terminology": "medicine",
    "homeopathy": "medicine",
    "alternative medicine": "alternative-medicine",
    "alternative-medicine": "medicine",
    "Ayurveda": "alternative-medicine",
    "mycology": "biology",
    "paganism": "religion",
    "Scientology": "religion",
    "Islam": "religion",
    "Sufism": "Islam mysticism",
    "mechanical-engineering": "engineering",
    "mechanics": "mechanical-engineering",
    "mechanical": "mechanical-engineering",
    "robotics": "mechanical-engineering computing",
    "machining": "mechanical-engineering",
    "lubricants": "mechanical-engineering",
    "fasteners": "mechanical-engineering",
    "thermodynamics": "physics",
    "fluid dynamics": "physics",
    "signal processing": "computing mathematics",
    "topology": "mathematics",
    "algebraic topology": "topology",
    "algebraic geometry": "geometry",
    "norm topology": "topology",
    "linear algebra": "mathematics",
    "number-theory": "mathematics",
    "number theory": "number-theory",
    "analytic number theory": "number-theory",
    "insurance": "business",
    "taxation": "economics government",
    "sugar-making": "manufacturing",
    "glassmaking": "manufacturing",
    "food manufacture": "manufacturing",
    "manufacturing": "business",
    "optics": "physics engineering",
    "chemistry": "physical-sciences",
    "ceramics": "chemistry engineering",
    "chess": "board-games",
    "xiangqi": "board-games",
    "shogi": "board-games",
    "checkers": "board-games",
    "mahjong": "board-games",
    "Rubik's Cube": "games",
    "crystallography": "chemistry",
    "fluids": "chemistry physics engineering",
    "science": "sciences",
    "physics": "physical-sciences",
    "electrical-engineering": "engineering",
    "electricity": "electrical-engineering electromagnetism energy",
    "electronics": "electricity",
    "programming": "computing",
    "Lisp": "programming",
    "databases": "computing",
    "visual art": "visual-arts",
    "visual arts": "visual-arts",
    "visual-arts": "arts",
    "graffiti": "visual-arts",
    "crafts": "arts hobbies",
    "papercraft": "crafts",
    "bowmaking": "crafts",
    "lutherie": "crafts",
    "ironworking": "crafts",
    "glassblowing": "crafts",
    "history": "human-sciences",
    "Egyptology": "history",
    "heraldry": "hobbies nobility",
    "philately": "hobbies",
    "hobbies": "lifestyle",
    "numismatics": "hobbies",
    "chronology": "horology",
    "horology": "hobbies",
    "cryptography": "computing",
    "encryption": "cryptography",
    "finance": "business",
    "finances": "finance",
    "financial": "finance",
    "accounting": "finance",
    "economics": "science",
    "microeconomics": "economics",
    "politics": "government",
    "geopolitics": "politics",
    "sociopolitics": "politics",
    "ideology": "politics philosophy",
    "feminism": "ideology",
    "communism": "ideology",
    "socialism": "ideology",
    "capitalism": "ideology",
    "feudalism": "politics",
    "fascism": "ideology",
    "white supremacist ideology": "ideology",
    "manosphere": "ideology",
    "pedology": "geography psychology",
    "biogeography": "geography biology",
    "cryptocurrency": "finance",
    "nobility": "monarchy",
    "monarchy": "politics",
    "demography": "demographics",
    "historical demography": "demography",
    "chromatography": "chemistry",
    "anarchism": "ideology",
    "economic liberalism": "ideology",
    "diplomacy": "politics",
    "regionalism": "politics",
    "war": "politics",
    "military": "war government",
    "agri.": "agriculture",
    "agriculture": "business lifestyle",
    "horticulture": "agriculture",
    "fashion": "lifestyle",
    "cosmetics": "lifestyle",
    "design": "arts",
    "money": "finance",
    "oceanography": "geography",
    "geological oceanography": "geology oceanography",
    "angelology": "theology",
    "woodworking": "carpentry crafts",
    "art": "arts",
    "television": "broadcasting",
    "broadcasting": "media",
    "radio": "broadcasting",
    "radio communications": "radio",
    "radio technics": "radio",
    "journalism": "media",
    "writing": "journalism literature communications publishing",
    "editing": "writing publishing",
    "poetry": "writing",
    "film": "television",
    "cinematography": "film",
    "drama": "dramaturgy",
    "dramaturgy": "film theater",
    "printing": "publishing",
    "publishing": "media",
    "science fiction": "literature",
    "space science": "aerospace",
    "astronautics": "aerospace",
    "aerodynamics": "aerospace physics",
    "NASA": "aerospace",
    "ESA": "aerospace",
    "fiction": "literature",
    "pornography": "media sexuality",
    "DVD": "media",
    "sex": "sexuality",
    "bibliography": "information-science",
    "information science": "information-science",
    "information-science": "human-sciences computing",
    "naturism": "lifestyle",
    "veganism": "lifestyle",
    "urbanism": "lifestyle",
    "Kantianism": "philosophy",
    "newspapers": "journalism",
    "telegraphy": "telecommunications",
    "wireless telegraphy": "telegraphy",
    "telegram": "telegraphy",
    "audio": "electrical-engineering",
    "literature": "publishing",
    "folklore": "arts literature history",
    "MMORPG": "Internet video-games",
    "ACG": "video-games",
    "roguelikes": "video-games",
    "Magic: The Gathering": "games",
    "IRC": "Internet",
    "CSS": "Internet",
    "blogging": "Internet",
    "music": "entertainment",
    "baile funk": "music",
    "musical note": "music",
    "guitar": "music",
    "handbells": "music",
    "handball": "ball-games",
    "racquet sports": "ball-games",
    "billiards": "ball-games",
    "musicology": "music human-sciences",
    "MIDI": "music",
    "talking": "communications",
    "militaryu": "military error-misspelling",
    "army": "military",
    "navy": "military",
    "naval": "navy",
    "weaponry": "military tools",
    "weapon": "weaponry",
    "firearms": "weaponry",
    "artillery": "weaponry",
    "ballistics": "weaponry physics",
    "fortifications": "military",
    "fortification": "fortifications",
    "law enforcement": "government",
    "police": "law-enforcement",
    "firefighting": "government",
    "archaeology": "history",
    "epigraphy": "history literature",
    "paleontology": "history biology",
    "palæontology": "paleontology",
    "paleobiology": "paleontology",
    "paleoanthropology": "paleontology anthropology",
    "paleogeography": "paleontology geography",
    "paleography": "epigraphy paleogeography",
    "palentology": "paleontology error-misspelling",
    "papyrology": "history",
    "hagiography": "history religion",
    "palaeography": "paleography",
    "historical geography": "geography history",
    "historiography": "history",
    "calligraphy": "arts writing",
    "crocheting": "crafts",
    "ichthyology": "zoology",
    "fish": "ichthyology",
    "herpetology": "zoology",
    "glaciology": "geography",
    "arachnology": "zoology",
    "mammals": "zoology",
    "mammalogy": "zoology",
    "rodents": "mammals",
    "snakes": "zoology",
    "veterinary pathology": "zoology pathology",
    "veterinary": "zoology pathology",
    "conservation": "biology history",
    "patology": "pathology error-misspelling",
    "acarology": "zoology",
    "mythology": "mysticism",
    "ufology": "mythology",
    "fundamental interactions": "physics",
    "quantum field theory": "physics",
    "colorimetry": "physics",
    "extragalactic medium": "cosmology",
    "extra-cluster medium": "cosmology",
    "uranography": "cartography astronomy",
    "astrocartography": "uranography",
    "mining": "business",
    "quarrying": "mining",
    "forestry": "business",
    "metalworking": "metallurgy crafts",
    "tin-plate manufacture": "manufacturing",
    "metallurgy": "engineering",
    "brick-making": "manufacturing",
    "communication": "communications",
    "telecommunications": "electrical-engineering communications",
    "telephony": "telecommunications communications",
    "mobile telephony": "telephony",
    "telephone": "telephony",
    "bookbinding": "crafts",
    "engraving": "crafts",
    "petrology": "geology",
    "petrography": "petrology",
    "petroleum": "energy",
    "energy": "business physics",
    "shipbuilding": "manufacturing",
    "plumbing": "construction",
    "roofing": "construction",
    "carpentry": "construction",
    "construction": "manufacturing",
    "piledriving": "construction",
    "masonry": "construction",
    "stone": "masonry",
    "tools": "engineering",
    "cranes": "tools",
    "colleges": "education",
    "higher education": "education",
    "clothing": "textiles fashion",
    "dyeing": "textiles",
    "fabrics": "textiles",
    "alchemy": "pseudoscience",
    "photography": "hobbies arts",
    "videography": "photography film",
    "pets": "lifestyle",
    "horses": "pets sports",
    "equestrianism": "horses",
    "equestrian": "horses",
    "dressage": "horses",
    "horse racing": "horseracing",
    "horse-racing": "horseracing",
    "horseracing": "horses racing",
    "equitation": "horses",
    "farriery": "horses",
    "dogs": "pets",
    "sheepdog trials": "dogs",
    "demoscene": "computing lifestyle",
    "golf": "sports",
    "tennis": "sports",
    "hunting": "hobbies",
    "fishing": "hobbies",
    "birdwashing": "hobbies",
    "paintball": "games",
    "fisheries": "ecology",
    "limnology": "ecology geology",
    "informatics": "computing",
    "bioinformatics": "computing biology",
    "marketing": "business",
    "advertising": "marketing",
    "electrotechnology": "electrical-engineering",
    "electromagnetic radiation": "electromagnetism",
    "electronics manufacturing": "manufacturing",
    "electric power": "energy electrical-engineering",
    "electronic communication": "telecommunications",
    "electrical device": "electrical-engineering",
    "cigars": "lifestyle",
    "smoking": "lifestyle",
    "flowery": "lifestyle",
    "gambling": "games",
    "bingo": "games",
    "exercise": "sports",
    "football": "ball-games",
    "netball": "ball-games",
    "softball": "ball-games",
    "American football": "football",
    "acting": "film theater",
    "theater": "entertainment",
    "comedy": "entertainment",
    "entertainment": "lifestyle",
    "dominoes": "games",
    "pocket billiards": "games",
    "pool": "games",
    "graphical user interface": "computing",
    "mysticism": "philosophy",
    "philology": "linguistics history philosophy",
    "enthnology": "human-sciences",
    "creationism": "religion",
    "shamanism": "religion",
    "politology": "political-science",
    "political-science": "social-sciences",
    "political science": "political-science",
    "cartomancy": "mysticism",
    "tarot": "mysticism",
    "tasseography": "mysticism",
    "occult": "mysticism",
    "theology": "religion",
    "religionists": "religion",
    "spiritualism": "religion",
    "spiritism": "spiritualism",
    "demonology": "religion",
    "Zoroastrianism": "religion",
    "Wicca": "religion",
    "Buddhism": "religion",
    "Buddhist": "Buddhism",
    "Shingon Buddhism": "Buddhism",
    "Tendai or Kegon Buddhism": "Buddhism",
    "Zen and Pure Land Buddhism": "Buddhism",
    "Tham": "Buddhism",  # Buddhist religious script
    "motor racing": "racing",
    "racing": "sports",
    "spinning": "sports",
    "gymnastics": "sports",
    "cricket": "ball-games",
    "volleyball": "ball-games",
    "lacrosse": "ball-games",
    "rugby": "ball-games",
    "bodybuilding": "sports",
    "falconry": "hunting",
    "hawking": "falconry",
    "parachuting": "hobbies",
    "squash": "ball-games",
    "curling": "ball-games",
    "motorcycling": "hobbies",
    "swimming": "sports",
    "diving": "sports",
    "underwater diving": "diving",
    "basketball": "ball-games",
    "baseball": "ball-games",
    "pesäpallo": "ball-games",
    "soccer": "ball-games",
    "snooker": "ball-games",
    "snowboarding": "sports",
    "skateboarding": "sports",
    "weightlifting": "sports",
    "skiing": "sports",
    "alpine skiing": "skiing",
    "aerial freestyle": "skiing",
    "mountaineering": "sports",
    "skating": "sports",
    "ice hockey": "skating",
    "cycling": "sports",
    "rowing": "sports",
    "boxing": "martial-arts",
    "Scouting": "lifestyle",
    "bullfighting": "entertainment",
    "archery": "martial-arts",
    "fencing": "martial-arts",
    "climbing": "sports",
    "surfing": "sports",
    "ballooning": "sports",
    "sailmaking": "crafts nautical",
    "sailing": "nautical",
    "maritime": "nautical",
    "ropemaking": "crafts nautical",
    "nautical": "transport",
    "retail": "commerce",
    "commercial": "commerce",
    "retailing": "commerce",
    "electrical": "electricity",
    "category theory": "mathematics computing",
    "in technical contexts": "engineering physics chemistry computing",
    "technology": "engineering",
    "technical": "engineering",
    "stock exchange": "finance",
    "stock market": "finance",
    "stock ticker symbol": "finance",
    "trading": "finance",
    "surveying": "geography",
    "networking": "computing",
    "computer sciences": "computing",
    "computer software": "computing",
    "software compilation": "computing",
    "computer languages": "computing",
    "computer hardware": "computing",
    "computer graphics": "computing",
    "meats": "food",
    "meat": "meats",
    "web design": "computing",
    "aviation": "aeronautics",
    "aeronautics": "aerospace",
    "aerospace": "engineering business",
    "rocketry": "aerospace",
    "investment": "finance",
    "computing theory": "computing mathematics",
    "information theory": "mathematics computing",
    "probability": "mathematics",
    "probability theory": "mathematics",
    "set theory": "mathematics",
    "sets": "mathematics",
    "order theory": "mathematics",
    "graph theory": "mathematics",
    "group theory": "mathematics",
    "complex analysis": "mathematics",
    "measure theory": "mathematics",
    "mathematical analysis": "mathematics",
    "combinatorics": "mathematics",
    "cellular automata": "computing mathematics",
    "game theory": "mathematics computing",
    "computational": "computing",
    "computer": "computing",
    "behavioral sciences": "psychology",
    "behavior": "psychology",
    "clinical psychology": "psychology",
    "psycology": "psychology",
    "space sciences": "astronomy",
    "applied sciences": "sciences engineering",
    "civil engineering": "engineering",
    "(sport)": "sports",
    "banking": "business",
    "commerce": "business",
    "real-estate": "business",
    "real estate": "real-estate",
    "cryptocurrency": "finance",
    "cryptocurrencies": "cryptocurrency",
    "cartography": "geography",
    "ecology": "biology",
    "hydrology": "geography",
    "hydrography": "hydrology oceanography",
    "hydrodynamics": "hydrology physics",
    "topography": "geography",
    "polygraphy": "law",
    "planetology": "astronomy",
    "astrology": "mysticism",
    "astrology signs": "astrology",
    "linguistic morphology": "morphology",
    "science": "sciences",
    "console": "video-games",
    "video games": "video-games",
    "role-playing games": "games",
    "poker": "card-games",
    "waterpolo": "games",
    "wrestling": "martial-arts",
    "professional wrestling": "wrestling",
    "sumo": "wrestling",
    "legal": "law",
    "copyright": "intellectual-property",
    "intellectual-property": "law",
    "patent law": "intellectual-property",
    "intellectual property": "intellectual-property",
    "court": "law government",
    "rail transport": "railways",
    "traffic": "transport",
    "incoterm": "transport law business",
    "road": "transport",
    "colour": "color",
    "days of the week": "weekdays",
    "weekdays": "time",
    "duration": "time",
    "temporal location": "time",
    "theology": "religion",
    "monotheism": "religion",
    "Catholicism": "Christianity",
    "Shinto": "religion",
    "Gnosticism": "religion",
    "Protestantism": "Christianity",
    "occultism": "religion",
    "buddhism": "religion",
    "hinduism": "religion",
    "Roman Catholicism": "Catholicism",
    "naturism": "lifestyle",
    "carnaval": "lifestyle",
    "organic chemistry": "chemistry",
    "inorganic chemistry": "chemistry",
    "gaming": "games",
    "SI units": "units-of-measure",
    "units of measure": "units-of-measure",
    "Western Christianity": "Christianity",
    "Eastern Christianity": "Christianity",
    "Abrahamic religions": "religion",

}