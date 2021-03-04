-------------------------------------------------------------
Dynamic programming
---------------------
memoization

fibonacci


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025

# memoized version


def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025

# --------------------------


def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)


print(gridTraveler(1, 1))  # 1
print(gridTraveler(2, 3))  # 3
print(gridTraveler(2, 3))  # 3
print(gridTraveler(3, 3))  # 6
# print(gridTraveler(18, 18)) # 2333606220

# -- Memoization - gridTraveler


def gridTraveler(m, n, memo=None):
    key = f"{m},{n}"
    if memo is None:
        memo = {}
    if key in memo.keys():
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]


print(gridTraveler(1, 1))  # 1
print(gridTraveler(2, 3))  # 3
print(gridTraveler(2, 3))  # 3
print(gridTraveler(3, 3))  # 6
# print(gridTraveler(18, 18)) # 2333606220


# -------------------------------

def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            return True
    return False


print(canSum(7, [2, 3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
# print(canSum(300, [7, 14])) # False


memoized version
-----------------


def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
# print(canSum(300, [7, 14])) # False

---------------------------------------


def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            return remainderResult
    return None


print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
# print(howSum(300, [7, 14])) # None

memoized version
-----------------


def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
    memo[targetSum] = None
    return None


print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None


--------------------


def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination is not None:
            remainderCombination = remainderCombination + [num]
            # combination = remainderCombination
            if shortestCombination == None or len(remainderCombination) < len(shortestCombination):
                shortestCombination = remainderCombination

    return shortestCombination


print(bestSum(7, [2, 3]))  # [3, 2, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))  # None
# print(bestSum(300, [7, 14])) # None

memoized version
-----------------


def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            remainderCombination = remainderCombination + [num]
            # combination = remainderCombination
            if shortestCombination == None or len(remainderCombination) < len(shortestCombination):
                shortestCombination = remainderCombination

    memo[targetSum] = shortestCombination
    return shortestCombination

# # m = target sum
# # n = len(numbers)

# # Brute Force
# # time: O(n^m * m)
# # space: O(m^2)


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [5, 3]
print(bestSum(8, [1, 4, 5]))  # [4, 4]
print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
print(bestSum(300, [7, 14]))  # None


--------------------------------------------


def canConstruct(target, wordBank):
    if target == "":
        return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank) == True:
                return True
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(canConstruct("skateboard", ["z", "ska", "rd", "bo",
                                  "ate", "t",  "sk", "boar"]))  # False
print(canConstruct("enterapotentpot", [
    "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False


memoized version
-----------------


def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo.keys():
        return memo[target]
    if target == "":
        return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(canConstruct("skateboard", ["z", "ska", "rd", "bo",
                                  "ate", "t",  "sk", "boar"]))  # False
print(canConstruct("enterapotentpot", [
    "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False


--------------------------


def countConstruct(target, wordBank):
    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        if target.find(word) == 0:
            numWaysForRest = countConstruct(target[len(word):], wordBank)
            totalCount += numWaysForRest
    return totalCount


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("skateboard", ["z", "ska", "rd", "bo",
                                    "ate", "t",  "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", [
    "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0


memoized version
-----------------


def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo.keys():
        return memo[target]
    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        if target.find(word) == 0:
            numWaysForRest = countConstruct(target[len(word):], wordBank, memo)
            totalCount += numWaysForRest
    memo[target] = totalCount
    return totalCount


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("skateboard", ["z", "ska", "rd", "bo",
                                    "ate", "t",  "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", [
    "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0

--------------------------------------------------


def allConstruct(target, wordBank):
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = [[word] + x for x in suffixWays]
            result.extend(targetWays)
    return result


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#     ['purp', 'le'],
#     ['p', 'ur', 'p', 'le']
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [
#     ['ab', 'cd', 'ef'],
#     ['ab', 'c', 'def'],
#     ['abc', 'def'],
#     ['abcd', 'ef']
# ]

print(allConstruct("skateboard", ["z", "ska",
                                  "rd", "bo", "ate", "t",  "sk", "boar"]))
# []

print(allConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
# [
#     ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
#     ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
#     ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
#     ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
# ]

print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaz",
                   ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []


memoized version
-----------------


def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo.keys():
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = [[word] + x for x in suffixWays]
            result.extend(targetWays)
    memo[target] = result
    return result


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#     ['purp', 'le'],
#     ['p', 'ur', 'p', 'le']
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [
#     ['ab', 'cd', 'ef'],
#     ['ab', 'c', 'def'],
#     ['abc', 'def'],
#     ['abcd', 'ef']
# ]

print(allConstruct("skateboard", ["z", "ska",
                                  "rd", "bo", "ate", "t",  "sk", "boar"]))
# []

print(allConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
# [
#     ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
#     ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
#     ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
#     ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
# ]

print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaz",
                   ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []

------------------------------------
Tabulation
fibonacci


def fib(n):
    table = [0] * (n+2)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))

-----------------
Gridtraveler tablutation
[[0]*(6+2) for x in range(6+2)]


def gridTraveler(m, n):
    table = [[0]*(n+1) for x in range(m+1)]

    table[1][1] = 1

    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j + 1] += current
            if i+1 <= m:
                table[i + 1][j] += current
    return table[m][n]


print(gridTraveler(1, 1))  # 1
print(gridTraveler(2, 3))  # 3
print(gridTraveler(3, 2))  # 3
print(gridTraveler(3, 3))  # 6
print(gridTraveler(18, 18))  # 2333606220

----------------------


def canSum(targetSum, numbers):
    table = [False]*(targetSum+1)
    table[0] = True

    for i in range(targetSum):
        if table[i] == True:
            for num in numbers:
                if i+num <= targetSum:
                    table[i + num] = True
    return table[targetSum]


print(canSum(7, [2, 3]))  # true
print(canSum(7, [5, 3, 4, 7]))  # true
print(canSum(7, [2, 4]))  # false
print(canSum(8, [2, 3, 5]))  # true
print(canSum(300, [7, 14]))  # false


--------------------------------------------


def howSum(targetSum, numbers):
    table = [None]*(targetSum+1)
    table[0] = []

    for i in range(targetSum):
        if table[i] is not None:
            for num in numbers:
                if i+num <= targetSum:
                    table[i + num] = table[i] + [num]
    return table[targetSum]


print(howSum(7, [2, 3]))  # [3,2,2]
print(howSum(7, [5, 3, 4, 7]))  # [4,3]
print(howSum(7, [2, 4]))  # null
print(howSum(8, [2, 3, 5]))  # [2,2,2,2]
print(howSum(300, [7, 14]))  # null


----------------------------------


def bestSum(targetSum, numbers):
    table = [None] * (targetSum+1)
    table[0] = []

    for i in range(targetSum):
        if table[i] is not None:
            for num in numbers:
                combination = table[i] + [num]
                if i+num <= targetSum:
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination
    return table[targetSum]


# print(bestSum(7, [2, 3]))  # [3,2,2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3, 5]
print(bestSum(8, [1, 4, 5]))  # [4,4]
print(bestSum(100, [1, 2, 5, 25]))  # [25,25,25,25]

-----------------------------------------


def canConstruct(target, wordBank):
    table = [False] * (len(target)+1)
    table[0] = True

    for i in range(len(target)):
        if table[i] is True:
            for word in wordBank:
                # if the word matches the characters starting at position i
                if i+len(word) <= len(target):
                    if target[i:i+len(word)] == word:
                        table[i+len(word)] = True
    return table[len(target)]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee", "eeeee"]))


------------------------------------


def countConstruct(target, wordBank):
    table = [0] * (len(target)+1)
    table[0] = 1

    for i in range(len(target)):
        for word in wordBank:
            if i+len(word) <= len(target):
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += table[i]
    return table[len(target)]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
                     ["e", "ee", "eee", "eeee", "eeeee"]))  # 0

----------------------------------------


def allConstruct(target, wordBank):
    table = [[] for x in range(len(target)+1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in wordBank:
            if i+len(word) <= len(target):
                if target[i:i+len(word)] == word:
                    newCombinations = [x + [word] for x in table[i]]
                    table[i + len(word)].extend(newCombinations)

    return table[len(target)]


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
# [ 'purp','le'],
# ['p', 'ur', 'p', 'le']
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [
# [ 'ab','cd', 'ef'],
# ['ab', 'c', 'def'],
# ['abc', 'def'],
# ['abcd', 'ef']
# ]

print(allConstruct("skateboard", ["z", "ska",
                                  "rd", "bo", "ate", "t",  "sk", "boar"]))
# []

print(allConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
# [
# ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
# ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
# ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
# ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
# ]

# print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaz",
#    ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []
