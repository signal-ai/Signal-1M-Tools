import json
from pprint import pprint
import sys, getopt


def usage():
    print ("usage: convert-to-trec.py -i inputfile -o outputfile \n\n"+
           "                    inputfile: the original JSONL file of the dataset\n\n"+
           "Copyright (c) 2015 by Singal Media Ltd.")

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if not inputfile:
        usage()
        sys.exit()
    if not outputfile:
        usage()
        sys.exit()
    outfile = open(outputfile, 'w+')
    with open(inputfile) as f:
        for line in f:
            news_article=json.loads(line)
                #pprint(news_article)
            trecdoc = "<DOC>\n"
            trecdoc+= "<DOCNO>"+news_article["id"]+"</DOCNO>\n"
            trecdoc+= "<SOURCE>"+news_article["source"]+"</SOURCE>\n"
            trecdoc+= "<MEIDATYPE>"+news_article["media-type"]+"</MEDIATYPE>\n"
            trecdoc+= "<PUBLISHED>"+news_article["published"]+"</PUBLISHED>\n"
            trecdoc+= news_article["content"]+"\n"
            trecdoc+= "</DOC>\n"
            outfile.write(trecdoc.encode('utf-8'))
            outfile.flush()
        outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
