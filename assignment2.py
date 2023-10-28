
############
# Question 1
############

def reverseAndConcatenateString(s, i):
  rev = ""
  for x in range(len(s) - 1, -1, -1):
    # We stop at -1 since we want to include the first character at index 0 of the string (dont forget that the stopping point is exclusive)
    rev += s[x]

  return rev*i

print(reverseAndConcatenateString("hello", 3))

############
# Question 2
############

def rearrangeString(s):
  upper_case = ""
  lower_case = ""
  for x in s:
    if x == x.upper() and x != " ": #to not include spaces as the example shows
      upper_case += x
    elif x == x.lower() and x != " ":
      lower_case += x

  return upper_case + lower_case

print(rearrangeString("HEllo WorlD"))

############
# Question 3
############

#what we can do here is cast the string into a list and then use the .sort() function on the lists, then we can easily compare the sorted lists to see if they are equal or not
#if they are not equal the function will return False, otherwise True

def checkReordering(s1, s2):
  list1 = list(s1)
  list2 = list(s2)
  list1.sort()
  list2.sort()
  return list1 == list2 # This will return either True or False

print(checkReordering("hello", "lloeh"))

############
# Question 4
############

#Max

def findMax(l):
  highest = l[0] #it is better to set it to the first element than -999999999 since we cannot assume that the list does not have values less than -999999999
  for x in range(len(l)):
    if l[x] > highest:
      highest = l[x] #when we find a value higher than what we had stored, we repalce it with the new highest value

  return highest

print("The max value is: ", findMax([1,0,-99,8,64,3,1,-3]))

#Min

def findMin(l):
  lowest = l[0]
  for x in range(len(l)):
    if l[x] < lowest:
      lowest = l[x] #when we find a value lower than what we had stored, we repalce it with the new lowest value

  return lowest

print("The min value is: ", findMin([1,0,-99,8,64,3,1,-3]))

############
# Question 5
############

def sumDigits(n):
    if n == 0:
        return n
    return n%10 + sumDigits(n//10) # %10 gives us the last digit, //10 gives us everything except the last digit. Use them logically

print(sumDigits(123))


############
# Question 6
############

def removeConsecutiveDuplicates(s):
  if len(s) == 1:
    return s
  elif s[0] == s[1]:
    return removeConsecutiveDuplicates(s[1:]) #we are shortening the string each time to reach the base case by removing the character at index 0, also does NOT concatenate here since if a character is repeating consecutively we do not want to print it

  return s[0] + removeConsecutiveDuplicates(s[1:]) #also shortening string but also concatenating outside, so when the base case is reached it will keep returning and concatenating the string without the repeating consecutive characters


print(removeConsecutiveDuplicates("hhelooo    meez"))

####################
# Question 7 (Bonus)
####################

def reverseNumber(n):
  if n // 10 == 0:
    return n
  return (n % 10) * ((10)**((len(str(n))-1))) + reverseNumber(n // 10) #some fun math for you to look at :)

print(reverseNumber(44466611121))
