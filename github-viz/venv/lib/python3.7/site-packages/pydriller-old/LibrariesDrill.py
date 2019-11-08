from pydriller import RepositoryMining
import json
import csv

def libraries():
    urls = ["https://github.com/AmeyaDhavalikar/BRep"]
    lib_count = 1
        
    open('data_gen/libs_%s.csv' % lib_count, 'w').close()
    open('data_gen/libs_%s.json' % lib_count, 'w').close()
    
    for url in urls:

        comm = list(RepositoryMining(url, only_modifications_with_file_types=['.py']).traverse_commits())
            #print('Author {} modified a java file'.format(commit.author.name))
        for m in comm[-1].modifications:
            #print (m.filename)
                #print (m.source_code)
            x = m.source_code.split("\n")
            py_libs = []
            check_multiline_comment = False
            for line in x:
                words = line.split(" ")
                if words[0] == "#" or words[0] == "import" or words == [''] or words[0] == "\"\"\"" or words[0] == "\'\'\'" and not check_multiline_comment:
                    if words[0] == "import":
                        py_libs.append(["Python",words[1]])
                    if words[0] == "\"\"\"" or words[0] == "\'\'\'":
                        if not check_multiline_comment:
                            check_multiline_comment = True

                    continue
                elif words[0] == "\"\"\"" or words[0] == "\'\'\'" and check_multiline_comment:
                    check_multiline_comment = False
        
        #    print (py_libs)

        comm = list(RepositoryMining(url, only_modifications_with_file_types=['.java']).traverse_commits())
        for m in comm[-1].modifications:
            #print (m.filename)
                #print (m.source_code)
            x = m.source_code.split("\n")
            java_libs = []
            check_multiline_comment = False
            for line in x:
                words = line.split(" ")
                if words[0] == "//" or words[0] == "import" or words == [''] or words[0] == "//" or words[0] == "/*" or words[0]=="*/" and not check_multiline_comment:
                    if words[0] == "import":
                        java_libs.append(["Java",words[1]])
                    if words[0] == "/*" or words[0] == "*/":
                        if not check_multiline_comment:
                            check_multiline_comment = True
                    continue
                elif words[0] == "/*" or words[0] == "*/" and check_multiline_comment:
                    check_multiline_comment = False
        #     print (java_libs)

            comm = list(RepositoryMining(url, only_modifications_with_file_types=['.c']).traverse_commits())
            # print('Author {} modified a java file'.format(commit.author.name))
            for m in comm[-1].modifications:
                #print (m.filename)
                # print (m.source_code)
                x = m.source_code.split("\n")
                c_libs = []
                check_multiline_comment = False
                for line in x:
                    words = line.split(" ")
                    if words[0] == "#" or words[0] == "//" or words == [''] or words[0] == "/*" or words[0] == "*/" and not check_multiline_comment:
                        if words[0] == "#":
                            c_libs.append(["C", words[1]])
                        if words[0] == "/*":
                            if not check_multiline_comment:
                                check_multiline_comment = True
                        continue
                    elif words[0] == "*/" and check_multiline_comment:
                        check_multiline_comment = False
                #print (c_libs)


            comm = list(RepositoryMining(url, only_modifications_with_file_types=['.cpp']).traverse_commits())
            # print('Author {} modified a java file'.format(commit.author.name))
            for m in comm[-1].modifications:
                #print (m.filename)
                # print (m.source_code)
                x = m.source_code.split("\n")
                cpp_libs = []
                check_multiline_comment = False
                for line in x:
                    words = line.split(" ")
                    if words[0] == "#" or words[0] == "//" or words == [''] or words[0] == "/*" or words[0] == "*/" and not check_multiline_comment:
                        if words[0] == "#":
                            cpp_libs.append(["C++", words[1]])
                        if words[0] == "/*":
                            if not check_multiline_comment:
                                check_multiline_comment = True
                        continue
                    elif words[0] == "*/" and check_multiline_comment:
                        check_multiline_comment = False
                #print (cpp_libs)



        myfile = open("data_gen/libs_%s.csv" % lib_count, "a")
        with myfile:
            writer = csv.writer(myfile)
            writer.writerows(py_libs)
            writer.writerows(java_libs)
            writer.writerows(c_libs)
            writer.writerows(cpp_libs)


        csvfile = open('data_gen/libs_%s.csv' % lib_count, 'r')
        jsonfile = open('data_gen/libs_%s.json' % lib_count, 'a')
        fieldnames = ("Language", "Library")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

        lib_count += 1

if __name__=="__main__":
    libraries()
