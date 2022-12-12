

with open('input.txt') as file:
    datastream_buffer = file.read()
    for i in range(len(datastream_buffer)):
        # Part 1
        if len(set(datastream_buffer[i:i+4])) == 4:
            print(i+4)
            break

        # Part 2
        if len(set(datastream_buffer[i:i+14])) == 14:
            print(i+14)
            break

