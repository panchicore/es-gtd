# es-gtd

The Global Terrorism Database (GTD) is an open-source database including information on terrorist events around the world from 1970 through 2016 (with annual updates planned for the future). Unlike many other event databases, the GTD includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 170,000 cases.

The goal of this repo is to index those 170K terrorist events into Elastic Search and explore its content with Kibana.

## Requirements
- Python
    - requests: `pip install requests`
- Elasticsearch
- Logstash

## Setup
1. Create index `python create_index.py`
2. The database is already in the repository on the `data` folder. No need to download more. Unzip database using `unzip Archive.zip`
3. Start the logstash ingest `logstash -f logstash/ls-gtd-pipeline.conf`

## Todo
