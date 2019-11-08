from pydriller import RepositoryMining
import json
import csv

def commits():
    urls = ["https://github.com/IBM/mi-prometheus", "https://github.com/AmeyaDhavalikar/BRep", "https://github.com/IBM/kui"]
    url_no = 1
        
    open('data_gen/bugs_%s.csv' % url_no, 'w').close()
    open('data_gen/bugs_%s.json' % url_no, 'w').close()
    
    for url in urls:
        count = 0
        commit_data = []
        for commit in RepositoryMining(url).traverse_commits():
            # commit_data.append([commit.hash, commit.project_name, commit.author.name, commit.Modification.filename, commit.author_date, commit.author_timezone, commit.branches, commit.committer_date])

            if "bug" in commit.msg:
                #print("\tFixed a bug")
                commit_data.append([commit.hash, commit.project_name, commit.author.name, len(commit.modifications), commit.author_timezone, commit.branches, commit.committer_date])
                count += 1
        print ("# of bugs fixed: ", count)

        myfile = open("data_gen/bugs_%s.csv" % url_no, "a")
        with myfile:
            writer = csv.writer(myfile)
            writer.writerows(commit_data)
        
        csvfile = open('data_gen/bugs_%s.csv' % url_no, 'r')
        jsonfile = open('data_gen/bugs_%s.json' % url_no, 'a')
        fieldnames = ("commit.hash", "commit.project_name", "commit.author.name", "len(commit.modifications)", "commit.author_timezone", "commit.branches", "commit.committer_date")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')
        url_no += 1

if __name__=="__main__":
    commits()
