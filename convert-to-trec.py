# -- coding: utf-8 --
import json
import sys
import getopt


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
    with open(inputfile) as fin, open(outputfile, 'w') as fout:
        for line in fin:
            news_article = json.loads(line)
            trecdoc = u"<DOC>\n"
            trecdoc += u"<DOCNO>{}</DOCNO>\n".format(news_article["id"])
            trecdoc += u"<SOURCE>{}</SOURCE>\n".format(news_article["source"])
            trecdoc += u"<MEDIATYPE>{}</MEDIATYPE>\n".format(news_article["media-type"])
            trecdoc += u"<PUBLISHED>{}</PUBLISHED>\n".format(news_article["published"])
            trecdoc += u"{}\n".format(news_article["content"])
            trecdoc += u"</DOC>\n"
            try: # py27
                fout.write(trecdoc.encode('utf-8'))
            except TypeError: # py34
                fout.write(trecdoc)

if __name__ == "__main__":
    main(sys.argv[1:])
