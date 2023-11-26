alien_0 = {'color': 'green', 'points': 5}
print(f"The alien is colored {alien_0['color']}.")
print(f"The alien is worth {alien_0['points']} points.")

# A new one for the next example
alien_0 = {'color': 'green'}
print(f"\nThe new alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Now with more properties
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
    
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Remove a key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(f"\nBefore deleting points: {alien_0}")

del alien_0['points']
print(f"\nAfter deleting points: {alien_0}")

# Start with an empty dictionary
alien_0 = {}
print(f"\nStarted with an empty dictionary: {alien_0}")
alien_0['color'] = 'green'
alien_0['points'] = 5
print(f"Final alien_0: {alien_0}")