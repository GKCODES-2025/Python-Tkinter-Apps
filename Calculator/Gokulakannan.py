class String:
    def __init__(self):
        self.uppercase = 0
        self.lowercase = 0
        self.vowel = 0
        self.consonant = 0
        self.space = 0
        self.string = ""

    def get_str(self):
        self.string = str(input("Enter a string: "))

    def count(self):
        for ch in self.string:
            if ch.isupper():
                self.uppercase += 1
            if ch.islower():
                self.lowercase += 1
            if ch == " ":
                self.space += 1
            if ch in "AEIOUaeiou":
                self.vowel += 1

        self.consonant = self.uppercase + self.lowercase - self.vowel

    def display(self):
        print("The string contains.....")
        print("%d Uppercase Letters" % self.uppercase)
        print("%d Lowercase letters" % self.lowercase)
        print("%d Vowels" % self.vowel)
        print("%d Consonants" % self.consonant)
        print("%d Spaces" % self.space)


S = String()
S.get_str()
S.count()
S.display()
