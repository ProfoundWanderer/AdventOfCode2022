priorities_list = []
with open('input.txt') as f:
    current_group = []
    for i, line in enumerate(f):
        cleansed_line = line.rstrip('\n')

        # Part 1
        """
        middle_point = len(cleansed_line)//2
        first_compartment = cleansed_line[:middle_point]
        second_compartment = cleansed_line[middle_point:]

        in_both_compartments = set(first_compartment) & set(second_compartment)

        for letter in in_both_compartments:
            for char in in_both_compartments:
                if letter == char:
                    if char.isupper():
                        priorities_list.append(ord(char) - 38)
                        break
                    else:
                        priorities_list.append(ord(char) - 96)
                        break
        """

        # Part 2
        current_group.append(cleansed_line)

        if len(current_group) == 3:
            in_all_rucksacks = set(current_group[0]) & set(current_group[1]) & set(current_group[2])
            current_group = []

            for char in in_all_rucksacks:
                if char.isupper():
                    priorities_list.append(ord(char) - 38)
                    break
                else:
                    priorities_list.append(ord(char) - 96)
                    break

print(sum(priorities_list))
