 
# 1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True
def sleep_in(weekday, vacation):
    if not weekday or vacation == True:
        return True
    else:
        return False


# 2. We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False
def monkeys(a_smile, b_smile):
    if a_smile and b_smile or a_smile is False and b_smile is False:
        return True
    else:
        return False


# 3. Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8
def sum(a, b):
    if a == b:
        return (a +b) * 2
    else:
        return a + b


#4. Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0
def diff(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n


#5. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False
def parrot_trouble(talking, hour):
  if talking and hour < 7 or talking and hour > 20:
    return True
  else:
    return False

#6. Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True
def makes10(a, b):
  if a == 10 or b == 10 or (a + b == 10):
    return True
  else:
    return False

#7. Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True
def pos_neg(a, b, negative):
  if (a < 0 and b > 0) and negative is Falsen or (a > 0 and b < 0) and negative is False:
    return True
  if negative and (a < 0 and b < 0):
    return True
  else:
    return False

#8. Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'
def not_string(str):
  if str[:3] == 'not':
    return str
  else:
    return 'not ' + str


#9. Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'
def missing_char(str, n):
  vorne = str[:n]
  hinten = str[n + 1:]
  return vorne + hinten


#10. Given a string, return a new string where the first and last chars have been exchanged.
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'
def front_back(str):
  if len(str) == 1:
    return str
  else:
    first = 0
    last = len(str)
    mid = str[first + 1:last - 1]
    return str[last - 1:] + mid + str[:first + 1]


#11. Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'
def front3(str):
  return str[0:3] * 3