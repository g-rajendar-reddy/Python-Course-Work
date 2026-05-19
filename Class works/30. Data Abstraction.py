# Data Abstraction means hiding internal implementation details 
# and showing only the necessary features to the user.


from abc import ABC, abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass

class Photo(Content):
    def upload(self):
        print("Compressing photo...") 
        print("Uploading photo...") 
        print("Photo uploaded successfully!") 

class Video(Content):        
    def upload(self):
        print("Encoding video...") 
        print("Uploading video...") 
        print("Video uploaded successfully!")

class Reel(Content):
    def upload(self):
        print("Adding effects to reel...") 
        print("Uploading reel...") 
        print("Reel uploaded successfully!")    

All = [Photo(), Video(), Reel()]
for i in All:
    i.upload()             