from stats import count_words
from stats import num_characters
from stats import sort_dict
import sys
from sys import argv

def get_book_text(filepath):
 with open(filepath) as f:
  contents = f.read()
  return contents

def main():
 if len(argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

 book_path = sys.argv[1]
 text = get_book_text(book_path)
 num_of_words = count_words(text)
 num_of_chars = num_characters(text)
 sorted_dict = sort_dict(num_of_chars)
 
 print("============ BOOKBOT ============")
 print(f"Analyzing book found at {book_path}")
 print("----------- Word Count ----------")
 print(f"Found {num_of_words} total words")
 print("--------- Character Count -------")
 for dict in sorted_dict:
  if dict['char'].isalpha():
   print(f"{dict['char']}: {dict['num']}")
 print("============= END ===============")


main()

