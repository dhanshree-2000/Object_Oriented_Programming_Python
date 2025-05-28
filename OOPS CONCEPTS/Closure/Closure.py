def create_traffic_light():
    colors = ['red', 'green', 'yellow']

    def validate_color(color):
        if color not in colors:
            raise ValueError(f"Invalid color: {color}")
        else:
            return f"Color {color} is valid."
        
    return validate_color   ## This function returns a closure that validates traffic light colors.

# Example usage
traffic_light = create_traffic_light()
try:
    print(traffic_light('red'))      # Valid color
    print(traffic_light('blue'))     # Invalid color
except ValueError as e:
    print(e)
