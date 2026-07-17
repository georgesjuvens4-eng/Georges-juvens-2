# a voir les structure de fichier dans le fichier readme 
pour afin de les cree pour que le program se lance 

# se fichier se trouve dans le docier interface_adapter


from framworks.a import A

class B : 

    def get1(self): 
        a = A()
        url = str (a.recevoir())

        # ajout https si absent 

        if not url.startswith("https://"):
            url_2 = "https://"+ url
        return url_2    
