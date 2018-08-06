from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
   __tablename__ = 'interesting_topics'
   topic_id = Column(Integer, primary_key=True)
   topic_name = Column(String)
   title = Column(String)
   my_rating = Column(Integer)

   def __repr__(self):
    if self.my_rating>7:	
      return ("the topic id is {}\n" 
      	       "if you want to learn about: {}\n"
               "you should look at the article called: {} \n"
               "the rating i gave this article is: {}").format(
                    self.topic_id, self.topic_name, self.title, self.my_rating) 
    else:
      return ("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon").format(
                    self.topic_name, self.title, self.my_rating)







