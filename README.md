# newpost.py

This is a tiny script written in Python to generate post template for Jekyll page.

## Usage

Enter the post name in double quotation marks and then category name followed like this:

    $ python2 newpost.py "This Is A New Post" PostCategory

A new file named as "2014-10-30-this-is-a-new-post.markdown" would be created in the same folder while the content displayed as below:

    ---
    layout: post
    title: "This Is A New Post"
    date: 2014-10-30 21:45
    comments: true
    categories: Postcategory
    ---
    
    
    
    <!--more-->
        
    
