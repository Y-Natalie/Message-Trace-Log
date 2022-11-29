file = input("What is the file name? (include .txt): ")
try:
    f = open(file, 'r')
except:
    print ("\n !! The file could not be found !! \n")
    file = input("Please input a file name that exists in the folder (include .txt): ")
    f = open(file, 'r')

output = file[:-4] + "_Delivered.txt"
internal = file[:-4] + "_Internal.txt"
domainSearch = input("What is the domain name? (include @): ")
DeliverEmail = set()
domainEmails = set ()
fo = open(output, 'w')
fi = open(internal, 'w')

for line in f:
    # Separate status from the email with , in one list
    separate = line.split(";")
    for i in separate:
        # Indivdual status with corresponding email in one list
        separate2 = i.split("##")
        # Status and email in separate list
        for j in separate2:
            if "Deliver" in i and "@" in j:
                DeliverEmail.add(j.strip())

for q in DeliverEmail:                
    fo.write(q + "\n")
    if domainSearch.lower() in q.lower():
        domainEmails.add(q.strip())
        fi.write(q + "\n")

print ("Number of distinct emails with status \"Delivered\": ", len(DeliverEmail))
print("Total number of", domainSearch, "emails: ", len(domainEmails))