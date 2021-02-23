# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 04:45:28 2019

@author: danie
"""

def Convert_Text(_string):
    """
    Define this function such that it takes in a simple 
    string such as "hello" and outputs the corresponding
    list of integers (ascii) for each letter in the word hello.
    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    """
    # list to contain ascii conversions, note 32 is space value 
    integer_list = []
    #looping through chracters of message
    for char in _string:
        #ord(char) will return the ascii value of string
        integer_list.append(ord(char))
    return integer_list


def Convert_Num(_list):
    """
    Do the opposite of what you did in the Convert_Text
    function defined above.
    
    Define this function such that it takes in a simple 
    string such as "hello" and outputs the corresponding
    list of integers for each letter in the word hello.
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
    #string to contain our ascii conversions back to characters
    _string = ''
    #looping through each number and converting back into character
    for i in _list:
        #chr(i) will convert ascii to character
        _string += chr(i)
    return _string


def FME(b, n, m):
    """
    1. Using the fast modular exponentiation algorithm.
    the below function should return b**n mod m.
    As described on page 254. (however, you may input the exponent and 
    then convert it to a string - the book verison imports the binary expansion)  
    2. You should use the function defined above
    Convert_Binary_String()
    3. Use this string to test which components are used in the calculation.
    4. Yes, there are many other ways to do this. I am asking you to do it this unusual way on purpose.
    """ 
    #list to store all keys, which are the exponents
    squar_map_key = []
    #list to store all values, exponentiated values mod m
    square_map_val = []
    #output of repeated square
    map_n = 0
    #power of repeated square
    map_n_pow = 0
    
    #while the squared power is less than or equal to the exponent at question (n) 
    while map_n_pow <= n:
        #exponentiate base by squared power and mod 7
        squar_map_key.append(map_n_pow)
        map_n = (b**map_n_pow)%m
        #append newly exponentiated value mod 7, to our reference map 
        square_map_val.append(map_n)
        #to incrument correctly, we need to account for 0 as 0 x 2 != 1
        if map_n_pow == 0:
            map_n_pow = 1
        else:
            map_n_pow = map_n_pow*2
            
    #creating map formatted as such "power : exponentiated value mod m"
    square_map_dict = {el:0 for el in squar_map_key}
    ind = 0
    for key, value in square_map_dict.items():
        square_map_dict[key] = square_map_val[ind]
        ind+=1
    
    

###### Finding possible combination of group sum to equal n (power in question) ######
    #out = is a list 1 and 0, 
    #where 1's resemble the number (at it's index position) is used in group sum
    out = find_combination(squar_map_key,n)
    
    #looping through list of 1's and 0's to convert into keys (exponents) 
    #being used in group sum and appending to list
    keys_used = []
    for i in range(0,len(out)):
        if out[i] == 1:
            keys_used.append(squar_map_key[i])

    #Table look up to see what values are at the keys used to create group sum of n
    val_used = []
    for key,val in square_map_dict.items():
        for element in keys_used:
            if key == element:
                val_used.append(val)
    
    # product of all values being used and mod 7 
    return ((np.prod(val_used))%m)
            
        
        
###### Finding possible combination of group sum to equal n (power in question) ######
import itertools
import numpy as np

#Source: https://codereview.stackexchange.com/questions/152988/find-smallest-subset-of-integers-having-a-given-sum
def find_combination(choices, total): 
    """
    Finding cartesian product of 0 and 1 (all uniqye combinations)
    Loop to multiply each bin of 1/0's (possible combinations)

    Return first combination list that equates to exponent n
    """
    bins = np.array(list(itertools.product([0, 1], repeat=len(choices))))
    combinations = [b for b in bins if sum(choices * b) == total]
    return (min(combinations, key=sum) if combinations else
            max([b for b in bins if sum(choices * b) < total], key=sum))



def Euclidean_Alg(a, b):
    """
    1. Calculate the Greatest Common Divisor of a and b.
    
    2. Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    The function must return a single integer 'x' which is
    the gcd of a and b.
    """
    #swapping a and b, if b greater than a 
    if a < b:
        temp = a
        a = b
        b = temp
    # continuously finding the remainder of a divided by b, replacing a with b & b with the remainder 
    while b > 0:
        k = a % b
        a = b
        b = k
    return a
    

