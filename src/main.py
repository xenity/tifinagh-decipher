from PIL import Image
import pytesseract

DIRECTIONS = [(0, 1), (1, 0), (1, 1), (-1, 1)]
MIN_WORD_LENGTH = 3

def load_wordlist():
    with open('assets/words.txt') as word_file:
        wordlist = set(word_file.read().split())
    return wordlist

def search_in_direction(grid, word_list, x, y, dx, dy):
    word = ''
    matching_words = set()
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        word += grid[x][y]
        if len(word) > MIN_WORD_LENGTH and word in word_list:
            matching_words.add(word)
        x += dx
        y += dy
    return matching_words

def search(grid, word_list):
    matching_words = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in DIRECTIONS:
                matching_words.update(search_in_direction(grid, word_list, x, y, dx, dy))
                matching_words.update(search_in_direction(grid, word_list, x, y, -dx, -dy))
    return matching_words


text_grid = pytesseract.image_to_string('assets/grid.png')
grid_array = [list(row) for row in text_grid.splitlines() if row]

english_word_list = load_wordlist()
words_found = search(grid_array, english_word_list)
print(words_found)