import random

#mix of:
# lower case letters;
# uppercase letters;
# numbers ;
# and symbols !"#$%&/ these things

# weak password: pick a word or two from a list


def password_generator():
        lowercaseLetters = ["happy", "key", "book", "platform", "plugin", "icon", "mac", "pc", "doug", "carrie", "arthur", "heaven", "yes"]
        uppercaseLetters = ["LIFE","SEA", "TRY", "GOAL", "FAMILY", "LOVE", "FLOWER", "SMILE", "YOU", "FRUIT", "SKY", "SEAGULL"]
        numbers = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
        symbols = ["!", "#", "$", "%", "&", "/", "(", ")", "?", "+", "*", "^", ".", ",", "-", "@"]
        password = str(random.choice(lowercaseLetters) \
                       +random.choice(uppercaseLetters)\
                       +random.choice(numbers)\
                       +random.choice(symbols))

        return password

print password_generator()
