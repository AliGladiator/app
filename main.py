from typing import List
def cap_space(txt: str) -> str:
    new_txt = ''
    for i in txt:
        if i.isupper():
            new_txt = new_txt + ' ' + i.lower()
        else:
            new_txt = new_txt + i.lower()
    return new_txt


print(cap_space('AliSagrwIsHere'))
