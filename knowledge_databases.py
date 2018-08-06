from databases_lab import Base, Knowledge
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_articles(topic_name,title,my_rating):
  	article_object = Knowledge(
        topic_name=topic_name,
        title=title,
        my_rating=my_rating)
        session.add(article_object)
        session.commit()


add_articles("brazil", "the wonders of south america", 8)
add_articles("soccer", "while is real madrid the greatest", 10)
add_articles("soccer", "while barcelone suck", 9)



def query_all():
  k = session.query(
      Knowledge).all()
  return k



def query_article_by_topic(topic_name):
  k= session.query(
    Knowledge).filter_by(
    topic_name=topic_name).all()
  return k


def query_article_by_primary_key(topic_id):
  k= session.query(
    Knowledge).filter_by(
    topic_id=topic_id).all()
  return k




#print(query_all())
#print(query_article_by_topic("soccer"))
print(query_article_by_primary_key(1))








