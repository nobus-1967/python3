def main():
    '''Convert binaty to decimal / decimal to binary.'''
    b = input('Enter a binary number: ')
    b_2_d = int(b, 2)
    print(f'Binary {b} is equal to {b_2_d} (decimal).')
    
    print()
    
    d = int(input('Enter a decimal number: '))
    d_2_b = str(bin(d)).lstrip('0b')
    print(f'Decimal {d} is equal to {d_2_b} (binary).')


if __name__ == '__main__':
    main()
