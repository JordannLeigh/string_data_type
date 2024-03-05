"""

start

Save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." as a single string
reprint sentence using replace () to change every '!' to a blank space
reprint the sentence in all capital letters using upper()
reprint the sentence in reverse

stop

"""


print ("The!quick!brown!fox!jumps!over!the!lazy!dog.")
# Save the sentence as a single string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Reprint sentence using replace() to change every '!' to ' '
print(sentence.replace("!" , " "))
# Save new sentence without '!' to new variable
new_sentence = (sentence.replace("!" , " "))
# Reprint entire sentence using upper()
print(new_sentence.upper())
# Save upper sentence to new variable
second_sentence = (new_sentence.upper())
# Reprint the sentence in reverse
print (second_sentence[::-1])