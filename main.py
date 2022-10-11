from pprint import pprint
import csv
import re



with open("phonebook_raw.csv", encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    contact_list = list(rows)

lastname_ = []
firstname = []
surname_ = []
phone_ = []
organization = []
position = []
email_ = []
headings = {}
contact_list_New = []


def names_():
    pattern = '[а-яёА-ЯЁ]*'
    pattern1 = r'(\w+)'
    pattern_2 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'    
    pattern_3 = r'[а-яёА-ЯЁ]*\s[а-яёА-ЯЁ]*'
    for names in contact_list:
        if names[0] == 'lastname':
            contact_list_New.append(names)
        result1 = re.search(pattern1, names[0])
        result = re.search(pattern_2, names[0])
        result_2 = re.match(pattern1, names[1])
        result_3 = re.search(pattern_3, names[0])
        result4 = re.search(pattern_2, names[0])
        result5 = re.match(pattern_3, names[1])
        result6 = re.search(pattern, names[2])
        if result1.group(0) != 'lastname':
            lastname_.append(result1.group(0))
        if names[1] == 'firstname':
            pass
        elif result is not None:
            firstname.append(result.group(0).split(" ")[1])
        elif result_3:
            firstname.append(result_3.group(0).split(" ")[1])
        else:
            firstname.append(result_2.group(0))
        if names[2] == 'surname':
                pass
        elif result4 is not None:
                surname_.append(result4.group(0).split(" ")[2])
        elif result5 is not None:
                surname_.append(result5.group(0).split(" ")[1])
        else:
                surname_.append(result6.group(0))    
names_()


def phones_():
    pattern = r'(\+7|8)+\s?\(?(\d{3})\)?\D?(\d{3})\D?(\d{2})\D?(\d{2})\s?\(?(доб.)?\s?(\d*)'
    for phone in contact_list:
        result = re.search(pattern, phone[5])
        if phone[5] == "phone":
            continue
        elif result is None:
            phone_.append("")
        elif result.group(6) is not None:
            phone_.append(
                f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)} доб.{result.group(7)}')
        else:
            phone_.append(f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)}')
phones_()


def organization_():
    pattern = '.*'
    for org in contact_list:
        result = re.search(pattern, org[3])
        if org[3] == 'organization':
            continue
        elif result is None:
            organization.append("")
        else:
            organization.append(result.group(0))
organization_() 


def position_():
    pattern = '.*'
    for pos in contact_list:
        result = re.search(pattern, pos[4])
        if pos[4] == 'position':
            continue
        elif result is None:
            position.append("")
        else:
            position.append(result.group(0))
position_()


def email():
    pattern = '.*'
    for mail in contact_list:
        result = re.search(pattern, mail[6])
        if mail[6] == 'email':
            continue
        elif result is None:
            email_.append("")
        else:
            email_.append(result.group(0))         
email()
def contact_list_():
    for i in range(len(lastname_)):
        Family_name = lastname_[i], firstname[i] 
        if Family_name not in headings:
            headings[Family_name] = surname_[i], organization[i], position[i], phone_[i], email_[i]
        else:
            headings[Family_name] += position[i], phone_[i], email_[i]    
    for item in headings.items():  
        contact_list1 = item[0] + item[1]
        contact_list_New.append(contact_list1)
contact_list_()


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list_New)

