import unicodedata

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


f = open('noEmailsToMailbox.txt', 'rb')
open('bigCleanMailbox.txt', "w")
unneddedEmailText = ["String1", "String12"];
for line in f:
    if not any(text in line for text in unneddedEmailText):
        if len(line) < 2000: #delete html/css code
            file = open("cleanEmails.txt", "a")
            file.write(line)
            file.close

f.close()
