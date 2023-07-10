import pandas as pd

df=pd.read_csv("youtube-ing.csv")

result=df.head(10) #first 10 data

result=df[5:15].head #firts 5 data between of 5 to 15

result=df.columns #name of the columns

result=len(df.columns) #number of columns

#droping (thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date)
df=df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1) 


result=df["likes"].mean()  #avarage of likes
result=df["dislikes"].mean() #avarage of dislikes


result=df[["title","likes","dislikes"]].head(50)  #first 50 data of title,likes and dislikes

result=df[df["views"].max()==df["views"]]["title"].iloc[0] #the most views name of the video on data

result=df[df["views"].min()==df["views"]]["title"].iloc[0] #the least views name of the video on data

result=df.sort_values("views",ascending=False).head(10)[["title"]] #sort with views

result=df.groupby("category_id").mean("category_id").sort_values("likes",)["likes"]

result=df.groupby("category_id").sum().sort_values("comment_counts",ascending=False) #sorting as comment counts

result=df["category_id"].value_counts() #number of the each category 

df["lengt_title"]=df["title"].apply(len) #new columns creating for length of the title
result=df

df["lengt_tag"]=df["tags"].apply(len) #new columns creating for length of the tags
result=df


result=df.sort_values("likes",ascending=False)[["title","likes"]] #sorting the most from populer videos to least ones

print(result)