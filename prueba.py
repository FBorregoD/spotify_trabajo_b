from xml.etree.ElementInclude import include
import zipfile
import os
import pandas as pd


zipname= "data.zip"
pathstr="./spotify"
zippath=pathstr+"/"+zipname
flist=['artists_norm.csv','albums_norm.csv','tracks_norm.csv']
print("List of items in the directory before extraction")
for item in os.listdir(path=pathstr):
    print(item)
print("\n\n")
#opening the zip file in read mode.
#Extracting all the content of the zip file in current working directory.    
with zipfile.ZipFile(zippath,"r") as zf:
    zf.extractall(path=pathstr,members=flist)
#Printing list of item in the current working directory before extracting contents 
print("List of items in the directory after extraction")    
for item in os.listdir(path=pathstr):
    print(item)  

df_artist=pd.read_csv(pathstr+"/"+flist[0], sep=";", index_col=False)
print(df_artist.head())
print(df_artist.describe(include="all"))

df_album=pd.read_csv(pathstr+"/"+flist[1],sep=";", index_col=False)
print(df_album.head())
print(df_album.describe(include="all"))
df_tracks=pd.read_csv(pathstr+"/"+flist[2],sep=";", index_col=False)
print(df_tracks.head())
print(df_tracks.describe(include="all"))
