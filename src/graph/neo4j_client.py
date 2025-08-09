from neo4j import GraphDatabase

class GraphClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def upsert_utterance(self, utt: dict):
        # TODO: implement MERGE statements with tier filtering
        pass
