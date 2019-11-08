import json
import requests
import csv

username = "amenon2"
token = "1eb20c64f34b8ca37ca9c2e2305605bab7b4c4c2"
sesn=requests.session()

def list_all_issues():

    url1 = "https://api.github.ncsu.edu/repos/adhaval/csc510-project/issues?state=closed"
    count_iss = 1
    number=[]
    names=[]
    createdat=[]
    closedat=[]
    closedby=[]
    authenticatn = sesn.get(url1, auth=(username, token))

    print("Task 1")
    print("list of issues fixed:")
    for list_issues in authenticatn.json():
        #print(list_issues)

        number.append(list_issues['number'])
        names.append(list_issues['title'])
        createdat.append(list_issues['created_at'])
        closedat.append(list_issues['closed_at'])
        closedby.append(list_issues['user']['login'])



    issuedata=list(zip(number,names,createdat,closedat,closedby))
        
    open('data_gen/issues_%s.csv' % count_iss, 'w').close()
    myfile = open("data_gen/issues_%s.csv" % count_iss, "w")
    with myfile:
        writer = csv.writer(myfile)
        writer.writerows(issuedata)
    
    count_iss += 1

if __name__=="__main__":
    list_all_issues()
