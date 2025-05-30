def count_words(text):
 content = text.split()
 num_words = 0
 for words in content:
  num_words += 1
 return num_words

def num_characters(text):
 lower_char = text.lower()
 chars_counted = {}
 for char in lower_char:
  if char in chars_counted:
   chars_counted[char] += 1
  else:
   chars_counted[char] = 1
 return chars_counted

def sort_dict(dictionary):
 sorted_list = []
 for char, count in dictionary.items():
  sorted_list.append({"char": char, "num": count }) 
  sorted_list.sort(reverse=True, key=sort_on) 
 return sorted_list

def sort_on(dict):
 return dict["num"]
