import urllib.request as urllib2
import datetime


def download_data(input_url):
    file_in = urllib2.urlopen(input_url)
    return file_in


def process_data(filein):
    # result dictionary
    data_dict = {}
    data = filein.read().decode('utf-8')
    lines = data.split("\n")

    for line in lines[1:]:
        try:
            p_id = line.split(',')[0]
            p_name = line.split(',')[1]
            p_dob = line.split(',')[2]
            dob_data = p_dob.split('/')
            day = int(dob_data[0])
            month = int(dob_data[1])
            year = int(dob_data[2])
            dob_final = datetime.date(year, month, day)
            data_dict[p_id] = (p_name, dob_final)
        except Exception as e:
            print(f"Error parsing %s" % line)
    return data_dict


def display_person(p_id, person_data):
    if p_id in person_data:

        name = person_data[p_id][0]
        birthday = str(person_data[p_id][1])
        print("Person #%s is %s with a birthday of %s" % (p_id, name, birthday))

    else:
        print("No user found with that id")


url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

dataCSV = download_data(url)
resultDict = process_data(dataCSV)

display_person("14", resultDict)
