from py2neo import Graph
graph = Graph(
    "http://192.168.2.130:7474",
    # database="academic-knowledge-graph",
    username="neo4j",
    password="Kddir@123456&"
)
CA_LIST = {"Person":0}
similar_words = {
    "孩子":"child",
    "父母":"parent",
    "配偶":"spouse",
    "兄妹":"sibling",
    "共同家长": "coparent"
}
