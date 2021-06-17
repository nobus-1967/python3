import pickle

class Pocket():
    '''
    Create a blank store (a dictionary) for different keys & values.
    
    To add a key and a value, try 'obj.key = value'
    (where 'obj' is the name of your instance, 'key' and 'value' --
    names of new key and it's value).
    To get all keys & values, try 'vars(obj)' or 'obj.__dict__'.
    The class defines a special method too: 'obj.values()'.
    
    Also 'print(obj)' is usable for information (via '__repr__' method).
    
    To store a pocket, try 'obj.save()' (serialization using pickle).
    To load a pocket from .pickle-file, try 'load_pocket(filename)'.
    
    '''    
    def __init__(self, name):
        '''Initialize a new named pocket.'''
        self.name = name
        
        
    def values(self):
        '''Print all keys (including name) and values.'''
        dictionary = vars(self)
        
        for key, value in dictionary.items():
            print(f'{key}: {value}')
            
            
    def save(self):
        '''Save an instance (use the method of serialization).'''    
        with open('store_pocket.pickle', 'wb') as f:
            pickle.dump(self, f)
    
    
    def __repr__(self):
        '''Returns the name and a total number of keys (excluding name).'''
        info = f'A pocket "{self.name}". Total keys: {len(vars(self)) - 1}'
        
        return info
    

def load_pocket():
    with open('store_pocket.pickle', 'rb') as f:
        restored_mypocket = pickle.load(f)
    
    return restored_mypocket

# Test our class
mypocket = Pocket('My pocket # 1')     # Create a named instance
mypocket.email = 'my-email@email.com'  # Add a new value

print()

print(mypocket)    # Prints info about name and total of values (exclud. name)

print()

print(vars(mypocket))     # Returns a dictionary of all keys & values
print(mypocket.__dict__)  # Returns the same

print()

mypocket.values()  # Print all value (includ. name)

print()

mypocket.save()    # Serialize an instance into file
restored_mypocket = load_pocket() # Restore an instance from file
print(restored_mypocket)    # Check info of restored pocket
restored_mypocket.values()  # Check keys & values
