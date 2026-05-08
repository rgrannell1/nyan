# Colour scheme definitions for nyancat — maps pixel characters to ANSI background codes.
from typing import TypedDict


class ColourScheme(TypedDict):
    colors: dict[str, str]
    rainbow: str  # sequence of pixel chars that form the trailing rainbow strip


# Classic nyancat — full rainbow trail, original cat colours
SCHEME_RAINBOW: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',
        '.': '\033[48;5;231m',
        "'": '\033[48;5;16m',
        '@': '\033[48;5;230m',
        '$': '\033[48;5;175m',
        '-': '\033[48;5;162m',
        '>': '\033[48;5;196m',
        '&': '\033[48;5;214m',
        '+': '\033[48;5;226m',
        '#': '\033[48;5;118m',
        '=': '\033[48;5;33m',
        ';': '\033[48;5;19m',
        '*': '\033[48;5;240m',
        '%': '\033[48;5;175m',
    },
    'rainbow': ',,>>&&&+++###==;;;,,',
}

# Trans pride — light blue, pink, and white stripes; cat body gains trans colours
SCHEME_TRANS: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',
        '.': '\033[48;5;231m',
        "'": '\033[48;5;16m',
        '@': '\033[48;5;231m',   # white
        '$': '\033[48;5;218m',   # trans pink
        '-': '\033[48;5;204m',   # deeper pink
        '>': '\033[48;5;153m',   # trans light blue
        '&': '\033[48;5;218m',   # trans pink
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;153m',   # trans light blue
        '=': '\033[48;5;111m',   # medium blue
        ';': '\033[48;5;75m',    # deeper blue
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;218m',   # trans pink
    },
    # blue, pink, white, pink, blue — five stripes matching the trans flag
    'rainbow': ',,>>>&&&++++&&&>>>,,'
}

# Ireland — green, white, and orange; poptart stripes take the tricolour
SCHEME_IRELAND: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy background
        '.': '\033[48;5;231m',   # white (stars + white stripe)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;230m',   # cream (cat body)
        '$': '\033[48;5;157m',   # light green (cat body tint)
        '-': '\033[48;5;28m',    # Irish green (cat detail)
        '>': '\033[48;5;34m',    # Irish green
        '&': '\033[48;5;208m',   # Irish orange
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;28m',    # Irish green (darker)
        '=': '\033[48;5;231m',   # white
        ';': '\033[48;5;208m',   # Irish orange
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;157m',   # light green
    },
    # green (top), white (middle), orange (bottom)
    'rainbow': ',,######.....&&&&&,,'
}

# Cyprus — white, copper, and olive green; colours from the flag's map and olive branches
SCHEME_CYPRUS: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark background
        '.': '\033[48;5;231m',   # white (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;230m',   # cream (cat body)
        '$': '\033[48;5;180m',   # warm tan (cat body)
        '-': '\033[48;5;172m',   # copper detail
        '>': '\033[48;5;172m',   # copper (used in rainbow)
        '&': '\033[48;5;136m',   # deeper copper
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;64m',    # olive green (brighter than 58)
        '=': '\033[48;5;22m',    # dark olive green
        ';': '\033[48;5;64m',    # olive green
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;180m',   # tan
    },
    # white (top), copper (middle — was broken, now uses > not +), olive green (bottom)
    'rainbow': ',,......>>>>######,,'
}

# Spain — red and golden yellow in 1:2:1 ratio matching the flag's horizontal bands
SCHEME_SPAIN: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark background
        '.': '\033[48;5;231m',   # white (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;230m',   # cream (cat body)
        '$': '\033[48;5;220m',   # golden yellow (cat body)
        '-': '\033[48;5;160m',   # Spanish red (detail)
        '>': '\033[48;5;196m',   # red
        '&': '\033[48;5;208m',   # orange-red
        '+': '\033[48;5;220m',   # golden yellow
        '#': '\033[48;5;220m',   # golden yellow
        '=': '\033[48;5;160m',   # red
        ';': '\033[48;5;88m',    # dark red
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;220m',   # golden yellow
    },
    # red (top, narrow), gold (middle, wide), red (bottom, narrow) — 1:2:1
    'rainbow': ',,>>>>++++++++>>>>,,',
}

# India — saffron, white with Ashoka blue, and India green
SCHEME_INDIA: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy
        '.': '\033[48;5;231m',   # white (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;230m',   # cream (cat body)
        '$': '\033[48;5;208m',   # saffron (cat body tint)
        '-': '\033[48;5;22m',    # India green (detail)
        '>': '\033[48;5;208m',   # saffron
        '&': '\033[48;5;208m',   # saffron
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;28m',    # India green
        '=': '\033[48;5;27m',    # Ashoka chakra blue
        ';': '\033[48;5;22m',    # dark India green
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;208m',   # saffron
    },
    # saffron, white, blue (Ashoka chakra), white, India green
    'rainbow': ',,&&&&..==..######,,'
}

