def Fibonacci(n):
    if n ==0 or n==1:
       return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
  
n = int(input("Enter number of elements: "))
for i in range(0 , n):
    print(Fibonacci(i) , sep=",")

def PrimeNumber(nump):
    if nump < 2:
        return False
    for i in range(2, int(nump)):
        if nump % i == 0:
            return False
    return True

nump = float(input("Enter the number: "))
for i in range(int(nump)):
    if PrimeNumber(i):
        print(i, end=" , ")

            
sentence = input("Enter your sentence: ")
n = len(sentence)
vowel_count = 0
cons_count = 0
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
for char in sentence:
    if char.lower().isalpha():


      if char in vowels:
          vowel_count += 1
      else:
          cons_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {cons_count}")

def star(n):
    set = 1
    i = 0
    while i<n:
        spaces = n-i-1
        print(' '*spaces + '*'*set)
        set += 2
        i+=1
star(4)


    