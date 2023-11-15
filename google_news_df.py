from GoogleNews import GoogleNews
import pandas as pd

def google_news_df(per='1d',langu='es',reg='US',topic='python'):
  gn = GoogleNews(lang=langu,region=reg,period=per,encode='utf-8')
  gn.search(topic)
  news_items = gn.result()
  print(len(news_items))

  #topics_l=[]
  media = []
  date=[]
  titles = []
  texts = []
  links=[]

  for news in news_items:
    #topics_l.append(t.replace(' ',''))
    media.append(news['media'])
    date.append(news['date'])
    titles.append(news['title'])
    texts.append(news['desc'])
    links.append(news['link'])

  df = pd.DataFrame({'topic': topic, 'media': media,
                   'date': date, 'title': titles,
                   'text': texts, 'link': links
                   })
  
  return df
