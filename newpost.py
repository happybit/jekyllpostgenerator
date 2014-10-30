#!/usr/bin/python2

import os
import sys
import time

#POST_PATH = "/path/to/your/posts/location/"

def main(argv):
    postTitle = argv[1]
    postCategory = argv[2]
    todayDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    currentTime = time.strftime('%H:%M',time.localtime(time.time()))
    
    fileNameWithoutDate = postTitle.lower().replace(' ', '-')
    fileName = todayDate + "-" + fileNameWithoutDate + ".markdown"
    # fileFullName = os.path.join(POST_PATH, fileName)
    
    fin = open(fileName, 'w+')

    fin.write("---\n")
    fin.write("layout: post\n")
    fin.write('title: "' + postTitle + '"\n')
    fin.write("date: " + todayDate + " " + currentTime  + "\n")
    fin.write("comments: true\n")
    fin.write("categories: " + postCategory.capitalize() + "\n")
    fin.write("---\n\n\n\n")
    fin.write("<!--more-->\n\n\n")
    
    fin.close()

    print('"' + fileName + '" was created successfully.')
    
if __name__ == "__main__":
    main(sys.argv)
