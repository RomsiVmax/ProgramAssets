with open("repository.iurl", "r") as repositoryurl:
    repositoryurl = repositoryurl.read()





link = repositoryurl

rurl = link.rfind('/') #rurl stands for repository URL




if rurl != -1:
    rnadg=link[rurl+1:] #rnadg stands for repository name and dot git
    rn = rnadg.rsplit(".", 1)[0]
    print(rn)
    
        
        




if rurl != -1:
    f = open("repository.name", "a")
    print(rn, file=f)
    f.close()
