# write a python program to translate a message into secret code language. Use the rules below to trsanslate normal english into secreat code language,

# Codeing:
# If the word contains atleast 3 characters, remove the first letter and append it at the end now alppend three random chatacters at the starting and the end.
# else :
# simply revese the SyntaxWarning

# Decoding:
# If the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now the last letter and append it to the beginning.

# You program should ask wether you wantn to code or decode.

st = input("Enter Message: ")
words = st.split(" ")
coding = input("Enter '1' to Coding and '0' to Decoding: ")
coding = True if (coding == '1') else False
print(coding)
if(coding):
    nword = []
    for word in words:
        if(len(st)>=3):
         r1 = "xyz"
         r2 = "abc"
         stnew = r1 + word[1:]+word[0] + r2
         nword.append(stnew)
        else:
         nword.append(word[::-1])
    print(" ".join(nword))


else:
    nword = []
    for word in words:
        if(len(st)>=3):
         stnew = word[3:-3]
         stnew = stnew[-1] + stnew[:-1]
         nword.append(stnew)
        else:
         nword.append(word[::-1])
    print(" ".join(nword))

