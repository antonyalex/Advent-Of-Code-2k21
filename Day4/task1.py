with open("C:\\Users\\anton\\OneDrive\\Desktop\\input.txt") as f:
    content = f.readlines()
calls=[int(x) for x in content[0].strip().split(',')]
cards = []
card = []
for line in content[2::]:
    if line.strip() == "":
        if len(card) > 0:
            cards.append(card)
            card = []
    else:
        card.append([int(x) for x in line.strip().split()])
cards.append(card)


def call_no(card, number):
    for r in range(len(card)):
        line = card[r]
        for c in range(len(line)):
            cell = line[c]
            if cell == number:
                card[r][c] = -1
    return card

def check(card):                                   
    for l in card:
        if l.count(-1)==len(l):
            return True
    for k in range(len(card[0])):
        c=0
        for l in card:
            if l[k]==-1:
                c+=1
        if c==len(l):
            return True
    return False



def card_sum(card):
    sum=0
    for l in card:
        for number in l:
            if number!=-1:
                sum+=number
    return sum

for call in calls:
    new_cards = cards.copy()
    for card in cards:
        card=call_no(card,call)
        if check(card):
            sum_final = card_sum(card)
            print(sum_final*call)
            print(sum_final,call)
            exit()
            




  






            
            

        
   
    
        

    
