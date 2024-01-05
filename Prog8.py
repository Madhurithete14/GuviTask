#Anagram program takes string and returns true otherwise false

def check(s1, s2):
     
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams(True).") 
    else:
        print("The strings aren't anagrams(False).")         
         
# driver code  
s1 ="heart"
s2 ="earth"
check(s1, s2)