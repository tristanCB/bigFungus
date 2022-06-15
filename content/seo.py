meta = {
        "Products" : {
            "title": "BigFungus: Providing you with top tier mushroom strains and types.",
            "description" : "BigFungus provides you with the highest quality, clean, and affordable mushroom growing products to start you very own experience at home."
        },
        "Guides": {
            "title": "Mushroom growing: Collective knowledge for growing mushrooms",
            "description" : "Growing mushrooms can be tricky. BigFungus provides you with all the necessary information needed to grow mushrooms indoor and outdoors. Whether you are searching for beginner techniques, obscure teks or anything of the like, bigfungus provides you with vetted protocols and established experience to grow your very own mushrooms at home."
        },
        "Identification": {
            "title": "Mushroom Identification: Easy to follow identification of mushrooms.",
            "description" : "Identifying mushrooms can be tricky. This page is a beginner friendly, ready to use mushroom identification guide." 
        },
        "Home": {
            "title": "Growing mushrooms can be tricky. BigFungus provides you with all the necessary information needed to grow mushrooms indoor and outdoors. Whether you are searching for beginner techniques, obscure teks or anything of the like, bigfungus provides you with vetted protocols and established experience to grow your very own mushrooms at home.",
            "description" : "Mushroom growing: Collective knowledge for growing mushrooms",
        }
    }

def getMeta() -> dict:
    return meta

def getPages() -> list:
    return [i for i in meta if i != "Home"]