

def sum_of_numbers():
    with open('day1/input.txt', 'r') as file:
       lista =  [lookup_for_number(line) for line in file]
       print(sum(lista))
       


def lookup_for_number(line):
    response= ""
    for i in line:
        if i.isdigit():
            response = response+i
    response = response[0]+response[-1]
    return int(response)

    


if __name__=='__main__':
    sum_of_numbers()