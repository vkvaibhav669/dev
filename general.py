import os

#each website crawled will have a separe folder
def create_project_directory(dire):
    if not os.path.exists(dire):
        print("creating project" +  dire)
        os.makedirs(dire)

def create_data_files(project_name , base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    #it will be empty as it will have the links which will come from the waiting list  and join the already crawled links
#create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
#good practise to close the data to save some memory

#add data into an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#delete the content of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

#seting a set to ensure the unique links are only there and no duplicate
#avoid lists


#read a file and convert it into a set
def file_to_set(file_name):
    results = set()#empty set
    with open(file_name, 'rt')as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return results
#iterate through a set , each item will be a new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)









