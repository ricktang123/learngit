#!/usr/bin/env python
def anti_vowel(text):
    textnew=''
    for i in text:
        if not (i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
            textnew=textnew+i
    return textnew

print anti_vowel('please')

