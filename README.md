# Signal-1M-Tools

## Signal-1M-Convert-To-TREC
A script to convert the Signal Media One-Million News Articles Dataset to TREC format.
The TREC format allows researchers to index the dataset using popular Information Retrieval platforms such as http://terrier.org

###Running the script
After obtaining the dataset through this form http://goo.gl/forms/5i4KldoWIX, you can extract the JSONL file from the the downloaded Gzip file
Then you run the script like this

```
python convert-to-trec.py -i <path to signalmedia-1m.jsonl> -o <path to your outputfile>
```

## Indexing the dataset with Terrier
We recommend using the terrier.properties file included in this repository to index the dataset with Terrier
