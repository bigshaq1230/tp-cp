x = input().split()  # O(n) Get input and split it into a list of cards

l = []  # O(1) Initialize an empty list to store card values
sum = 0  # O(1) Initialize sum of card values
type = ""  # O(1) Variable to store the suit of the first card

# Function to resolve card values based on face value or rank
def resolve(c):
    if c.isnumeric():  # O(1) If it's a number, return the integer value
        return int(c)
    else:
        if c == "T":  # O(1)
            return 10
        elif c == "J":  # O(1)
            return 11
        elif c == "Q":  # O(1)
            return 12
        elif c == "K":  # O(1)
            return 13
        elif c == "A":  # O(1)
            return 14

ace = False  # O(1)
state = True  # O(1)
type = x[0][1]  # O(1)

for i in x:  # O(n) Loop through each card in the input list
    if type != i[1]:  # O(1) Always check if same suit
        state = False  # O(1)
        print("NO")  # O(1)
        break  # O(1)

    if i[0] == "A":  # O(1) Check if the card is an Ace
        ace = True  # O(1)

    card_number = resolve(i[0])  # O(1) Get value of card
    l.append(card_number)  # O(1)
    sum += card_number  # O(1)

if state:  # O(1) If all cards are of the same suit
    l.sort()  # O(n log n) Sort the card values
    sum_serie = (5 / 2) * (l[0] + l[-1])  # O(1) Calculate the sum of the series

    if sum_serie != sum:  # O(1)
        if ace:  # O(1) If there's an Ace, try using Ace as 1 instead of 14
            l.pop()  # O(1) Remove Ace (14) from the list
            l.insert(0, 1)  # O(n) Insert Ace (1) at the beginning
            sum_serie = (5 / 2) * (l[0] + l[-1])  # O(1) Recalculate the series sum
            sum = sum - 13  # O(1) Adjust the total sum by subtracting (14 - 1)

            if sum_serie == sum:  # O(1) 
                print("YES")  # O(1)
            else:
                print("NO")  # O(1)
    else:
        print("YES")  # O(1)
