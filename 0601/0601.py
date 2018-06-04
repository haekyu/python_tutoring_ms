f = open('sample.txt', mode='w')
f.write('hlasdhkj\n')
f.write('hlasdhkj\n')
f.write('hlasdhkj\n')
f.write('hlasdhkj\n')
f.write('hlasdhkj')
f.close()



f = open('sample.txt', mode='r')
while True:
    line = f.readline()
    print(line)
    if line == '':
        break

# lst = f.readlines()
# print(lst)
# print(f)
f.close()




# def fib_tail(n):
#     tail_toss()
#     return result


# # input: f(n - 2), f(n - 1)
# # output: f(n), new tails-> f(n - 1), f(n)

# def tail_toss(f_n_1, f_n_2):
#     f_n = f_n_1 + f_n_2
#     return f_n, f_n_1, f_n

# 1, 1, 2, 3, 5, ...

def fib_naive(n):
    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = fib_naive(n - 1) + fib_naive(n - 2)
    return result


# Dynamic programming
# input: 원래인풋, reservoir (dictionary)
# output: 원래 아웃풋, 업데이트 된 reservoir

def fib_dynamic(n, reservoir):

    # 초기조건
    if n == 0 or n == 1:
        result = 1
    # 재귀 식
    else:
        if n - 1 in reservoir.keys():
            f_n_1 = reservoir[n - 1]
        else:
            f_n_1, reservoir = fib_dynamic(n - 1, reservoir)

        if n - 2 in reservoir.keys():
            f_n_2 = reservoir[n - 2]
        else:
            f_n_2, reservoir = fib_dynamic(n - 2, reservoir)
        
        result = f_n_1 + f_n_2
    
    # reservoir update
    reservoir[n] = result

    return result, reservoir


fib_30, final_reservoir = fib_dynamic(30, {})

print(fib_30)
print(final_reservoir)


from collections import defaultdict

def classify_words(word_lst):
    # Initialize a word dictionary, whose
    #   - key: an alphabet
    #   - val: list of words starting from the key
    classifier = defaultdict(lambda: [])

    for word in word_lst:
        # lst = classifier[word[0]]
        # lst.append(word)
        classifier[word[0]].append(word)

    # Retrun the dictionary
    return classifier


word_lst = ["apple", "bear", "person", "aurora", "print", "boy"]
classifier = classify_words(word_lst)
print(classifier)


def classify_words_nodefault(word_lst):
    # Initialize a word dictionary, whose
    #   - key: an alphabet
    #   - val: list of words starting from the key
    classifier = dict()

    for word in word_lst:
        key = word[0]
        if key in classifier.keys():
            classifier[word[0]].append(word)
        else:
            classifier[word[0]] = [word]

    # Retrun the dictionary
    return classifier


