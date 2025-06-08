import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> E SAux
    SAux -> Conj E SAux | Empty
    E -> N V N Conj V | N V N | N V
    N -> NP NAux
    NAux -> Conj NP NAux | Empty
    NP -> NE | PS | N Adj | Adj
    NE -> NEP NEAux
    NEAux -> Conj NEP NEAux | Empty
    NEP -> PI FC NER VM | PF NER VF | PG FV NER VM | FC NER VM | NER VF | FV NER VM
    V -> VP VAux
    VAux -> Conj VP VAux | Empty
    VP -> TV VPAux
    VPAux -> Adv VPAux | Empty
    Adv -> TAdv AdvAux
    AdvAux -> Conj TAdv AdvAux | Empty
    Adj -> TAdj AdjAux
    AdjAux -> Conj TAdj AdjAux | Empty
    NER -> 'ibr' | 'agazz' | 'iorn' | 'mic' | 'an' | 'donn' | 'scuol' | 'insalat' | 'cos' | 'cas'
    PS -> 'loro'
    PI -> 'i'
    PG -> 'gli'
    PF -> 'le'
    VM -> 'i'
    VF -> 'e'
    TV -> 'sono' | 'mangiano' | 'legono'
    TAdv -> 'molto' | 'qui' | 'sempre'
    Adj -> 'forti' | 'alti' | 'belli'
    FC -> 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z'
    FV -> 'a' | 'e' | 'i' | 'o' | 'u'
    Conj -> 'e' | 'o'
    Empty ->
""")

parser = nltk.ChartParser(grammar)

def separate(sentence):
    sentence = sentence.lower()

    separation = {
        'libri': 'l ibr i',
        'ragazzi': 'r agazz i',
        'giorni': 'g iorn i',
        'amici': 'a mic i',
        'pani': 'p an i',
        'case': 'cas e',
        'donne': 'donn e',
        'scuole': 'scuol e',
        'insalate': 'insalat e',
        'cose': 'cos e',
    }

    for originalWord, separated in separation.items():
        sentence = sentence.replace(originalWord, separated)
    return sentence.split()

sentences = [
    #correct
    "I giorni e loro mangiano libri e pani",
    "Le donne mangiano molto insalate",
    "Gli amici sono alti",
    "Loro legono i libri",
    "Le scuole sono qui",
    "I pani sono molto belli",
    "Le cose sono molto belli e loro legono i libri",
    "I ragazzi sono forti",
    # incorrect
    "Gli pani sono alti",
    "Le scuole gli amici alti",
    "I giorni sono legono",
    "Le ragazzi sono belli e forti",
    "Il giorni e mangiano",
]

for sentence in sentences:
    try:
        separated_sentence = separate(sentence)
        trees = list(parser.parse(separated_sentence))
        if trees:
            for tree in trees:
                print("\nThe sentence " + "\033[1m" + sentence + "\033[0m" + " has the following tree: ")
                tree.pretty_print()
                print()
        else:
            print("The sentence " + "\033[1m" + sentence + "\033[0m" + " is not correct.")
    except Exception as e:
        print("The sentence " + "\033[1m" + sentence + "\033[0m" + " is not correct. Error: " + str(e))