
def ask_value(letter):
    while True: 
        value = input(f'{letter} value : ')

        try:
            new_value = float(value)
            return new_value

        except: pass
        
def det_matrix():
    first_term = values["a1"]*(values["b2"]*values["c3"] - values["c2"]*values["b3"])
    second_term = values["a2"]*(values["b1"]*values["c3"] - values["c1"]*values["b3"])
    third_term = values["a3"]*(values["b1"]*values["c2"] - values["c1"]*values["b2"])
    determinant = first_term - second_term + third_term
    return determinant

def find_minor(position):
    minor_position = []
    for letter,num in user_letters:
        if letter not in position and num not in position:
            minor_position.append(letter + num)
            
    return minor_position

def minor_values(vectors):
    filter_values = []
    for x in vectors:
        if x in values.keys():
            filter_values.append(values[x])
            
    return filter_values
            
def new_values(old_values):
    return old_values[0]*old_values[3] - old_values[2]*old_values[1]

def show_ans():
    print("The inverse of the matrix above is : ")
    print(f"( {rounded_cofactors[0]}  {rounded_cofactors[3]}  {rounded_cofactors[6]} )")
    print(f"( {rounded_cofactors[1]}  {rounded_cofactors[4]}  {rounded_cofactors[7]} )")
    print(f"( {rounded_cofactors[2]}  {rounded_cofactors[5]}  {rounded_cofactors[8]} )")

print("This program will inverse the matrices of dimensions (3x3)")
print("Please enter the vlaues by referencng the diagram below")
print("( a1   a2   a3 )")
print("( b1   b2   b3 )")
print("( c1   c2   c3 )")

user_letters = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
values = {"a1":0,"a2":0,"a3":0,"b1":0,"b2":0,"b3":0,"c1":0,"c2":0,"c3":0}
minors = []
cofactors = []

for x in user_letters:
    values[x] = ask_value(x)

print("Your matrix is : ")
print("( " + str(values["a1"]) +"  "+ str(values["a2"]) +"  "+ str(values["a3"]) + " )")
print("( " + str(values["b1"]) +"  "+ str(values["b2"]) +"  "+ str(values["b3"]) + " )")
print("( " + str(values["c1"]) +"  "+ str(values["c2"]) +"  "+ str(values["c3"]) + " )")

det = det_matrix()
    
for x in user_letters:
    cap_values = (1/det)*new_values(minor_values(find_minor(x)))
    minors.append(cap_values)
    
for x in range(0,len(minors)):
    if x%2 == 1:
        cofactors.append(-minors[x])
        
    else:
        cofactors.append(minors[x])
        
rounded_cofactors = [round(elem,4) for elem in cofactors]
show_ans()