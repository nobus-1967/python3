# Use string.punctuation for other symbols (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)
import string

def main() -> None:
    '''Run the main function-driver.'''
    print('This program analyzes the use of letters in a passage')
    print('from "Emma" by Jane Austen:\n')
    
    print('Emma Woodhouse, handsome, clever, and rich, with a comfortable home')
    print('and happy disposition, seemed to unite some of the best blessings of')
    print('existence; and had lived nearly twenty-one years in the world with')
    print('very little to distress or vex her [and so on]...')
    
    # 1. Get a dictionary of text sentences.
    text = input_text()
    
    # 2. Analyze sentences and return a dictionary of lettes's usage.
    stats = count_letters(text)
    
    # 3. Print statistics
    print_stats(stats)   
    

def input_text() -> list:
    '''Open file and return a text.'''
    file_text = list()
    
    with open('from_emma.txt', 'r') as fin:
        for line in fin:
            file_text.append(line.strip())
    
    return file_text


def count_letters(phrases: list) -> dict:
    '''Counts a usage of every letter and return as a dictionary.'''
    usage = dict()
    punkts = string.punctuation + string.whitespace
    
    for sentence in phrases:
        for symbol in sentence:
            if symbol not in punkts:
                if symbol not in usage:
                    usage[symbol.lower()] = 1
                else:
                    usage[symbol.lower()] += 1
    
    return usage
    

def print_stats(usage: dict) -> None:
    '''Print statistics sorted by letters.'''
    letters = sorted(list(usage.keys()))
    
    print('\nStatistics (letters in alphabetical order):')
    for letter in letters:
        print(f'\t{letter}: {usage[letter]:3d} times')


if __name__ == '__main__':
    main()
