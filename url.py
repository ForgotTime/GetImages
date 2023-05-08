import random
from random import shuffle
def get_random_url():
    file = open("urls.txt", "r")
    ls = file.readlines()
    ls = [i.strip() for i in ls]
    return random.choice(ls)
def get_random_urls(num=10):
    file = open("urls.txt", "r")
    ls = file.readlines()
    ls = [i.strip() for i in ls]
    shuffle(ls)
    return ls[:num]
if __name__ == "__main__":
    url = get_random_url()
    print(url)
