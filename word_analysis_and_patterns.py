# The following code will perform various analyses on a given list of words, to identify patterns 
# and characteristics such as vowel count, palindrome, and duplicate frequencies.

def magical_words(word_list):
  #Most Vowel Count

  vowels = ['a','e','i','o','u','A','E','I','O','U']
  vowel_count=dict.fromkeys(word_list,0)

  for key in vowel_count.keys():
    for char in key:
      if char in vowels:
        vowel_count[key]+=1

  Max_vowel=[]
  max_vowel=max(vowel_count.values())

  for key,value in vowel_count.items():
    if value==max_vowel:
      Max_vowel.append(key)

  Most_Vowel = min(Max_vowel)
  print("Highest Vowels:",Most_Vowel)

## Palindrome

  Palindrom_dict = dict.fromkeys(word_list,False)

  for key in Palindrom_dict.keys():
    if key.lower()==key.lower()[::-1]:
      Palindrom_dict[key]=True

  Palindrom_list=[]
  for key,value in Palindrom_dict.items():
    if value==True:
      Palindrom_list.append(key)

  if len(Palindrom_list)==0:
    print("Palindrome: None")
  else:
    print("Palindrome:",', '.join(Palindrom_list))

  # Count Duplicate Words
  lower_case = []
  for words in word_list:
    lower_case.append(words.lower())

  Duplicate_Dict = {}
  for word in lower_case:
    if word in Duplicate_Dict:
      Duplicate_Dict[word] += 1
    else:
      Duplicate_Dict[word] = 1

  Duplicate_List = []
  for word, count in Duplicate_Dict.items():
    if count >1:
      Duplicate_List.append(word)

  if len(Duplicate_List)==0:
    print("Duplicate Words: None")
  else:
    print("Duplicate Words:",', '.join(Duplicate_List))


magical_words(["california", "florida", "atlanta", "sweden", "delhi", "alavala", "CALIFORNIA"])
