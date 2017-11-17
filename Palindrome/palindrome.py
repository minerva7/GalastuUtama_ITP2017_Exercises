text = "kasurusak"
text = text.casefold()
rtext = reversed(text)
if list(text) == list(rtext):
 		print("this is a palindrome")
else:
        print("this is not a palindrome")

