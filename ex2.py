def count_a_occurrences(s):
    s_lower = s.lower()
    count = s_lower.count("a")
    exists = count > 0
    return exists, count
input_string = input("Digite uma string: ")
exists, count = count_a_occurrences(input_string)
if exists:
    print(f'A letra "a" ocorre {count} vez(es) na string,')
else:
    print("A letra 'a' não ocorre na string.")
