# get required libraries
import pyperclip, requests, bs4

link = pyperclip.paste()

# load the gazette html page
print("Downloading roll numbers and pointers from copied link...")
res = requests.get(link)
res.raise_for_status()


print("Finding top 20 students...")
# parse and extract tag containing roll numbers
source = bs4.BeautifulSoup(res.text, features="html5lib")
elem = source.select("tr > td")[0]

# print("Finding top 20 students...")
# remove duplicates
data = list(set(elem.getText().split("\xa0")))

# clean up the list
for each in data.copy():
	if not each.startswith("3"):
		data.remove(each)

# convert into tuple containing roll no and pointer
tup = []
for each in data:
	if len(each[7:-1]) != 0:
		tup.append((float(each[7:-1]), int(each[:6])))

tup.sort(reverse=True)
top = tup[:20]
output = ""
for each in top:
	form = str(each[1]) + " (" + str(each[0]) + ")\n"
	output += form

pyperclip.copy(output)
print()
print(output)
print()
print("Done! Also copied to clipboard.")