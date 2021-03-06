def getProductsClean():
    products = [
    {
        "type":"Mushroom Tissue Culture",
        "subTypes": [
            {   "subType":"Medicinal",     
                "description": "May or may not extend your lifespan",
                "cost":22,
                "formMapping":"medicinal_tissue"
            },
            {   
                "subType":"Oyster",          
                "description": "Easy to grow",
                "cost":17,
                "formMapping":"oyster_tissue"

            },
            {        
                "subType":"Other",          
                "description": "An Assortment of types",
                "cost":15,
                "formMapping":"other_tissue"
            },        
        ],
    },
    {
        "type":"Growing Kits",
        "subTypes": [
            {   
                "subType":"Medicinal",     
                "description": "May or may not extend your lifespan",
                "cost":35,
                "formMapping":"medicinal_block"

            },
            {   
                "subType":"Oyster",          
                "description": "Easy to grow",
                "cost":22,
                "formMapping":"oyster_block"

            },
            {        
                "subType":"Other",          
                "description": "An Assortment of types",
                "cost":22,
                "formMapping":"other_block"

            },
            
        ],
    },
    {
        "type":"Beetle Feed",
        "subTypes": [
            {
                "subType":"Kinshi",     
                "description": "Tailored Nutrition for Beetles",
                "cost":35,
                "formMapping":"kinshi_block"
            }
        ]
    }
    ]
    return products

def getProducts():
    products = [
            {
                "name":"Tissue Culture",
                "alt_name":"Sterile mushroom tissue culture.",
                "price": 15.99,
                "price_code":"price_1KJrTLCzLXa9dokV5oMt4KJq",
                "uom":"unit",
                "image_url": "/product_images/tissueCulture.png",
                
                "image_url_desc": "/product_images/kingTransparent.png",

                "title_description": "Pure, Isolated Mycelium",
                "description": "Perfect for starting your very own grainspawn or liquid cultures.",
                "description2": "The Agar medium was made using a recipe similar to Sabouraud agar. Our proprietary blend of ingredients and high standard of cleanliness while manufacturing plates provides you with a guaranteed start to exploring a vast array of new mushroom strains. All batches are tested for possible baterial contamination.",

            },
        
            {
                "name":"Spawn",
                "alt_name":"Organic Rye Berry Grain Spawn",
                "price": 25.99,
                "price_code":"",
                "uom":"unit",
                "image_url": "/product_images/grainSpawn.png",
                
                "image_url_desc": "/product_images/grainSpawnCrossSection.jpg",
                "title_description": "Organic Rye Grain Spawn",
                "description": "Perfect for inoculating your very own bulk substrate. 1L masonjar, 3/4 full, fully colonized and ready to use",
                "description2": "On the left a cross section of grain can be seen. Because thr Mycelium is burried deep inside the grains, It can be broken vigorously and evenly mixed in bulk substrate for faster colonization.",

            },
        
            {
                "name":"Grow Kit",
                "alt_name":"Ready to fruit, fully colonized bulk substrate",
                "price": 39.99,
                "price_code":"price_1KJrOtCzLXa9dokVAfHJkTc3",
                "uom": "unit",
                "image_url": "/product_images/5lbsColonized.png",
                
                "image_url_desc": "/product_images/blackOysters.png",
                "title_description": "Ready To Fruit Fully Colonized",
                "description": "Includes one fully colonized artificial log grown in sterile mushroom grow bag. Can expect to get first harvest after keeping in humid environment for approximately two weeks.",
                "description2": "One the left a block of black oysters can be seen emerging from the block. The plastic top was cut off,the block was then kept in a humid environment exposed to some light.",

            },

            {
                "name":"Unicorn grow bag",
                "alt_name":"100 X heat tolerant plastic mushroom bags",
                "image_url": "/product_images/T4GrowBag.jpg",
                "price": 199.99,
                "price_code":"price_1KJrXXCzLXa9dokVOlH6E10g",
                "uom":"unit",
                "description": "Model T4. Comes in bundle of 100. Made in the USA and have .3 micron filter patches. 100 bags per unit.",

            },
            {
                "name":"Liquid Culture",
                "alt_name":'Mycelial Suspension',
                "uom":"unit",
                "image_url": "/product_images/liquidCulture.png",
                "title_description": "Syringe Filled With Mycelium",
                "description": "Encapsulated mycelium in a proprietary suspension for effective use of injection ported bags.",
                "description2": "All Solutions are made using ISO9001 standards.",

            },
            {
                "name":"Parafilm",
                "alt_name":'Parafin thin film. 2" wide',
                "uom":"unit",
                "image_url": "/product_images/paraFilm.jpg",
                "description": "Includes all in one spore syringe, and sterilized media bag with injection port.",

            },
            {
                "name":"Seminar",
                "alt_name":'1hr live, personalized seminar on biology and practical home growing.',
                "uom":"unit",
                "image_url": "/product_images/seminar.png",
                "description": "Will contact to schedule time.",

            }
    ]
    return products