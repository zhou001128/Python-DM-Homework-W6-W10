import numpy as np
import pandas as pd
df=pd.DataFrame(pd.read_excel('有效数据.xlsx'))
df_ESPN = df.loc[df['channel_title'].isin(['NBA'])]
df_ESPN.sort_values(by = 'video_id')
df1_ESPN = pd.DataFrame({"用户":[],
                    "总浏览数":[],
                   "总点赞数":[],
                   "总评论数":[],
                   "总视频数":[]
},
                   columns = ['用户', '总浏览数', '总点赞数', '总评论数', '总视频数'])
video_id = "agKDPntMv-E"
views = 0
likes = 0
comments = 0
videos = 0
for index, row in df_ESPN.iterrows():
    if row['video_id']==video_id:
        views += row['views']
        likes += row['likes']
        comments = row['comment_count']
        videos += 1
    else:
        df_insert = pd.DataFrame({"用户": [video_id],
                                   "总浏览数": [views],
                                   "总点赞数": [likes],
                                   "总评论数": [comments],
                                   "总视频数": [videos]})
        df1_ESPN = df1_ESPN.append(df_insert, ignore_index=True)
        video_id = row["video_id"]
        views = row['views']
        likes = row['likes']
        comments = row['comment_count']
        videos = 1
df1_ESPN.sort_values(by = '总视频数')
print(df1_ESPN)
writer = pd.ExcelWriter("频道用户数据分析.xlsx")
df1_ESPN.to_excel(writer, 'Jimmy Kimmel Live')
writer.save()
writer.close()