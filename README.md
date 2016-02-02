# Signal-1M-Tools

## What is the Signal 1M Dataset?

The [Signal Media One-Million News Articles Dataset](http://research.signalmedia.co/newsir16/signal-dataset.html) dataset by [Signal Media](http://signal.uk.com/) was released to facilitate conducting research on news articles. It can be used for submissions to the NewsIR'16 workshop, but it is intended to serve the community for research on news retrieval in general.

The articles of the dataset were originally collected by Moreover Technologies (one of Signal's content providers) from a variety of news sources for a period of 1 month (1-30 September 2015). It contains 1 million articles that are mainly English, but they also include non-English and multi-lingual articles. Sources of these articles include major ones, such as Reuters, in addition to local news sources and blogs.

## Getting Started

### Downloading the dataset

To obtain the dataset, follow the download link [here](http://research.signalmedia.co/newsir16/signal-dataset.html).


### Elasticsearch

[Elasticsearch](https://www.elastic.co/products/elasticsearch) is a powerful distributed RESTful search engine that can be used to store and index large amounts of data. At Signal, we use Elasticsearch to handle most of our search requests.

#### Installation

1. Download [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) and unzip.
2. Run `bin/elasticsearch` on Unix or `bin/elasticsearch.bat` on Windows.
3. Run `curl -X GET http://localhost:9200/`

At this point, Elasticsearch should be running locally on port `9200`. More information about Elasticsearch can be found at their [GitHub page](https://github.com/elastic/elasticsearch).

We advise that you use a tool to interact with Elasticsearch. Here are a few good ones:
* [Sense (Beta) Chrome Plugin](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig?hl=en)
* [Postman](https://www.getpostman.com/)

#### Creating an index

In order to store articles, you need to create an index. First, create an `articles` index:

```bash
curl -X PUT 'http://localhost:9200/articles'
```

or in Sense:

```javascript
PUT articles
```

#### Indexing the million articles

To index the million articles into Elasticsearch using python, first install [Requests](https://github.com/kennethreitz/requests/):

```bash
pip install requests
```

Then run:

```bash
python index_articles.py http://localhost:9200/articles ./million.jsonl
```

### TREC

#### Signal-1M-Convert-To-TREC
A script to convert the [Signal Media One-Million News Articles Dataset](http://research.signalmedia.co/newsir16/signal-dataset.html)  to TREC format.
The TREC format allows researchers to index the dataset using popular Information Retrieval platforms such as http://terrier.org

#### Running the script
After obtaining the dataset through this form http://goo.gl/forms/5i4KldoWIX, you can extract the JSONL file from the the downloaded Gzip file
Then you run the script like this

```bash
python convert-to-trec.py -i <path to signalmedia-1m.jsonl> -o <path to your outputfile>
```

#### Indexing the dataset with Terrier
We recommend using the terrier.properties file included in this repository to index the dataset with Terrier.
In your Terrier etc folder, add a text file "signal.spec" with one line containing the path to the file you created above (The TREC formatted dataset)
