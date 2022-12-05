score_dict = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}
score = 0


# Part 1
with open('input.txt') as f:
    for line in f:
        cleansed_line = line.rstrip('\n').split(' ')
        # Part 1
        """
        opponent_choice = cleansed_line[0]
        my_choice = cleansed_line[1]
        # if a draw
        if (
                opponent_choice == 'A' and my_choice == 'X' or
                opponent_choice == 'B' and my_choice == 'Y' or
                opponent_choice == 'C' and my_choice == 'Z'
        ):
            score += 3
        # if I lose
        elif (
                opponent_choice == 'A' and my_choice == 'Z' or
                opponent_choice == 'B' and my_choice == 'X' or
                opponent_choice == 'C' and my_choice == 'Y'
        ):
            score += 0
        # if I win
        elif (
                opponent_choice == 'A' and my_choice == 'Y' or
                opponent_choice == 'B' and my_choice == 'Z' or
                opponent_choice == 'C' and my_choice == 'X'
        ):
            score += 6

        score += score_dict[my_choice]
        """

        # Part 2
        opponent_choice = cleansed_line[0]
        needed_match_outcome = cleansed_line[1]
        # if I need to lose
        if needed_match_outcome == 'X':
            if opponent_choice == 'A':
                # C = scissors = 3 points
                score += 3
            elif opponent_choice == 'B':
                # A = rock = 1 point
                score += 1
            elif opponent_choice == 'C':
                # B = paper = 2 points
                score += 2
            score += 0
        # if I need draw
        elif needed_match_outcome == 'Y':
            if opponent_choice == 'A':
                # A = rock = 1 point
                score += 1
            elif opponent_choice == 'B':
                # B = paper = 2 points
                score += 2
            elif opponent_choice == 'C':
                # C = scissors = 3 points
                score += 3
            score += 3
        # if I need to win
        elif needed_match_outcome == 'Z':
            if opponent_choice == 'A':
                # B = paper = 2 points
                score += 2
            elif opponent_choice == 'B':
                # C = scissors = 3 points
                score += 3
            elif opponent_choice == 'C':
                # A = rock = 1 point
                score += 1
            score += 6

print(score)
