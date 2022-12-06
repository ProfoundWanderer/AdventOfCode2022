with open('input.txt') as f:
    fully_contain_count = 0
    for i, line in enumerate(f):
        cleansed_line = line.rstrip('\n')
        first_elf, second_elf = cleansed_line.split(',')

        first_elf_start, first_elf_end = [int(x) for x in first_elf.split('-')]
        second_elf_start, second_elf_end = [int(x) for x in second_elf.split('-')]

        first_elf_list = list(range(first_elf_start, first_elf_end + 1))
        second_elf_list = list(range(second_elf_start, second_elf_end + 1))

        # PART 1
        """
        # check both list against each other to see if all of one list is in another
        if all([x in second_elf_list for x in first_elf_list]) or all([x in first_elf_list for x in second_elf_list]):
            fully_contain_count += 1
        """

        # PART 2
        # check both list against each other to see if the list have any overlap
        if any([x in second_elf_list for x in first_elf_list]) or any([x in first_elf_list for x in second_elf_list]):
            fully_contain_count += 1

    print(fully_contain_count)
