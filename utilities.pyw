from sys import argv
from functions import *

instructions = {
    "-": googlesearch,
    "youtube": youtubesearch,
    "images": imagesearch,
    "translate": translate,
    "sarcasm": sarcasm,
    "spacer": spacer,
    "spoilerspam": spoilerspam,
    "copypaste": copypaste,
    "cp": copypaste,
    "discord": discord,
    "dsc": discord,
    "emojify": emojify,
    "spam": spambot,
    "extend": extend,
    "mcprofiles": mcprofiles,
    "autoclick": autoclick,
    "tapemouse": tapemouse,
    "exponent": exponent,
    "ep": exponent,
    "fraction": fraction,
    "fc": fraction,
    "superscript": exponent,
    "mp": mcprofiles,
}

try:
    for i in instructions:
        if argv[1].startswith(i):
            instructions[i]()

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
    print(e)
