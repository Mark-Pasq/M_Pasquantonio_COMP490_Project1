from feed_to_sqlite import ingest_feed

url = f' https://stackoverflow.com/jobs/feed'

ingest_feed("feeds.db", url=url, table_name="links")
