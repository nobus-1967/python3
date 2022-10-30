#!/usr/bin/env python3
# Cats with hats
"""
You have one hundred (100) cats.

One day, you decide to arrange all your cats in a giant circle.
Initially, none of your cats has a hat on.
You walk around the circle a hundred times,
always starting with the ﬁrst cat (cat #1).
Each time you stop at a cat, you check if it has a hat on.
If it doesn’t, then you put a hat on it.
If it does, then you take the hat oﬀ.

1. The 1st round, you stop at every cat, placing a hat on each one.
2. The 2nd round, you stop only at every second cat
(#2, #4, #6, #8, and so on).
3. The 3rd round, you stop only at every third cat
(#3, #6, #9, #12, and so on).
4. You continue this process until you’ve made one hundred rounds
around the cats; on the last round, you stop only at cat #100.

This program outputs which cats have hats at the end.
"""
NUM_CATS = 100


def main():
    cats = {num: False for num in range(1, NUM_CATS + 1)}

    for iteration in range(1, NUM_CATS + 1):
        for cat in cats:
            if cat % iteration == 0:
                cats[cat] = not cats.get(cat)

    cats_in_hats = [cat for cat in cats if cats[cat]]
    print(f'Cats with hats: {cats_in_hats}')


if __name__ == '__main__':
    main()
