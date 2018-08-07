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


add_articles("brazil", "the wonders of south america", 4)
# add_articles("soccer", "while is real madrid the greatest", 10)
# add_articles("soccer", "while barcelone suck", 9)



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


def delete_article_by_topic(topic_name):
  session.query(Knowledge).filter_by(
    topic_name=topic_name).delete()
  session.commit()


def delete_all_articles():
  session.query(Knowledge).delete()
  session.commit()


def edit_rating(title,my_rating):
  article_object = session.query(
    Knowledge).filter_by(
    title=title).first()
  article_object.my_rating = my_rating
  session.commit()


def delete_article_by_rating(rating1):
  session.query(Knowledge).filter(Knowledge.my_rating<=rating1).delete()
  session.commit()

     

#print(query_article_by_primary_key(3))
#(delete_article_by_topic("soccer"))
#print(query_article_by_topic("soccer"))
#delete_all_articles()
#edit_rating("the wonders of south america", 9)
delete_article_by_rating(5)
print(query_all())










