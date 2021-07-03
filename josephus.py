# Josephus Problem (see https://en.wikipedia.org/wiki/Josephus_problem)
# with print() to visualize execution
from collections import deque

def main():
    '''Solve the Josephus problem (or Josephus permutation).'''
    n = int(input('Number of persons: '))
    k = int(input('Count for each step: ')) - 1

    list_of_persons = [num for num in range(1, n + 1)]
    deque_of_persons = deque(list_of_persons)
    print(f'\nStart: {list(deque_of_persons)}')
    
    if len(deque_of_persons) == 1:
        print('The person #1 remains')
    else:
        while len(deque_of_persons) > 1:
            deque_of_persons.rotate(-k)
            deque_of_persons.popleft()
            print(f'Rest:  {sorted(list(deque_of_persons))}')
        print(f'\nThe person #{deque_of_persons[0]} remains.')
        
        
if __name__ == '__main__':
    main()
