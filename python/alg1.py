
def Deler_vowel(St):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    st1=""
    for let in St:
        if let not in vowels:
            st1 += let
    return st1

A = Deler_vowel("Hello word!")
print(A)