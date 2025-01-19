sentence = "This sentence is a sentence"
sent = sentence.split()

print(sent)

res_string = ""

for i in range(len(sent)):
    if len(sent[i]) >= 5:
        res_string += sent[i][::-1]
    else:
        res_string += sent[i]

    if i != len(sent)-1:
        res_string += " "
    

print(res_string)