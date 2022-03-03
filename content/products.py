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

def getMycoNetBuilds() -> dict: 
    teks = {        
        "Agar Plates" : {
            "affiliateItems": [
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B08PVX9J9C/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B08PVX9J9C&linkCode=as2&tag=bigfungus-20&linkId=1ff1c4511937cc9742abba0555f9ce48"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B08PVX9J9C&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B07D5JRMM3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07D5JRMM3&linkCode=as2&tag=bigfungus-20&linkId=5dc192b1b1f37c20ab28237f3a5c0128"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07D5JRMM3&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B016Y8JSK4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B016Y8JSK4&linkCode=as2&tag=bigfungus-20&linkId=4e48827d678d05ff5ad3aa42dc78a2ef"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B016Y8JSK4&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B098KVXQ1N/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B098KVXQ1N&linkCode=as2&tag=bigfungus-20&linkId=437c61c9b105219a16a231018e16d5c1"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B098KVXQ1N&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B01JRXKKSM/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01JRXKKSM&linkCode=as2&tag=bigfungus-20&linkId=b47bc536729b4257e84da17ee9e99e85"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B01JRXKKSM&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B07JNPZZQ9/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07JNPZZQ9&linkCode=as2&tag=bigfungus-20&linkId=1ed2675e51acc60e8704b79c777a6789"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07JNPZZQ9&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B09PB4BVPF/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B09PB4BVPF&linkCode=as2&tag=bigfungus-20&linkId=fabfabeae295cd0a56ba16cd52a769b1"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B09PB4BVPF&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B07WLCSM14/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07WLCSM14&linkCode=as2&tag=bigfungus-20&linkId=5c49f972ded63e9e0bc4a20dbf0e35da"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07WLCSM14&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B01C65T4M6/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01C65T4M6&linkCode=as2&tag=bigfungus-20&linkId=9aa7a5830a09fa37491a1a59a473293e"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B01C65T4M6&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
                ,'<a href="https://www.amazon.com/Msfullsea-Vertical-Laminar-Workstation-Worktable/dp/B095WH7MB1?crid=3L85KXN3FVPBZ&keywords=laminar+flow+hood&qid=1646345769&sprefix=laminar+flowhood%2Caps%2C67&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVE5IU1Y2WkgzVFNCJmVuY3J5cHRlZElkPUEwNzIyNjM5MzNZTkFaOVpFSE5MVSZlbmNyeXB0ZWRBZElkPUEwNTk5NjMxMlNCWlZLVUtWVVZYSiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=f9254e0582ce9e73447fde7617cc5e8c&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B095WH7MB1&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B095WH7MB1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            ],
            "desc": "This procedure will give you a step by step on how to make your own petri dishes to isolate your mycelium",
            "steps": [
                "Dice 200g of potatoes",
                "Prepare a pot with 1L of water and bring to a boil",
                "After 15 mintues, remove the potatoes with a slotted spoon and put the potato water aside",
                "Mix the 1L of potato water with 20g of AGAR and 20g of DEXTROSE(substitute with table sugar)",
                "Mix thorougly and pour the mixture into 3 small MASON JARS. Put lid on but DO NOT close lid tightly as to not risk breaking the jar.",
                "Set the agar filled mason jars in your AUTOCLAVE and sterilize for 1 hour. It is useful to use the extra autoclave space to sterilize your SCALPEL and RAZOR BLADE",
                "Prepare PETRI DISHES by disinfecting them in a BLEACH solution for 20 minutes. The recipe for the bleach solution is as follows [1L WATER : 70mL BLEACH] this will give a 3000 ppm solution",
                "After 20 minutes, set your petri dishes down in front of your flow hood and let them dry",
                "While waiting for your petri dishes to dry, wait for the autoclave sterilizing cycle to finish and remove your agar jars and scalpel and put them in front of your flow hood as well",
                "While remaining in front of your flow hood, carefully pour a small amount of potato agar into the bottom of each dish: there should be enough agar for 25 petri dishes",
                "Assemble each dish with a matching top and let cool a bit longer to let the potato agar firm up in the dish, you are now ready to isolate your mycelium",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 30 $",
            "img_href": "teks/plates.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },
        "Tissue Culture" : {
            "affiliateItems": [
                '<a href="https://www.amazon.com/Hygenix-Disposable-Filter-Tested-Nelson/dp/B089TX3BPY?crid=54T4SHEIEOXK&keywords=medical+mask&qid=1646345934&sprefix=medical+mask%2Caps%2C99&sr=8-1-spons&psc=1&smid=A1W8CLML2J3Z1B&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRlA2Rks1TUhUUVFHJmVuY3J5cHRlZElkPUEwNTM4MjU1M0daTExXRU9YTUNKRiZlbmNyeXB0ZWRBZElkPUEwMTk4MDMzMlVPQ0QxTUhEU1REUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li2&tag=bigfungus-20&linkId=68806ebe150e9ac3ef648b4401347ee1&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B089TX3BPY&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B089TX3BPY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,'<a href="https://www.amazon.com/PRIDE-Synthetic-Nitrile-Vinyl-Gloves-Medium/dp/B08Y98BVDM?crid=3KU700AZ3ED3N&keywords=nitrile+gloves&qid=1646345963&sprefix=nitrile+glove%2Caps%2C107&sr=8-3&linkCode=li2&tag=bigfungus-20&linkId=a0c98e4806a9bb01bdafc7f9577baa26&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08Y98BVDM&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B08Y98BVDM" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,'<a href="https://www.amazon.com/Amazon-Brand-Isopropyl-Antiseptic-Technical/dp/B07NFSFBXQ?crid=33S8RSBQWT5EJ&keywords=isopropyl&qid=1646346021&sprefix=isopropyl%2Caps%2C116&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTkNUVjVRWjBLT0hUJmVuY3J5cHRlZElkPUEwNjgzNzkyM0Q5WElCTFlNR1kwSCZlbmNyeXB0ZWRBZElkPUEwMDkxNTM4MlkwVTBDTDdRWlNCTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li2&tag=bigfungus-20&linkId=badd8957acdd7f501d70be8f173b22a7&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07NFSFBXQ&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07NFSFBXQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,'<a href="https://www.amazon.com/Surgical-Sterile-Practicing-Sculpting-Repairing/dp/B07WTVF64Z?crid=177QOOOX6RD83&keywords=scalpel&qid=1646346094&sprefix=scalpel%2Caps%2C96&sr=8-4&linkCode=li2&tag=bigfungus-20&linkId=ee0406b05187bed480efb65c2d375c44&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07WTVF64Z&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07WTVF64Z" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                
            ],
            "desc": "This procedure will give you a step by step on how to isolate your chosen mycelium on an empty petri dish",
            "steps": [
                "Note: it is recommend to wear a MASK and NITRILE GLOVES for this procedure to minimise bacterial contamination",
                "Find a suitable mushroom sample, it can be from a trusted market, grocery store, or even foraged from the forest (Make sure you know what you're getting!!)",
                "Clean the mushroom sample gently with running water to remove debris and spray lightly with ISOPROPYL ALCOHOL",
                "Wait for the sample to dry a bit while you compose yourself, take this moment to visualize the mushroom growing",
                "Using the Razor blade, slice the top of the mushroom down the center going a few centimeters deep, then grab both side of the mushroom to split it even down the center",
                "The reason for doing it this way is to avoid smearing surface bacteria into the center of the mushroom where you will take your sample",
                "Without touching the center of the mushroom you just exposed, take your sterilized scalpel and take a small shallow sample from the middle of the mushroom",
                "This sample should be taken where the cap meets the stem of the mushroom, this is where the mycelium will be most active",
                "Put a small section of the sample into each petri dish. The more you make, the more chance you have of getting a petri with no contamination",
                "You will now wait 2-3 weeks for the samples to cover your agar plate",
                "Some will have bacterial or fungal contamination (See our GUIDE TO RECOGNIZING CONTAMINATION)",
                "The goal is to isolate the nicest parts of the mycelium you have grown to clean plates in order to get a nice strong and clean sample",
                "Make sure to clean the outside of original place carefully before opening and cutting clean samples of the mycelium",
                "If a petri dish is heavily contaminated with mold, discard it since mold spore can be invisible to the naked eye and make it harder to isolate clean samples",
                "Repeat this procedure until you have acquired a petri dish growing only the desired mycelium",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 30 $",
            "img_href": "teks/tissueCulture.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },
        "Grain Spawn" : {
            "affiliateItems": [
                '<a href="https://www.amazon.com/Great-River-Organic-Milling-25-Pounds/dp/B0049YM8XU?crid=2NI38C0XCUR9M&keywords=organic+rye+grain&qid=1646346187&sprefix=organic+rye+grai%2Caps%2C104&sr=8-2&linkCode=li2&tag=bigfungus-20&linkId=7a0d29a0d9f2c570e54662ba766d9e4a&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0049YM8XU&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B0049YM8XU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,'<a href="https://www.amazon.com/BLACK-DECKER-Cooker-6-cup-White/dp/B016Y8JSK4?crid=19EZ25O19KBWD&keywords=rice+cooker&qid=1646346243&sprefix=rice+cooker%2Caps%2C92&sr=8-11&linkCode=li2&tag=bigfungus-20&linkId=f23846a03c3312b87418b599d5d1e473&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B016Y8JSK4&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B016Y8JSK4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,'<a href="https://www.amazon.com/Bounty-Quick-Size-Towels-Family-Regular/dp/B07MHJFRBJ?crid=1AB8RS57E101U&keywords=paper+towel&qid=1646346284&sprefix=paper+towel%2Caps%2C113&sr=8-5&linkCode=li2&tag=bigfungus-20&linkId=9f2b0ff91dc3cca0d909a8ca263118f4&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07MHJFRBJ&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07MHJFRBJ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                ,
            ],
            "desc": "This procedure will give you a step by step on how to prepare your grain spawn to ready it for your chosen mycelium",
            "steps": [
                "Place 1kg of dry rye grain into a large pot with 4L of tap water",
                "Bring to a boil and let simmer for 15-20 minutes while stirring constantly to avoid sticking, a RICE COOKER helps greatly with this step",
                "The grain is ready when it is almost fully hydrated or when 2-5 percent of the grains have burst",
                "Once the grain is sufficiently cooked, strain the grain to eliminate as much water as possible and spread out over some paper towel to dry excess moisture",
                "Wait 10-15 minutes for the grain to cool and for the surface moisture to evaporate from the grain",
                "Collect and use the cooked grain to fill 1-2 mushroom UNICORN BAGS",
                "Fold the tops of the bags down to prevent them from touching the sides of the autoclave while still allowing air transfer between the inside and outside of the bag (to prevent rupture)",
                "Autoclave the grain spawn for 1 hour at 121 degrees Celsius",
                "Once the sterilization cycle is finished, place grain spawn bag in front of your flow hood (don't forget to turn the flow hood ON)",
                "Put on gloves and mask and disinfect the outside of your isolated mycelium dish and your scalpel (if it is not sterilized already)",
                "Before inoculating your grain, make sure it has cooled to room temperature as to not kill the mycelium",
                "Using the scalpel, gently cut the agar in the petri dish into small pieces and put half into each bag",
                "While remaining in front of your flow hood, seal the bag using a heat or IMPULSE SEALER, or simply tie the top of the bag tightly with a few elastics",
                "Gently stir the bag around and place in a 20-22 degree C environment for 4-6 weeks",
                "When the mycelium has taken over 1/3 to 1/2 of the bag, break it up and shake very gently to accelerate the full inoculation of the bag",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 15 $",
            "img_href": "teks/grainSpawn.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },
        "PF Tek" : {
            "affiliateItems": [
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B0000BYCFU/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0000BYCFU&linkCode=as2&tag=bigfungus-20&linkId=91b53cc5b92863592fe9fe366458efd6"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0000BYCFU&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07MZF9J2G/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07MZF9J2G&linkCode=as2&tag=bigfungus-20&linkId=60d2df268ab5871defea2d4f32c91a42"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07MZF9J2G&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',                
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07N7PSQM1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07N7PSQM1&linkCode=as2&tag=bigfungus-20&linkId=9ff5a81e190df74b37553b119a02206d"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07N7PSQM1&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B00PG8RT6O/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00PG8RT6O&linkCode=as2&tag=bigfungus-20&linkId=b9d2b97c0976c9e06029b1eeed404295"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B00PG8RT6O&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07J49CD76/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07J49CD76&linkCode=as2&tag=bigfungus-20&linkId=c5ac9d11b317e539cbe5bddc26c7634e"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07J49CD76&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B000W7NNKA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B000W7NNKA&linkCode=as2&tag=bigfungus-20&linkId=9019181d34abbbd61bf31f4364d5b151"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B000W7NNKA&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            ],
            "desc": "PF tek is a common and simple method for beginers. It involves using a spore syringe to inoculate pasterized or sterilized substarte made from vermiculite and brown rice flour. If you are just starting or like to keep things simple, this tek is what you are looking for.",
            "steps": [
                "Mix 450ml of water with 450g of vermiculite in a bowl",
                "Coat Vermiculite evenly with 250g of brown rice flour",
                "Loosely fill mason jars to leave approximately 1cm of head space in each",
                "Wide 1cm rim clean of any water or debrit using a paper towel",
                "Top mason jar off with dry vermiculite",
                "drill 4 small holes in lids of jars, and tape them over with the millipore tape, cover full mason jar with taped lid, rim and a sheet of aluminum foil",
                "Line bottom of pressure cooker or cauldron with mason jar rims in order to prop the mason jar off the bottom during sterilization or pasteurization",
                "Fill the bottom of the pressure cooker up with water (Follow the manufacturers instructions) and load the filled mason jar up",
                "Close pressure cooker, bring it up to pressure and allow for 1hour to pass",
                "Empty pressure cooker and let the jars cool down in a relatively clean place (Inside your stove while it is off)",
                "Procure liquid mycelium syringe or spore syringe from bigfungus.ca or other source"
            ],
            "website": "community",
            "item_type": "Tek (Technique)",
            "price":"~ 250 $",
            "img_href": "teks/pftek.png",
            "shortDesc": "Psilocybe fanaticus technique",
            "level": "Beginner"
        },
        
    }
    return teks

def getShippingOptionsStripe():
    ship = [
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 0,
                    'currency': 'cad',
                },
                'display_name': 'Free shipping',
                # Delivers between 5-7 business days
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 5,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 7,
                    },
                }
                }
            },
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 1500,
                    'currency': 'cad',
                },
                'display_name': 'Next day air',
                # Delivers in exactly 1 business day
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                }
                }
            },
        ]
    return ship

def getComment():
    comments = [
        {
            "comment":"This is my first time purchasing, overall very satisfying process from start to finish. Very professional",
        },
        {
            "comment":"This is my second time purchasing, overall very satisfying process from start to finish. Very professional",
        }
    ]
    return comments