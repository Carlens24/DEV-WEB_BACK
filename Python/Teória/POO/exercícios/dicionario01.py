emails = {
    "carlens" : "carlensoslin@gmail.com",
    "rose": "rosemiracle@gmail.com",
    "schneidine" : "schneidine@gmail.com",
    "cocodemaria" : "cocodemaria@gmail.com"
}
print(emails)
print("-" * 50)

for nomes in emails:
    print(nomes)
print("-" * 50)

for email in emails:
    mails = emails[email]
    print(mails)

emails.pop("cocodemaria")
print(emails.values())

print("-" * 50)
if "carlensoslin@gmail.com" in emails.values():
    print("Este email realmente existe")
else:
    print("Este email não existe na nossa lista de emails")