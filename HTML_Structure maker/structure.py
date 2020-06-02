import os


def helpme():
    print('''
This app is made to make a rough structure of the webpage that the user is going to design. It has the following commands :\n
1. Section - It provides the <section> tag of HTML. It is used to divide a document into number of different sections. \n\tThere are two ways to us this here:
            a. inside mode - In this mode all the other tags used will be inside a section untill the user exits the app.
            b. outside mode - In this mode the all the other tags used will be outside a section untill the user exits the app.
            Usage:   section <inside/outside> <text-for-making-id> 
            Example: section outside this_is_section_no._1
2. Heading - It uses the heading(h1,h2,h3,h4,...) tags of HTML. It is used to give a heading on the webpage.
            Usage:   heading <type of heading> <heading-text>
            Example: heading h2 My heading text
3. Content - It uses the <p> tag of HTML. It is used to provide a paragraph to the webpage.
            Usage:    content <text-for-content>
            Example:  content some lorem ipsum maybe.
4. Table - It uses the <table> tag of HTML. It is used to make table for the webpage. Enter the number of rows then number of columns.
        After that enter the headings, Number of columns = Number of headings and No of rows include the heading row. 
            Remember to separate different headings with a comma(,).
            Usage:  table <no-of-rows> <no-of-columns>
                    Enter headings -> < headings separated with space >
                    Enter row <count> -> < row elements separated with space >
            Example: table 3 3
                    Enter headings -> Company,Contact,Country
                    Enter row 1 -> Alfreds Futterkiste,Maria Anders, Germany
                    Enter row 2 -> Centro comercial Moctezuma,Francisco Chang,Mexico
5. Image - It uses the img tag of HTML. It is used to provide a image to the webpage. HTML do not like whitespace use _ or -
            Usage: image <source_of-image> <height> <width>
            Example: image big_gun.png 400 340
6. Link - It uses the a tag of HTML. It is used to provide a link in the webpage. 
            Usage: link <url> <text-to-click-on>
            Example: <a href="https://www.w3schools.com/html/">They helped me</a>
7. exit - This command is used to exit the application.
            Usage: exit''')


print("Sample text: \n\tLorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat, quas odit sequi cupiditate dicta eveniet, aut possimus unde nemo fugiat.")


# Functions

#  This functions sets the upper half of the HTML document
def starting_up(title_of_page):
    with open("index.txt", 'w') as f:
        f.write(
            f'<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{title_of_page}</title>\n\t</head>\n<body>')

#  This functions sets the lower half of the HTML document


def ending_now(mode="outside"):
    with open("index.txt", 'a') as f:
        if mode == "inside":
            f.write("\n\t</section>\n</body>\n</html>")
        elif mode == "outside":
            f.write("\n</body>\n</html>")
    if os.path.exists("index.html"):
        os.rename("index.txt", "index2.html")
    else:
        os.rename("index.txt", "index.html")

# Section tag


def makeSectionTag(sectionid='sectionTag', mode='outside'):
    text = f'\n\t<section id="{sectionid}">\n'
    with open("index.txt", 'a') as f:
        if mode == "outside":
            f.write(text+"\n\t</secton>")
        elif mode == "inside":
            f.write(text)

# Heading tag


def makeHeadingTag(type='h2', headingtext=" "):
    with open("index.txt", 'a') as f:
        f.write(f"\n\t<{type}>{headingtext}</{type}>")

# Content tag


def makeContent(para=" "):
    with open("index.txt", 'a') as f:
        f.write(f"\n\t<p>{para}</p>\n")

# Table tag


def makeTableTag(rows, columns, rowlist):
    with open("index.txt", 'a') as f:
        f.write("\n\t<table>\n\t<tr>\n\t\t<th>" +
                '</th>\n\t\t<th>'.join(rowlist[0])+"</th>\n\t</tr>")
        for i in rowlist[1::]:
            f.write("\n\t<tr>\n\t\t<td>" +
                    '</td>\n\t\t<td>'.join(i)+"</td>\n\t</tr>")

# Image tag


def makeImageTag(src=" ", height=300, width=300):
    with open("index.txt", 'a') as f:
        f.write(f'\n<img src={src} height="{height}" width="{width}" >')

# Link tag


def makeLinkTag(src, linktext):
    with open("index.txt", 'a') as f:
        f.write(f'\n<a href="{src}" target="_blank">{linktext}</a>')


title_of_page = input("Enter the title of the page: ")
starting_up(title_of_page)
commands = ["helpme", "section", "heading", "content",
            "table", "image", "link", "exit"]

flag = ''
while flag != "exit":
    print(f"Commands are: {', '.join(commands)}")
    query = input("command:  ").split(" ", 1)
    os.system('cls')
    if query[0].lower() == "helpme":
        helpme()
    elif query[0].lower() == "section":
        x = query[1].split(" ", 1)
        mode = x[0]
        sectionid = ''.join(x[1])
        makeSectionTag(sectionid=sectionid, mode=mode)
    elif query[0].lower() == "heading":
        x = query[1].split(" ", 1)
        makeHeadingTag(x[0], ''.join(x[1]))
    elif query[0].lower() == "content":
        makeContent(query[1])
    elif query[0].lower() == "table":
        rows = int(query[1][0])
        columns = int(query[1][-1])
        rowlist = []
        x = input("Enter table headings(separate with commas):  ").split(",")
        rowlist.append(x)
        for i in range(rows-1):
            rowdata = input(
                "Enter table rows(separate with commas):  ").split(",")
            rowlist.append(rowdata)
        makeTableTag(rows, columns, rowlist)
    elif query[0].lower() == "image":
        x = query[1].split(" ")
        src = x[0]
        height = x[1]
        width = x[2]
        makeImageTag(src, height, width)
    elif query[0].lower() == "link":
        x = query[1].split(" ", 1)
        src = x[0]
        text = ''.join(x[1])
        makeLinkTag(src, text)
    elif query[0].lower() == "exit":
        flag = "exit"
    else:
        print("Wrong input\nMaybe try typing helpme?")
ending_now()