# Sealand — black, gold, and red from the Principality of Sealand flag
SCHEME_SEALAND: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy background (contrast for black stripe + cat body)
        '.': '\033[48;5;220m',   # gold (stars become gold coins)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;252m',   # light grey (cat body — visible against navy)
        '$': '\033[48;5;248m',   # medium grey (cat body)
        '-': '\033[48;5;240m',   # grey (detail)
        '>': '\033[48;5;196m',   # red
        '&': '\033[48;5;160m',   # darker red
        '+': '\033[48;5;220m',   # gold
        '#': '\033[48;5;136m',   # dark gold
        '=': '\033[48;5;88m',    # dark red
        ';': '\033[48;5;88m',    # dark red
        '*': '\033[48;5;232m',   # near-black (rainbow black stripe — readable against navy)
        '%': '\033[48;5;244m',   # grey
    },
    # black (top), gold (middle), red (bottom)
    'rainbow': ',,*****+++++>>>>>>,,'
}

# Italy — green, white, and red vertical tricolour
SCHEME_ITALY: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy background
        '.': '\033[48;5;231m',   # white (stars + white stripe)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;230m',   # cream (cat body)
        '$': '\033[48;5;157m',   # light green (cat body tint)
        '-': '\033[48;5;28m',    # Italian green (detail)
        '>': '\033[48;5;196m',   # Italian red
        '&': '\033[48;5;160m',   # deeper red
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;28m',    # Italian green
        '=': '\033[48;5;196m',   # red
        ';': '\033[48;5;160m',   # deeper red
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;157m',   # light green
    },
    # green (top), white (middle), red (bottom)
    'rainbow': ',,######.....>>>>>,,',
}

# Pinks — hot pinks, magentas, and purples throughout; dark purple background
SCHEME_PINKS: ColourScheme = {
    'colors': {
        ',': '\033[48;5;53m',    # dark purple background
        '.': '\033[48;5;219m',   # light pink (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;225m',   # very light pink (cat body highlight)
        '$': '\033[48;5;218m',   # pink
        '-': '\033[48;5;204m',   # rose
        '>': '\033[48;5;197m',   # hot pink
        '&': '\033[48;5;201m',   # magenta
        '+': '\033[48;5;219m',   # light pink
        '#': '\033[48;5;213m',   # orchid
        '=': '\033[48;5;207m',   # medium orchid
        ';': '\033[48;5;141m',   # medium purple
        '*': '\033[48;5;182m',   # muted pink (replaces cat grey)
        '%': '\033[48;5;218m',   # pink
    },
    'rainbow': ',,>>&&&+++###==;;;,,',
}

# Poland — white and red horizontal bands matching the Polish flag
SCHEME_POLAND: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy background
        '.': '\033[48;5;231m',   # white (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;231m',   # white (cat body)
        '$': '\033[48;5;252m',   # light grey (cat body tint)
        '-': '\033[48;5;196m',   # Polish red (detail)
        '>': '\033[48;5;196m',   # Polish red (brighter)
        '&': '\033[48;5;160m',   # deeper red
        '+': '\033[48;5;231m',   # white
        '#': '\033[48;5;252m',   # light grey
        '=': '\033[48;5;196m',   # Polish red
        ';': '\033[48;5;160m',   # deeper red
        '*': '\033[48;5;240m',   # grey
        '%': '\033[48;5;252m',   # light grey
    },
    # white (top), red (bottom) — equal halves matching the Polish flag
    'rainbow': ',,........>>>>>>>>,,',
}

# Germany — black, red, and gold horizontal bands matching the Bundesflagge
SCHEME_GERMANY: ColourScheme = {
    'colors': {
        ',': '\033[48;5;17m',    # dark navy background (contrast for black stripe)
        '.': '\033[48;5;220m',   # gold (stars)
        "'": '\033[48;5;16m',    # black
        '@': '\033[48;5;252m',   # light grey (cat body)
        '$': '\033[48;5;244m',   # mid grey (cat body tint)
        '-': '\033[48;5;240m',   # grey (detail)
        '>': '\033[48;5;160m',   # German red
        '&': '\033[48;5;124m',   # deeper red
        '+': '\033[48;5;220m',   # German gold
        '#': '\033[48;5;214m',   # darker gold
        '=': '\033[48;5;232m',   # near-black
        ';': '\033[48;5;232m',   # near-black
        '*': '\033[48;5;232m',   # near-black (rainbow black band — readable against navy)
        '%': '\033[48;5;244m',   # grey
    },
    # black (top), red (middle), gold (bottom)
    'rainbow': ',,******>>>>>+++++,,'
}

SCHEMES: dict[str, ColourScheme] = {
    'rainbow': SCHEME_RAINBOW,
    'trans': SCHEME_TRANS,
    'ireland': SCHEME_IRELAND,
    'cyprus': SCHEME_CYPRUS,
    'spain': SCHEME_SPAIN,
    'india': SCHEME_INDIA,
    'sealand': SCHEME_SEALAND,
    'pinks': SCHEME_PINKS,
    'germany': SCHEME_GERMANY,
    'poland': SCHEME_POLAND,
    'italy': SCHEME_ITALY,
}
