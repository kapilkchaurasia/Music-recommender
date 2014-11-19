import pandas as pd
from sklearn.cluster import KMeans
from datetime import datetime


##For every artist in artists_tags calculate the most frequently used tag.

mat=pd.read_csv('/home/kapil/Downloads/hw2data/artists-tags.txt',sep='|')
#mat1=mat.set_index('id')
mat1=mat[:1000]
mat3=mat.groupby('band_nm')
j=0
flag=0
MaxName=[]
df =pd.DataFrame(columns=('ArtistID', 'band_nm', 'tag'))
for i ,k in mat3:
    j=j+1
    if(j>18):
        flag=1
    else:
        if(flag==1):
            break
        else:
            #print mat3.get_group(i)['count'].max()
            MaxName=mat3.get_group(i)[['id','band_nm','tag']][mat3.get_group(i)['count'] == mat3.get_group(i)['count'].max()].values
            df.loc[j]=MaxName

df[:1]  



##loding the training data
table = pd.read_csv('/home/kapil/Downloads/hw2data/userart-mat-training.csv', delimiter=',')

##apply kmean on above loaded training data
startTime = datetime.now()
kmean=KMeans(init='random', n_clusters=5, n_init=10).fit(mat10)
print(datetime.now()-startTime)

#just checking training data cluster id's
#for k,v in x.iterrows():
#    k,v1= kmean.predict(v.ix[3:]),v['tag']
#    print k,v1

### Return a data structure that contains artist_id, artist_name, top tag, cluster_label for every artist
x= pd.merge(df,table, on='ArtistID', how='inner')

# Return a data structure that contains cluster_id, list of top 5 tags for every cluster
x1=x.groupby('cluster_id').sort('Tag',ascending=False).head(:5)

##predict the tag for test data

#load the test data
test_table = pd.read_csv('/home/kapil/Downloads/hw2data/userart-mat-test.csv', delimiter=',')
test_table1=test_table.set_index('ArtistID')
test_table1.shape

test_table2=test_table1[:100]

#predict the cluster id for test data
for k,v in test_table2.iterrows():
    lb=kmean.predict(v)
    print k,lb    
