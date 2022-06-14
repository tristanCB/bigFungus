meta = {
        "Grow Guides": {
            "Grow-Guides": {
                "title": "Mushroom growing: Collective knowledge for growing mushrooms",
                "description" : "Growing mushrooms can be tricky. BigFungus provides you with all the necessary information needed to grow mushrooms indoor and outdoors. Whether you are searching for beginner techniques, obscure teks or anything of the like, bigfungus provides you with vetted protocols and established experience to grow your very own mushrooms at home."
            },
            "Identification": {
                "title": "Mushroom Identification: Easy to follow identification of mushrooms.",
                "description" : "Identifying mushrooms can be tricky. This page is a beginner friendly, ready to use mushroom identification guide." 
            },
            "Equipment": {
                "title": "Mushroom growing equipment: Collective knowledge for mushroom growers",
                "description" : "Finding the proper equipment to start a new hobby can be tough. Myco-Net promotes mushrooms growing starter kits and various teks to expand your horizons as a mushroom grower."
            },
            "Recipes": {
                "title": "Mushroom recipes: Unbiased recipe collection for all mushroom enthusiasts",
                "description" : "Finding the perfect recipe to grow your produce is always challenging. This Tool gathers content from various cooking site and offers you with unbiased reviews."
            }
            },
        "Identification": {
                "title": "Mushroom Identification: Easy to follow identification of mushrooms.",
                "description" : "Identifying mushrooms can be tricky. This page is a beginner friendly, ready to use mushroom identification guide." 
            },
        "Products" : {
            "title": "BigFungus: Providing you with top tier mushroom strains and types.",
            "description" : "BigFungus provides you with the highest quality, clean, and affordable mushroom growing products to start you very own experience at home."
            },
    }

def getMeta() -> dict:
    return meta

def getPages() -> list:
    return [i for i in meta]