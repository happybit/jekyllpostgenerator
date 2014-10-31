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
    
    with open(fileName, 'w+') as fin:
        fin.write("---\n")
        fin.write("layout: post\n")
        fin.write('title: "%s"\n' % postTitle)
        fin.write('date: %s %s\n' %(todayDate, currentTime))
        fin.write("comments: true\n")
        fin.write('categories: %s\n' % postCategory.capitalize())
        fin.write("---\n\n\n\n")
        fin.write("<!--more-->\n\n\n")
    
    fin.close()

    print('"%s" was created successfully.' % fileName)
    
if __name__ == "__main__":
    main(sys.argv)
