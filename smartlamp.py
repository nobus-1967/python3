# Define a class for a smart lamp can change (and reset) brightness and color:
class SmartLamp:
    """A class for a smart lamp."""
        
    def __init__(self):
        """Initialize a new lamp (off, brightness = 0%, color is white)."""
        self.on = False
        self._status = 'turned off'
        self.brightness = 0
        self.color = 'white'
        
        
    @property
    def on(self) -> bool:
        """Return the state of the lamp (on = True/off = False): getter."""
        return self._on
        
    @on.setter
    def on(self, value: bool):
        """Change the state of the lamp (on = True/off = False): setter."""          
        if not isinstance(value, bool):
            raise TypeError('Expected a boolean value!')
        
        self._on = value
        
        if value:
            self._status = 'turned on'            
        else:
            self._status = 'turned off'
            self._brightness = 0
            self._color = 'white'
            
        print(f'The smart lamp is now {self._status}!')
        
    @property   
    def brightness(self) -> int:
        """Return the brightness of the lamp (in %): getter."""
        return self._brightness   
    
    @brightness.setter
    def brightness(self, value: int):
        """Change the current brightness (if the lamp is on): setter."""
        if not isinstance(value, int):
            raise TypeError('Expected an integer!')
        
        if self._status == 'turned on':
            if value >= 0 and value <= 100:
                self._brightness = value
                
                print(f'Smart lamp\'s brightness is now {self._brightness}%.')
            else:
                print(f'Invalid value of brightness: {value}!')
                print('Right values: 0-100.')
        else:
            print(f'You can\'t change brightness while the lamp is {self._status}!')
                 
    @property   
    def color(self) -> str:
        """Return the color of the lamp (a string like 'white'): getter."""      
        return self._color
    
    @color.setter
    def color(self, value: str):
        """Change the current color (if the lamp is on): setter."""
        if not isinstance(value, str):
            raise TypeError('Expected a string!')
        
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
        info_1 = f'The smart lamp is {self._status}.\n'
        info_2 = f'Brightnes: {self._brightness}%, color: {self._color}.'
        
        return info_1 + info_2

# ----------------------------------------------------------------------
# Test our class:
smartlamp = SmartLamp()

print()

has_brightness = hasattr(smartlamp, 'brightness')
has_color = hasattr(smartlamp, 'color')
print(f'Has the oject an attribute "brightness"? {has_brightness}')
print(f'Has the oject an attribute "color"? {has_color}')

print()

print(smartlamp)

print()

smartlamp.on = True
smartlamp.on = False

print()

smartlamp.brightness = 100
smartlamp.on = True
smartlamp.brightness = -1
smartlamp.brightness = 50

print()

print(smartlamp)

print()

smartlamp.on = False
smartlamp.color = 'blue'
smartlamp.on = True
smartlamp.color = 'yellow'
smartlamp.color = 'orange'

print()

print(smartlamp)

print()

smartlamp.on = False

print()

print(smartlamp)
