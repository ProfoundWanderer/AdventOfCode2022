all_elf_storage = []
current_elf_storage = 0
with open('input.txt') as f:
    for line in f:
        if cleansed_line := line.replace('\n', ''):
            current_elf_storage += int(cleansed_line)
        else:
            all_elf_storage.extend([current_elf_storage])
            current_elf_storage = 0
    all_elf_storage.extend([current_elf_storage])

print(sum(sorted(all_elf_storage, reverse=True)[:3]))
