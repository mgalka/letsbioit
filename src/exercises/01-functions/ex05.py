def reverse_words(sentence):
    out = []
    for word in sentence.split():
        out.append(word[::-1])
    return ' '.join(out)

s = 'Quick brown fox'
print(reverse_words(reverse_words(s)))
print(reverse_words('Brave Sir Robin'))
