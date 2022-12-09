from itertools import zip_longest
import re


with open('input.txt') as f:
    stacks, instructions = f.read().split('\n\n')
    stacks = list(
        ''.join(x).strip()[1:]
        for i, x in enumerate(
            zip_longest(*map(list, stacks.split('\n')[::-1]), fillvalue=' ')
        )
        if i % 4 == 1
    )

    instructions = [tuple(map(int, re.findall(r"\d+", instruction))) for instruction in instructions.strip().split('\n')]

    _stacks = [None] + stacks[:]
    for amount, start, end in instructions:
        _stacks[start], crate = _stacks[start][:-amount], _stacks[start][-amount:][::-1]
        # Part 2 - Can also just remove this from the line above
        crate = crate[::-1]
        #
        _stacks[end] = _stacks[end] + crate

    # Part 1
    print(''.join(stack[-1] for stack in _stacks[1:]))
