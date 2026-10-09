import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))
print("Random User ID:", random_user_id())
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    
    characters = string.ascii_letters + string.digits
    ids = [''.join(random.choices(characters, k=num_chars)) for _ in range(num_ids)]
    
    return '\n'.join(ids)
def rgb_color_gen():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print("Random RGB Color:", rgb_color_gen())
def list_of_hexa_colors(count=1):
    return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(count)]
print("List of Hex Colors:", list_of_hexa_colors(3))
def list_of_rgb_colors(count=1):
    return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(count)]
print("List of RGB Colors:", list_of_rgb_colors(3))
def generate_colors(color_type, count):
    if color_type == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return "Invalid color type! Use 'hexa' or 'rgb'."
print("Generate Hexa (3):", generate_colors('hexa', 3))
print("Generate Hexa (1):", generate_colors('hexa', 1))
print("Generate RGB (3):", generate_colors('rgb', 3))
print("Generate RGB (1):", generate_colors('rgb', 1))
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled
print("Shuffled List:", shuffle_list([1, 2, 3, 4, 5]))
def unique_random_numbers():
    return random.sample(range(10), 7)
print("Unique Random Numbers (0-9):", unique_random_numbers())