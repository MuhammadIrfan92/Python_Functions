

def longest_word(text):
    """generates list of words, with splitting parameter being space"""
    text = text.split(' ') 
    dic={}
    lent=0
    for i in text:
        lent=len(i)
        dic[lent]=i

    keys=dic.keys()
    max_key = max(keys)
    return dic[max_key]


if __name__ == "__main__":
    text = input('enter the string: \n')
    print(longest_word(text))
        
