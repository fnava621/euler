import time


start = time.time()

singles = ['one', 'two', 'three', 'four', 
           'five', 'six', 'seven', 'eight', 'nine', 
           'ten', 'eleven', 'twelve', 'thirteen',
           'fourteen', 'fifteen', 'sixteen', 'seventeen',
           'eighteen', 'nineteen']


doubles = ['twenty', 'thirty', 'forty', 'fifty', 
           'sixty', 'seventy', 'eighty', 'ninety']

under_hund = []

for x in doubles:
    under_hund.append(x)
    for y in singles[0:9]:
        under_hund.append((x+" "+y))


hundreds = []

for x in singles[0:9]:
    h = x + " hundred"
    hundreds.append(h)
    for y in singles+under_hund:
        hundreds.append(h+ " and " + y)

hundreds.append('one thousand')
    


total = len(''.join(singles+under_hund+hundreds).replace(' ', ''))

elapsed = time.time() - start
 
print "%s found in %s seconds" % (total,elapsed)


    



