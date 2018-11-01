def print_parse(aLine):
    print("The Parsed text is: ",aLine)

def parse_text(theText, aPattern, function):
    for line in theText.split():
        if aPattern in line:
            function(line)
           
       


    
