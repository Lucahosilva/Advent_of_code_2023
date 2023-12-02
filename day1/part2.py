
def sum_of_numbers():
    with open('day1/input.txt', 'r') as file:
       lista =  [lookup_for_number(line) for line in file]
       print(sum(lista))
       


def lookup_for_number(line: str):
    response= ""
    line =replace_letters(line)
    for i in line:
        if i.isdigit():
            response = response+i
    response = response[0]+response[-1]
    return int(response)


def replace_letters(line: str):
    line=line.lower()
    line = line.replace('one','one1one')
    line = line.replace('two','two2two')
    line = line.replace('three','three3three')
    line = line.replace('four','four4four')
    line = line.replace('five','five5five')
    line = line.replace('six','six6six')
    line = line.replace('seven','seven7seven')
    line = line.replace('eight','eight8eight')
    line = line.replace('nine','nine9nine')
    return line



if __name__=='__main__':
    sum_of_numbers()