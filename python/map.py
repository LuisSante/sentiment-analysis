import sys


def map():
    with open('./reviews.txt', 'r', encoding='utf-8') as file:
        with open('./map.txt', 'w', encoding='utf-8') as mapperFile:
            for line in file:
                words = line.split()
                for word in words:
                    mapperFile.write(f'{word} 1\n')


map()
