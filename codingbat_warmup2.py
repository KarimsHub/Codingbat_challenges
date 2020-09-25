
# 1. Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'
#def string_times(str, n):
#  return str * n


# 2. Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'
#def front_times(str, n):
#  front = str[:3]
#  if len(str) < 3:
#    return str * n
#  else:
#    return front * n


# 3. Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'
def string_bits(str):
  new_string = ''
  for i in range(len(str)):
    if (i % 2) == 0:
      new_string += str[i]
  return new_string


# 4. Given a non-empty string like "Code" return a string like "CCoCodCode".
#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'
def string_splosion(str):
  new_string = ''
  for i in range(len(str)):
    new_string += str[:i + 1]
  return new_string


# 5. Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2
def last2(str):
  number = 0
  last = str[-2:]
  for i in range(len(str) -2):
    if str[i] + str[i + 1] == last:
      number += 1
  return number