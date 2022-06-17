import re

def erase(cc):
    # supprime espace entre deux (non lettre)
    # utilisation de lookbehinds/lookaheads pour éviter les problèmes de chevauchement
    return re.sub(r'(?<! ) (?! )', '', cc)
