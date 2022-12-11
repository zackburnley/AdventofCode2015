import hashlib
inputValue = "bgvyzdsv"

addMe = 0
while not addMe == -1:
    addMe = str(addMe)
    testVal = inputValue + addMe
    result = hashlib.md5(testVal.encode())
    result = result.hexdigest()
    print(result, addMe)
    addMe = int(addMe)
    if result[:6] == "000000":
        print(result, str(addMe))
        break
    addMe += 1