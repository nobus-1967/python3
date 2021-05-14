# Define a class for a smart lamp can change (and reset) brightness and color:
class SmartLamp:
    """A class for a smart lamp."""
        
    def __init__(self):
        """Initialize a new lamp (off, brightness = 0%, color is white)."""
        self._on = False
        self._status = 'turned off'
        self._brightness = 0
        self._color = 'white'
        
        
    def get_on(self) -> bool:
        """Return the state of the lamp (on = True/off = False): getter."""
        return self._on
        
        
    def set_on(self, value: bool):
        """Change the state of the lamp (on = True/off = False): setter."""
        self._on = value
        
        if value:
            self._status = 'turned on'            
        else:
            self._status = 'turned off'
            self._brightness = 0
            self._color = 'white'
            
        print(f'The smart lamp is now {self._status}!')
        
        
    def get_brigtness(self) -> int:
        """Return the brightness of the lamp (in %): getter."""
        return self._brightness
    
    
    def get_color(self) -> str:
        """Return the color of the lamp (a string like 'white'): getter."""      
        return self._color
        
    
    def set_brightness(self, value: int):
        """Change the current brightness of the lamp (if the lamp is on)."""
        if self._status == 'turned on':
            if value >= 0 and value <= 100:
                self._brightness = value
                
                print(f'Smart lamp\'s brightness is now {self._brightness}%.')
            else:
                print(f'Invalid value of brightness: {value}!')
                print('Right values: 0-100.')
        else:
            print(f'You can\'t change brightness while the lamp is {self._status}!')
                 
    
    def set_color(self, value: str):
        """Change the current color of the lamp (if the lamp is on)."""
        if self._status == 'turned on':
            if value in ['white',
                         'orange',
                         'red',
                         'purple',
                         'blue',
                         'green']:
                self._color = value
                
                print(f'Smart lamp\'s color is now {self._color}.')
            else:
                print(f'Invalid value of color: {value}!')
                print('Right values: white, orange, red, purple, blue, green.')
        else:
            print(f'You can\'t change color while the lamp is {self._status}!')
                
    
    def __repr__(self) -> str:
        """Display all conditions (variables) of the lamp."""
        text_1 = f'The smart lamp is {self._status}.\n'
        text_2 = f'Brightnes: {self._brightness}%, color: {self._color}.'
        
        return text_1 + text_2

# ----------------------------------------------------------------------
# Test our class:
smartlamp = SmartLamp()

print(smartlamp)

print()

smartlamp.set_on(True)
smartlamp.set_on(False)

print()

smartlamp.set_brightness(100)
smartlamp.set_on(True)
smartlamp.set_brightness(-1)
smartlamp.set_brightness(50)

print()

smartlamp.set_on(False)
smartlamp.set_color('blue')
smartlamp.set_on(True)
smartlamp.set_color('yellow')
smartlamp.set_color('orange')

print()

print(smartlamp)

print()

smartlamp.set_on(False)

print()

print(smartlamp)