import random
def Find_Public_Key_e(p, q):
    """
    Implement this function such that
    it takes 2 primes p and q.
    Using p and q, it should calculate:
    
    Use the gcd function that you have 
    defined before.
    
    The function should return 3 elements as follows:
    public key: n
    public key: e
    
    
    HINT: this function will run a loop to find e such 
    that e is relatively prime to (p - 1) (q - 1) 
    and not equal to p or q.
    """
    # Euclidean ald checks if p and q are relatively prime 
    if Euclidean_Alg(p,q) == 1:
        n = p*q
        phi_n = (p-1)*(q-1)
        #using random number generator to find a number relatively prime to phi_n 
        temp_e = random.randrange(1, phi_n)
        # continuously randomly  generate numbers until a postive relatively prime number (to phi_n) is found
        # the randomly generated number and n will be public key 
        for i in range(2,phi_n):
            if Euclidean_Alg(temp_e,phi_n) == 1 and temp_e > 0:
                e = temp_e
                return n,e
            else:
                temp_e = random.randrange(1, phi_n)


def Find_Private_Key_d(e, n):
    """
    Implement this method
    to find the decryption exponent d such that
    d is the modular inverse of e. 
    
    This will use the Extended Eucliean Algorithm
    
    This function should return the following:
    d: the decryption component.
    """
    
    b_0 = e
    m_0 = n
    s1 = 1
    t1 = 0 
    s2 = 0
    t2 = 1
    while m_0 > 0:
        
        # remainder of b divided by m 
        k = b_0%m_0
        # q = quotient of b mod m 
        q = b_0//m_0
        
        # substitution - making b the old m value & m the old k value   
        b_0 = m_0
        m_0 = k
        
        # substitution - making our 1st pair of weights equal to our 2nd par 
        s1_h, t1_h = s2, t2
        
        
        # calculating our Bezout coefficients
        s2_h = s1 - s2*q
        t2_h = t1 - t2*q
        
        # updating our 1st and 2nd set of coefficient values
        s1, t1 = s1_h, t1_h
        s2,t2 = s2_h, t2_h

        # if there is no remainder end this loop 
        # and return the inverse of e mod (p-1)(q-1) 
        if k == 0:
            return s1_h


def Encode(n, e, message):
    """
    Here, the message will be a string of characters.
    Use the function Convert_Text from 
    Second tool set and get a list of numbers.
    
    Encode each of those numbers using n and e and
    return the encoded cipher_text.
    """
    #list to contain the every charcter encrpyted 
    cipher_text = []
    #converts letters into numbers, specifically using ASCII mapping
    word_nums = Convert_Text(message)
    #looping through each ASCII letter 
    for word in word_nums:
        #Encrypting each ASCII letter and appending each letter to list
        cipher_text.append(FME(word, e, n))
    return cipher_text


def Decode(n, d, cipher_text):
    """
    Here, the cipher_text will be a list of integers.
    First, you will decrypt each of those integers using 
    n and d.
    Later, you will need to use the function that converts the integers to a string 
    defined in second toolset
    to recover the original message as a string. 
    """

    # string that will contain decoded message 
    message = ''
    # looping through each encrpyted charcter 
    for i in range(0,len(cipher_text)):
        # converting each encrypted charcter back to original mapped values (ASCII)
        cipher_text[i] = int((FME(cipher_text[i],d,n)))
    # converting from original mapping back to letter (ASCII > characters)
    message = Convert_Num(cipher_text)
    return message


def main():
    user_ans = 8
    while user_ans != '0':
        user_ans = input("Which of the following do you want to do? Get keys = 1, Encode = 2, Decode = 3, Exit = 0 \n")
        if user_ans == '1':
            p = int(input("You will need to choose 2 relatively prime numbers - Pick your 1st number (ex. 43) \n"))
            q = int(input("You will need to choose 2 relatively prime numbers - Pick your 2nd number(ex. 59) \n"))

            while Euclidean_Alg(p,q) != 1:
                print("You're 2 numbers are not relatively prime, try again")
                p = int(input("You will need to choose 2 relatively prime numbers - Pick your 1st number \n"))
                q = int(input("You will need to choose 2 relatively prime numbers - Pick your 2nd number \n"))
            print("Good Job! Your selections are relatively prime ")
            n_user,e_user = Find_Public_Key_e(p, q)
            d_user = Find_Private_Key_d(e_user, ((p-1)*(q-1)))
            print(n_user,d_user)
        
        elif user_ans == '2':
            message = input("enter your message you would like to encode: ")
            cipher_text_user = Encode(n_user, e_user, message)
            print("youre encoded message is: ", cipher_text_user)
        
        elif user_ans == '3':
            print("using your encoded message above")
            print(n_user,d_user,cipher_text_user)
            decoded_mes = Decode(n_user, d_user, cipher_text_user)
            print(decoded_mes)
            print("your decoded message is: ", decoded_mes)


if __name__ == '__main__':
    main()

    
    