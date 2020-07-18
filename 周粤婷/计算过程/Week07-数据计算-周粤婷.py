import numpy as np
import pandas as pd
df=pd.DataFrame(pd.read_excel('有效数据.xlsx'))
df1 = pd.DataFrame({"频道":[],
                    "总浏览数":[],
                   "总点赞数":[],
                   "总评论数":[],
                   "总视频数":[],
                    "条均浏览数":[],
                   "条均点赞数":[],
                    "条均评论数":[],
                    "月均视频数":[]
},
                   columns = ['频道', '总浏览数', '总点赞数', '总评论数', '总视频数',"条均浏览数","条均点赞数","条均评论数",'月均视频数'])
channeltitle = "12 News"
videos = 1
views = 85643
likes = 170
comments = 0
for index, row in df.iterrows():
    if row['channel_title']==channeltitle:
        views += row['views']
        likes += row['likes']
        comments += row['comment_count']
        videos += 1
    else:
        everyviews = views/videos
        everylikes = likes/videos
        everycomments = comments/videos
        everyvideo = videos/8
        df1_insert = pd.DataFrame({"频道": [channeltitle],
                                   "总浏览数": [views],
                                   "总点赞数": [likes],
                                   "总评论数": [comments],
                                   "总视频数": [videos],
                    "条均浏览数":[everyviews],
                   "条均点赞数":[everylikes],
                    "条均评论数":[everycomments],
                                   "月均视频数":[everyvideo]}, )
        df1 = df1.append(df1_insert, ignore_index=True)
        channeltitle = row["channel_title"]
        views = row['views']
        likes = row['likes']
        comments = row['comment_count']
        videos = 1
print(df1)
df1.to_excel('有效数据.xlsx', sheet_name='sheet2')


