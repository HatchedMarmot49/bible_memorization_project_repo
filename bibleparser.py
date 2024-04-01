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


print(parsechapter("Genesis1.txt"))