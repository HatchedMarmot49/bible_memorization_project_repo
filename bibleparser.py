import re, json

def parsechapter(chapter):
    chapdict = {}
    f = open(chapter, "r", encoding="utf8")
    string = f.read()
    ref = re.findall("\d+", string)
    string = format(string)
    # string = re.sub("[\d+]", "\n", string)
    for ind in range(0, len(ref)-1):
        verse = string[string.find(ref[ind])+(len(str(ind+1))):string.find(ref[ind+1])].strip()
        chapdict[int(ref[ind])] = verse
    verse = string[string.find(ref[-1])+(len(str(ind+1))):].strip()
    chapdict[int(ref[-1])] = verse
    spl = chapter.split(".")
    out = open(spl[0]+".json", "w")
    json.dump(chapdict, out, indent=4)
    

def format(string):
    #get rid of brackets
    string = re.sub("\n", "", string)
    string = re.sub("\t","", string)
    string = re.sub("\u2014", "", string)
    string = re.sub("\u201d", "", string)
    string = re.sub("\u201c", "", string)
    string = re.sub("\[", "", string)
    string = re.sub("\]", "", string)
    string = re.sub("\(ESV\)", "", string).strip()
    return string


def theBigDog(file):
    bible_dict = {}
    f = open(file, "rb")
    bible = f.readlines()
    bible = [re.sub("\r\n", "", line.decode('utf-8')) for line in bible]

    for idx in range(len(bible)-1):
        x = 0
        current = 0
        curr_book = ''
        curr_chapter = 0
        #if is all upper, its a chapter heading
        if bible[idx].isupper():
            bible_dict[bible[idx]] = {}
            curr_book = bible[idx]
        #if p=5 and c=2, then we have an unneeded header
        elif current==5 and bible[idx+1]=='' and bible[idx+2]=='':
            continue
        #if we hit a footnote
        elif re.match(r'[\d+]', bible[idx]) or re.match('Chapter', bible[idx]):
            continue
        #we have an actual line
        else:
            #beginning of a chapter
            if ':' in bible[idx]:
                print(bible[idx])
            if re.match('\d+?:', bible[idx]):
                x+=1
                sublst = bible[idx].split(':', maxsplit=1)
                #remove colon
                curr_chapter = sublst[0]
                verse = sublst[1]
                bible_dict[curr_book][curr_chapter] = {}

        if bible[idx] =='':
            current+=1
        else:
            current = 0

    return bible_dict



print(theBigDog("resources/esvBible.txt"))