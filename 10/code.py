import re

initial_val = "111"

def iterator(s, a=40):
    for i in range(a):

        iterated = ''
        regexed = [x.group() for x in re.finditer( r"(\d)\1+|(\d)", s)]
        
        for match in regexed: 

            if len(match) >= 2:
                iterated += f"{len(match)}{match[0]}"
            else:
                iterated += f'1{match}'

        s = iterated
    return iterated

print(f"First problem: {len(iterator(initial_val, 40))}")
print(f'Second problem: {len(iterator(initial_val, 50))}')