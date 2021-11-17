from articles import Article
from utils import counter

print(
    """
    Shtyp 1 per te numeruar fjalet
    Shtyp 2 per te numeruar shkronjat

    Shtyp 0 per exit
    """
)

option = input().strip()
number_of_articles = int(input("Per sa artikuj: "))

general_list = []
for i in range(number_of_articles):

    a = Article()
    a.remove_nonchar()
    a.lower_case()

    if option == "1":
        words = a.list_words()
        chars = a.list_chars()
    elif option == "2":
        chars = a.list_chars()
        general_list += chars
    elif option == "0":
        continue

count_chars = counter(chars)

for char, counter in count_chars.items():
    print(f"{char} -> {counter}")

