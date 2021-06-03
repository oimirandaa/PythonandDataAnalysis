#The Hamming distance is a metric for comparing two binary data strings. While comparing two 
#binary string of equal length, Hamming distance is the number of bit positions in which the 
#two bits are different
#It is use for error detection or error correction when data is transmitted ober computer
#networks. It is also using in coding theory for comparing equal length data words.

def hammingDistance(s1, s2):
    i = 0

    if len(s1) != len(s2):
        print("The strings are different sizes, please enter same size strings")
        exit()

    for _ in range(len(s1)):
        if s1[_] != s2[_]:
            i += 1

    return i
