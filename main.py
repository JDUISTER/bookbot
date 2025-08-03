#!bookenv/bin/python3

from stats import frank_path, get_num_words, get_characters, sort_on, create_character_list
import sys

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

result_a = get_num_words(book_path)

words = get_characters(book_path)

result_b = create_character_list(words)

result_b.sort(key=sort_on, reverse=True)

final_result = [
"============ BOOKBOT ============",
f"Analyzing book found at {frank_path}...",
"----------- Word Count ----------",
f"Found {result_a} total words",
"--------- Character Count -------"
]

for i in result_b:
    row = f"{i['char']}: {i['num']}"
    final_result.append(row)
final_result.append("============= END ===============")

for i in final_result:
    print(i)
