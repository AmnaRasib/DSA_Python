# : Python Regular Expressions
import re
text="The rain in Spain falls mainly in the plain."
# Find all words starting with 'S'
pattern=r"\bS\w+"
result=re.findall(pattern,text)
print("Words Starting with S: ",result)
# Replace 'rain' with 'snow'
modified_Text=re.sub(r"rain","snow",text)
print("Modified Text: ",modified_Text)

