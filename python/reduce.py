def reduce():
    # current_word = None
    # current_count = 0
    # word = None
    word_counts = {}

    with open('./map.txt', 'r', encoding='utf-8') as file:
        with open('./reduce.txt', 'w', encoding='utf-8') as reduceFile:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    word, count = parts[0], int(parts[1])
                    if word in word_counts:
                        word_counts[word] += count
                    else:
                        word_counts[word] = count

            dic_sort = dict(
                sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

            for word, count in dic_sort.items():
                reduceFile.write(f"{word} {count}\n")


reduce()
