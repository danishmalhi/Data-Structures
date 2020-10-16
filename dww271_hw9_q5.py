#Question 5






class InvertedFile:
    def __init__(self, file_name):
        self.file_object = open(file_name).read().split()
        self.indices_dict = {}
        
        indices =- 1
        for word in self.file_object:
            lst_indices = []
            indices += 1
            word = word.lower().strip(',.!?-_ ')
            if word not in self.indices_dict:
                lst_indices.append(indices)
                self.indices_dict[word]=lst_indices
                
            elif word in self.indices_dict:
                self.indices_dict[word].append(indices)

           
    def indices(self, word):
        word = word.lower().strip(',.!?-_ ')
        if word in self.indices_dict:
            return self.indices_dict[word]
        else:
            return []

def main():
    InvertedFile = InvertedFile("row_text.txt")
    print(InvertedFile.indices("Row"))
    print(InvertedFile.indices("Row! "))
    print(InvertedFile.indices("row"))
    print(InvertedFile.indices("spiderman"))
    print(InvertedFile.indices("the"))
#main()
