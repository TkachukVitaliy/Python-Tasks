# Створити програму, яка на вхід приймає рядок, та виділяє з нього всі числа в окремий масив,
# після чого програма друкує рядок без чисел. і масив чисел. 
# Змінити цей рядок таким чином, щоб кожне слово в ньому,починалось і закінчувалось великою літерою.
# Знайти максимальне значення в масиві чисел, 
# а всі інші числа піднести до степеню по їх індексу, та записати в інший масив.
import re 
array= input("\nВведіть початковий масив  ")
word = ''.join([x for x in array if not x.isdigit()])
number = re.findall(r'\d+', array) 
number = [int(i) for i in number] 
print("\nМасив з  слів  -", word)
print("\nМасив  з чисел -", number)

Uppword =''.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in word.split())
print ("Масив з слів , з великими літерами ", Uppword )

print ("Максимальний елемент масиву - ", max (number))

number.remove(max(number))
index_number = [number[i]**i for i in range(0,len(number))] 
print("Масив піднесений до степеню по їх індексу:",index_number)
print("\n")