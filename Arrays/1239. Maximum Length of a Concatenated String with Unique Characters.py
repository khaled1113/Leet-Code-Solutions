#how to make the special character 
arr =["aa","bb","c","d","ad"]
def repeated_values(string):
    duplicates =[]
    for letters in string:
        if string.count(letters)>1 and i not in duplicates:
            duplicates.append(letters)
        else:
          duplicates =[]
    return duplicates

for string in arr:
    duplicates =repeated_values(string)
    print(duplicates)
