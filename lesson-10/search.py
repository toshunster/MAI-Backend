from datetime import datetime
from elasticsearch import Elasticsearch

if __name__ == "__main__":
    #es_client = Elasticsearch(['https://user:secret@localhost:443']
    es_client = Elasticsearch()
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es_client.index(index="test-index", id=1, body=doc)
    res = es_client.search(index="test-index", body={"query": {"match_all": {}}})
    print(res)
