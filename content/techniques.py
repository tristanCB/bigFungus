
def getMycoNetBuilds(item: str = None) -> dict: 
    teks = {        
        "Agar Plates" : {
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/POTATOES-YELLOW-FRESH-PRODUCE-LBS/dp/B00AU1YSSY?crid=3OTOXC7OIDU4&keywords=potato&qid=1646429698&sprefix=potatoe%2Caps%2C123&sr=8-53&linkCode=li3&tag=bigfungus-20&linkId=d96de8a80f635df98c35210445e73538&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00AU1YSSY&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00AU1YSSY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B07D5JRMM3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07D5JRMM3&linkCode=as2&tag=bigfungus-20&linkId=5dc192b1b1f37c20ab28237f3a5c0128"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07D5JRMM3&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B016Y8JSK4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B016Y8JSK4&linkCode=as2&tag=bigfungus-20&linkId=4e48827d678d05ff5ad3aa42dc78a2ef"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B016Y8JSK4&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B098KVXQ1N/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B098KVXQ1N&linkCode=as2&tag=bigfungus-20&linkId=437c61c9b105219a16a231018e16d5c1"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B098KVXQ1N&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B01JRXKKSM/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01JRXKKSM&linkCode=as2&tag=bigfungus-20&linkId=b47bc536729b4257e84da17ee9e99e85"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B01JRXKKSM&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B07JNPZZQ9/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07JNPZZQ9&linkCode=as2&tag=bigfungus-20&linkId=1ed2675e51acc60e8704b79c777a6789"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07JNPZZQ9&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a href="https://www.amazon.com/All-American-2-Quart-Pressure-Cooker/dp/B00004S88Z?crid=2OXNOO9G05J2W&keywords=pressure+cooker&qid=1646447933&sprefix=pressure+cooker%2Caps%2C127&sr=8-11&linkCode=li2&tag=bigfungus-20&linkId=441df82d42e90cd626dee2f27fb1c718&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00004S88Z&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B00004S88Z" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a target="_blank"  href="https://www.amazon.com/gp/product/B01C65T4M6/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01C65T4M6&linkCode=as2&tag=bigfungus-20&linkId=9aa7a5830a09fa37491a1a59a473293e"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B01C65T4M6&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            #     ,'<a href="https://www.amazon.com/Msfullsea-Vertical-Laminar-Workstation-Worktable/dp/B095WH7MB1?crid=3L85KXN3FVPBZ&keywords=laminar+flow+hood&qid=1646345769&sprefix=laminar+flowhood%2Caps%2C67&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVE5IU1Y2WkgzVFNCJmVuY3J5cHRlZElkPUEwNzIyNjM5MzNZTkFaOVpFSE5MVSZlbmNyeXB0ZWRBZElkPUEwNTk5NjMxMlNCWlZLVUtWVVZYSiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=f9254e0582ce9e73447fde7617cc5e8c&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B095WH7MB1&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B095WH7MB1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            # ],
            "desc": "This procedure will give you a step by step on how to make your own petri dishes to isolate your mycelium",
            "steps": [
                "Dice 200g of <a href='https://amzn.to/3HVnxv9'>potatoes</a>",
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
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/Hygenix-Disposable-Filter-Tested-Nelson/dp/B089TX3BPY?crid=54T4SHEIEOXK&keywords=medical+mask&qid=1646345934&sprefix=medical+mask%2Caps%2C99&sr=8-1-spons&psc=1&smid=A1W8CLML2J3Z1B&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRlA2Rks1TUhUUVFHJmVuY3J5cHRlZElkPUEwNTM4MjU1M0daTExXRU9YTUNKRiZlbmNyeXB0ZWRBZElkPUEwMTk4MDMzMlVPQ0QxTUhEU1REUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li2&tag=bigfungus-20&linkId=68806ebe150e9ac3ef648b4401347ee1&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B089TX3BPY&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B089TX3BPY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/PRIDE-Synthetic-Nitrile-Vinyl-Gloves-Medium/dp/B08Y98BVDM?crid=3KU700AZ3ED3N&keywords=nitrile+gloves&qid=1646345963&sprefix=nitrile+glove%2Caps%2C107&sr=8-3&linkCode=li2&tag=bigfungus-20&linkId=a0c98e4806a9bb01bdafc7f9577baa26&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08Y98BVDM&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B08Y98BVDM" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Amazon-Brand-Isopropyl-Antiseptic-Technical/dp/B07NFSFBXQ?crid=33S8RSBQWT5EJ&keywords=isopropyl&qid=1646346021&sprefix=isopropyl%2Caps%2C116&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTkNUVjVRWjBLT0hUJmVuY3J5cHRlZElkPUEwNjgzNzkyM0Q5WElCTFlNR1kwSCZlbmNyeXB0ZWRBZElkPUEwMDkxNTM4MlkwVTBDTDdRWlNCTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li2&tag=bigfungus-20&linkId=badd8957acdd7f501d70be8f173b22a7&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07NFSFBXQ&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07NFSFBXQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Surgical-Sterile-Practicing-Sculpting-Repairing/dp/B07WTVF64Z?crid=177QOOOX6RD83&keywords=scalpel&qid=1646346094&sprefix=scalpel%2Caps%2C96&sr=8-4&linkCode=li2&tag=bigfungus-20&linkId=ee0406b05187bed480efb65c2d375c44&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07WTVF64Z&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07WTVF64Z" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
                
            # ],
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
        "Seed Spawn" : {
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/Great-River-Organic-Milling-25-Pounds/dp/B0049YM8XU?crid=2NI38C0XCUR9M&keywords=organic+rye+grain&qid=1646346187&sprefix=organic+rye+grai%2Caps%2C104&sr=8-2&linkCode=li2&tag=bigfungus-20&linkId=7a0d29a0d9f2c570e54662ba766d9e4a&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0049YM8XU&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B0049YM8XU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/BLACK-DECKER-Cooker-6-cup-White/dp/B016Y8JSK4?crid=19EZ25O19KBWD&keywords=rice+cooker&qid=1646346243&sprefix=rice+cooker%2Caps%2C92&sr=8-11&linkCode=li2&tag=bigfungus-20&linkId=f23846a03c3312b87418b599d5d1e473&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B016Y8JSK4&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B016Y8JSK4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Bounty-Quick-Size-Towels-Family-Regular/dp/B07MHJFRBJ?crid=1AB8RS57E101U&keywords=paper+towel&qid=1646346284&sprefix=paper+towel%2Caps%2C113&sr=8-5&linkCode=li2&tag=bigfungus-20&linkId=9f2b0ff91dc3cca0d909a8ca263118f4&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07MHJFRBJ&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li2&o=1&a=B07MHJFRBJ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Impresa-Products-Mushroom-Breathable-Autoclavable/dp/B07Q8VZ8X6?crid=2M88GEE6Q5H2F&keywords=UNICORN+BAGS+mushroom+grow&qid=1646447706&sprefix=unicorn+bags+mushroom+grow%2Caps%2C83&sr=8-6&linkCode=li3&tag=bigfungus-20&linkId=eb8a7542451f3c9c945be5596920e2be&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07Q8VZ8X6&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07Q8VZ8X6" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Tuttnauer-1730-Valueklave/dp/B00187YP1O?crid=28GREMPPBY6OJ&keywords=autoclave&qid=1646447880&sprefix=autoclave%2Caps%2C175&sr=8-3&linkCode=li3&tag=bigfungus-20&linkId=f13eadb8a77c4fced653ab8c131f461f&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00187YP1O&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00187YP1O" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Laminar-Filter-HEPA-Filter-Mycology-Repair/dp/B09DKFFRM4?crid=3EIBNE85QA40Z&keywords=laminar+flow+hood&qid=1646448034&sprefix=laminar+flow+hood%2Caps%2C159&sr=8-17-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExU0c4VTVZQ1Q2U1FEJmVuY3J5cHRlZElkPUEwMjg4ODM5TUpDTDRKOUEyVFFSJmVuY3J5cHRlZEFkSWQ9QTAyMzM0MjMzSzlYRVNDTFJIQ1lYJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ%3D%3D&linkCode=li3&tag=bigfungus-20&linkId=dbc1b666a565f2febe4c20e28d970a25&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09DKFFRM4&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B09DKFFRM4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/MedPride-Powder-Free-Nitrile-Gloves-Medium/dp/B00GS8W3T4?crid=2VLW326RE5P7D&keywords=gloves&qid=1646448095&sprefix=gloves%2Caps%2C147&sr=8-8&linkCode=li3&tag=bigfungus-20&linkId=c97454d155f13f7783335fd55a62d772&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00GS8W3T4&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00GS8W3T4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Comix-Face-Masks-Individual-Wrapped-Package-50pcs/dp/B08DHVTB7F?crid=ENABEI9PRB9L&keywords=mask&qid=1646448125&sprefix=mask%2Caps%2C119&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOUczNERTMFJDRVlFJmVuY3J5cHRlZElkPUEwNzcyMTA1VUNOMEMyNk9MMzdWJmVuY3J5cHRlZEFkSWQ9QTAwOTc3NDM2WDlKV1QyNkNUQlcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&linkCode=li3&tag=bigfungus-20&linkId=eda37d187fbb7242159c38c666da0044&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08DHVTB7F&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B08DHVTB7F" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Amazon-Brand-Isopropyl-Antiseptic-Technical/dp/B07NFSFBXQ?crid=16U1JZ2FONPCI&keywords=isopropyl&qid=1646448174&sprefix=isopropyl%2Caps%2C113&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR0UxUExJQjM2RlRRJmVuY3J5cHRlZElkPUEwNTY4ODk4VVY4WVpVVzZER1VFJmVuY3J5cHRlZEFkSWQ9QTAwOTE1MzgyWTBVMENMN1FaU0JOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ%3D%3D&linkCode=li3&tag=bigfungus-20&linkId=817f3bcb87a8083520f58be4babdba47&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07NFSFBXQ&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07NFSFBXQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Glass-Spray-Bottle-Refillable-Aromatherapy/dp/B00MBWBF7M?crid=1D2AO606QEQP1&keywords=spray+bottle&qid=1646448252&sprefix=spray+bottle%2Caps%2C112&sr=8-35&linkCode=li3&tag=bigfungus-20&linkId=4f4414827528a30dab22f26e9571b30f&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00MBWBF7M&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00MBWBF7M" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Medpride-Disposable-Stainless-Steel-Individual-Dermaplaining/dp/B07M9WJ38R?crid=18AIJJQX5A4GL&keywords=scalpel&qid=1646448303&sprefix=scalpel%2Caps%2C175&sr=8-3&linkCode=li3&tag=bigfungus-20&linkId=83bfebac960704ac0da4462fcfc2702d&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07M9WJ38R&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07M9WJ38R" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Metronic-Impulse-Sealing-Machine-Replacement/dp/B0062BFHRW?crid=2QZFWXGKQWE7M&keywords=IMPULSE+SEALER&qid=1646448340&sprefix=impulse+sealer%2Caps%2C170&sr=8-4&linkCode=li3&tag=bigfungus-20&linkId=fce4d95f5ef7254440fd59753629ee7e&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0062BFHRW&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B0062BFHRW" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,
            # ],
            "desc": "This procedure will give you a step by step on how to prepare your grain spawn to ready it for your chosen mycelium",
            "steps": [
                "Place 1kg of dry rye grain into a large pot with 1L of tap water",
                "Bring to a boil and let simmer for 15-20 minutes while stirring constantly to avoid sticking, a RICE COOKER helps greatly with this step",
                "The grain is ready when all the water is evaporated and you are left with a dry but hydrated grain",
                "Once the grain is sufficiently cooked, remove from heat and let air dry to let excess steam escape. For use with a rice cooker, simply leave it on the warm setting",
                "Wait 10-15 minutes for the grain to cool and for the surface moisture to evaporate from the grain",
                "Collect and use the cooked grain to fill as many mushroom UNICORN BAGS as you wish. recommended 4-5 bags",
                "Fold the tops of the bags down to prevent them from touching the sides of the autoclave while still allowing air transfer between the inside and outside of the bag (to prevent rupture)",
                "Autoclave the grain spawn for 1 hour at 121 degrees Celsius",
                "Once the sterilization cycle is finished, place grain spawn bags in front of your flow hood or still air box(don't forget to turn the flow hood ON)",
                "Put on gloves and mask and disinfect the outside of your isolated mycelium dish and your scalpel (if it is not sterilized already)",
                "Before inoculating your grain, make sure it has cooled to room temperature as to not kill the mycelium",
                "Using the scalpel, gently cut the agar in the petri dish into small pieces and put 1 petri dish per grain bag",
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
        "Bulk Spawn" : {
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/Great-River-Organic-Milling-25-Pounds/dp/B0049YM8XU?crid=1XWUGKTJ0YESY&keywords=rye+grain&qid=1646448647&sprefix=rye+grain%2Caps%2C329&sr=8-1&linkCode=li3&tag=bigfungus-20&linkId=4fda813402b466dfbf4dc29592628885&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0049YM8XU&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B0049YM8XU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Bayou-Classic-1144-Stainless-Stockpot/dp/B000FTLY1K?crid=MYJ7BGN3H7RA&keywords=large+pot&qid=1646448699&sprefix=large+pot%2Caps%2C527&sr=8-7&linkCode=li3&tag=bigfungus-20&linkId=0030d450dcfdde9ac0268cc8757df8f4&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B000FTLY1K&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B000FTLY1K" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            # ],
            "desc": "This procedure will give you a step by step on how to transfer seed spawn to bulk spawn in preparation for block inoculation",
            "steps": [
                "Place 4kg of dry rye grain into a large pot with 4L of tap water (more can be done in one shot, make sure your ratio remains 1:1)",
                "Bring to a boil and let simmer for 15-20 minutes while stirring constantly to avoid sticking, a RICE COOKER helps greatly with this step",
                "The grain is ready when all the water is evaporated and you are left with a dry but hydrated grain",
                "Once the grain is sufficiently cooked, remove from heat and let air dry to let excess steam escape. For use with a rice cooker, simply leave it on the warm setting",
                "Wait 10-15 minutes for the grain to cool and for the surface moisture to evaporate from the grain",
                "Collect and use the cooked grain to fill 4 mushroom UNICORN BAGS",
                "Fold the tops of the bags down to prevent them from touching the sides of the autoclave while still allowing air transfer between the inside and outside of the bag (to prevent rupture)",
                "Autoclave the grain spawn for 1 hour at 121 degrees Celsius",
                "Once the sterilization cycle is finished, place grain spawn bag in front of your flow hood (don't forget to turn the flow hood ON)",
                "Get your SEED GRAIN SPAWN ready by wiping down the outside with 70 percent isopropyl alcohol",
                "Gently break up the seed grain spawn into smaller kernels",
                "While remaining in front of your flow hood or still air box, pour the 1/4 of the seed spawn bag into each bulk spawn bag",
                "While still remaining in front of your flow hood, seal the bag using a heat or IMPULSE SEALER, or simply tie the top of the bag tightly with a few elastics. Hermetic seal is recommended",
                "Gently stir the bag around and place in a 20-22 degree C environment for 4-6 weeks",
                "When the mycelium has taken over 1/3 to 1/2 of the bag, break it up and shake very gently and break up large clumps to accelerate the full inoculation of the bag",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 60 $",
            "img_href": "teks/grainToGrain.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },
        "Block" : {
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/KUBEI-Upgraded-Digital-Precision-Electronic/dp/B07YKCFJHQ?crid=2D0SNWQFLOL6M&keywords=5kg+scale&qid=1646448816&sprefix=5kg+scal%2Caps%2C115&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN0JGUjdKNkZUUDVHJmVuY3J5cHRlZElkPUEwNzc1NDkxMkQ5SkpRMUczQVNWVCZlbmNyeXB0ZWRBZElkPUEwNjU0MzYwMjZBWExCNjkyTTA1WCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=63f6b3714d9cf55af93ae29e7cfa3e3c&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07YKCFJHQ&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07YKCFJHQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Down-Earth-Organic-Calcium-Sulfate/dp/B07N2Y5NHM?crid=1W7YP5JB0Z8VY&keywords=gypsum&qid=1646448849&sprefix=gypsum%2Caps%2C144&sr=8-2&linkCode=li3&tag=bigfungus-20&linkId=7cba3dfdcda8d0a73d1a5fb30344e8ad&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07N2Y5NHM&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07N2Y5NHM" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Duda-Energy-FGcc5f-Carbonate-Limestone/dp/B00K43MRKO?crid=RW1GYCBJLV09&keywords=CaCO3&qid=1646448888&sprefix=caco3%2Caps%2C214&sr=8-7&linkCode=li3&tag=bigfungus-20&linkId=1ff6d277d8e82cae477eb13c16826993&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00K43MRKO&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00K43MRKO" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/MushroomMediaOnline-Mushroom-Pellets-Supplement-Pound/dp/B09C2KFLNF?crid=AYYLV7DAEAKG&keywords=mastermix+pellets+mushrooms&qid=1646448931&sprefix=mastermix+pellets+mushrooms%2Caps%2C72&sr=8-1&linkCode=li3&tag=bigfungus-20&linkId=e47f3faa8be97a4fe31f5081b5ae0724&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09C2KFLNF&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B09C2KFLNF" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/MushroomMediaOnline-Mushroom-Pellets-Supplement-Pound/dp/B09C2KFLNF?crid=AYYLV7DAEAKG&keywords=mastermix+pellets+mushrooms&qid=1646448955&sprefix=mastermix+pellets+mushrooms%2Caps%2C72&sr=8-2&linkCode=li3&tag=bigfungus-20&linkId=5b5971551c94fd10cf04d4bbec774328&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09C2KFLNF&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B09C2KFLNF" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Tuttnauer-1730-Valueklave/dp/B00187YP1O?crid=2D2JH03NZMHGT&keywords=Autoclave&qid=1646449884&sprefix=autoclave%2Caps%2C78&sr=8-3&linkCode=li3&tag=bigfungus-20&linkId=0bc0eb43f39f889023a79e7734befea1&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00187YP1O&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B00187YP1O" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Amazon-Brand-Isopropyl-Antiseptic-Technical/dp/B07NFSFBXQ?crid=3B9WL969O8022&keywords=isopropyl&qid=1646449936&sprefix=isopropyl%2Caps%2C116&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQzZCUkY2VDg0MFdXJmVuY3J5cHRlZElkPUEwNzkwMjI2TUdUOVVaUFBCT0tFJmVuY3J5cHRlZEFkSWQ9QTAwOTE1MzgyWTBVMENMN1FaU0JOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ%3D%3D&linkCode=li3&tag=bigfungus-20&linkId=f12e071284f712b4b77a36f21b35dc3d&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07NFSFBXQ&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07NFSFBXQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Mushroom-Grow-Bags-Autoclave-Breathable/dp/B096FPKNPT?crid=1VWM73O3FWZOR&keywords=mushroom+grow+bag&qid=1646449976&sprefix=mushroom+grow+bag%2Caps%2C102&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWkZSOEFDNERMMkI1JmVuY3J5cHRlZElkPUEwNjIwOTg1MzI3VkRRQkpKTFUyQSZlbmNyeXB0ZWRBZElkPUEwMDQ3NDg2M1RGWDM2MU5OSFo4NyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=d44ffe227f2a7dc2bed531b96e6a6921&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B096FPKNPT&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B096FPKNPT" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Laminar-Filter-HEPA-Filter-Mycology-Repair/dp/B09DKFFRM4?crid=3Z43UZCIFGY3&keywords=flow+hood&qid=1646450029&sprefix=flowhold%2Caps%2C100&sr=8-32-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEdUOUJaNVZaTk5GJmVuY3J5cHRlZElkPUEwMTM5MDc2MU5GVUxLWDBFV001USZlbmNyeXB0ZWRBZElkPUEwMjMzNDIzM0s5WEVTQ0xSSENZWCZ3aWRnZXROYW1lPXNwX2J0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=87bbd7f6e9acf2f07a1fa3cf025c1c73&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09DKFFRM4&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B09DKFFRM4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Metronic-Impulse-Sealing-Machine-Replacement/dp/B0062BFHRW?crid=1RY690O4703LO&keywords=impulse+sealer&qid=1646450067&sprefix=impulse+sealer%2Caps%2C83&sr=8-4&linkCode=li3&tag=bigfungus-20&linkId=747d263f59f83f7cc47c852d1a44655e&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0062BFHRW&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B0062BFHRW" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,
            # ],
            "desc": "This procedure will give you a step by step on how to make your own mushroom block and inoculate it with grain spawn to grown your own mushrooms, flow hood and autoclave strongly recommended",
            "steps": [
                "Prepare the following items for 1 block (adjust for number of blocks): 1kg of MASTERs MIX, 0.57kg tap water, 1g of gypsum, 1 mushroom bag, bulk grain spawn of choice",
                "Put your 1kg of masters mix pellets in your mushroom bag.",
                "Mix the gypsum and CaCO3 with your water to dissolve it",
                "In one fast shot, dump all the water into the mushroom bag at the same time and immediately mix thoroughly . This will allow all the pellets to hydrate evenly",
                "Keep mixing for 2-3 minutes while the pellets hydrate fully",
                "Fold the top of the bag over and autoclave at 121 degrees C for 1h. Autoclaveing for longer than this will caramelize the substrate and will inhibit nutrient uptake",
                "Once the substrate bag is sterilized, remove it from the autoclave and set it in front of your flow hood next to your bulk grain spawn. Make sure to let it cool down fully before use",
                "Disinfect the outside of the grain spawn bag with 70 percent isopropyl alcohol and break the bulk grain spawn bag up gently and cut the top corner off to make a 3-5 inch opening",
                "Poor 1/5 of the 1kg grain spawn bag to inoculate 1 substrate bag, you can inoculate 5 substrate logs/bags with 1 bag of bulk spawn from this method",
                "Immediately seal the substrate bag while remaining in front of the flow hood to minimise possible contamination sources",
                "If the rest of the grain spawn bag isn't to be used right away, seal it as well to prevent contamination (it is recommended to just use the full bag of grain spawn and make 5 substrate logs)",
                "Once the bag is sealed, it can be labelled and shaken gently to mix the grain around with the substrate. Make sure to get it into the bottom corners of the bag, they tend to get neglected ",
                "Leave to newly inoculated substrate logs in a dark 20 degree C room. Wait 10-15 days while your blocks inoculate. Deviations in different mushrooms and temperature can increase time to 30-60 days",
                "If mushroom inoculated substrate bag is taking too long to colonise, spot for possible contamination using our GUIDE TO RECOGNIZING CONTAMINATION",

            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 45 $",
            "img_href": "teks/block.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },

        "Mushroom Block" : {
            # "affiliateItems": [
            #     '<a href="https://www.amazon.com/1000sqft-Reinforced-Waterproof-Encapsulation-Crawlspace/dp/B07BC4QFGV?crid=3P9DTFOE1S2QG&keywords=vapor+barrier&qid=1646450395&sprefix=vapor+barie%2Caps%2C84&sr=8-5&linkCode=li3&tag=bigfungus-20&linkId=ad329942777fd6a4f55d033276ab2f35&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07BC4QFGV&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07BC4QFGV" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Humidity-Controller-Inkbird-Humidistat-Pre-wired/dp/B01J1E5LWM?crid=3FTDBNA18E64E&keywords=humidifier+mushroom+growing&qid=1646450220&sprefix=humidifier+mushroom+growing%2Caps%2C77&sr=8-1-spons&psc=1&smid=A197YPAPAP8V04&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRUowSlEzWFFPT1NGJmVuY3J5cHRlZElkPUEwMTI4MjIyMzgwNDZESzRJU1ZVWCZlbmNyeXB0ZWRBZElkPUEwMjg4NjM4MlZVMUlSMUJUTlZNRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=272e49435211a48fa8f59bc2bf02552f&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01J1E5LWM&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B01J1E5LWM" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/JIAWANSHUN-Industrial-Humidifier-500-2200sq-ft-Supermarket/dp/B089GXGMBR?crid=1J2AGJVJZCH5A&keywords=humidifier+mushroom&qid=1646450266&sprefix=humidifier+mushroom%2Caps%2C81&sr=8-11&linkCode=li3&tag=bigfungus-20&linkId=9ebdcdec301622db391d1ab6fe6e430b&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B089GXGMBR&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B089GXGMBR" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/AC-Infinity-CLOUDLINE-S6-Controller/dp/B07FPFVZTZ?crid=16HHWR9S59WBX&keywords=inline+fan&qid=1646450328&sprefix=inline+fan%2Caps%2C96&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSVUzUjRKR0ZaSVE4JmVuY3J5cHRlZElkPUEwODcxNzU3Mjk4UTI4V09LRFc1SiZlbmNyeXB0ZWRBZElkPUEwMTg5NjU5MkxPQU5XMUg4Qk02NyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU%3D&linkCode=li3&tag=bigfungus-20&linkId=6eab601628fc3cb0b3818eb0e2df7d53&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07FPFVZTZ&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B07FPFVZTZ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            #     ,'<a href="https://www.amazon.com/Purificateur-Couverture-allerg%C3%A8nes-%C3%89limination-silencieuse/dp/B081NWVMCH?__mk_fr_CA=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1URWV67VOUFWN&keywords=air%2Bpurifying&qid=1648060262&sprefix=airpurifier%2Caps%2C70&sr=8-1-spons&smid=A32M9WIF92ZF3R&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBNDhFQk5YNkMxQ0YmZW5jcnlwdGVkSWQ9QTEzT0VMWUw4OUhTUUYmZW5jcnlwdGVkQWRJZD1BMDcwMTEyNDFCTFAxRjM2VkhFOTcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1&linkCode=li3&tag=bigfungus-20&linkId=4aab28cca461f39e7883c6a68ecbe785&language=en_US&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B081NWVMCH&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=bigfungus-20&language=en_US" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=bigfungus-20&language=en_US&l=li3&o=1&a=B081NWVMCH" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
            # ],
            "desc": "This procedure will give you a step by step on how to fruit the mushroom blocks you have bought or crafted, it is relatively straightforward but requires some practice to get right",
            "steps": [
                "Depending on the type of mushroom you are trying to fruit, this procedure will vary slightly",
                "Mushroom fruiting of Enokitake and King trumpet or King oyster mushrooms is much more difficult since they require colder temperatures around 15 degrees C to trigger the growth of the mushroom",
                "For easier fruiting, other types are more commonly used such as black oysters, Italian oysters, lions mane, etc.",
                "Your mushroom bag is ready to fruit when it becomes fully inoculated with mycelium",
                "Set your mushroom block out in a cool, dimly lit place. There must be enough light to be able to read but no more than that, without light, mushrooms won't form properly",
                "The block needs access to fresh air while remaining above 85 percent humidity, the easiest way to achieve this is by making a FRUITING BIN",
                "You can make your own fruiting bin easily by putting holes into a plastic bin and lining the bottom with VERMICULITE. The vermiculite will retain moisture and holes will allow air exchange",
                "Clean your mushroom bag with Isopropyl alcohol (optional). Place your mushroom bag in your fruiting chamber, bin or bag and cut a few Xs into the bag 1 inch in size",
                "The mushroom block must never dry out, it must stay at at least 85 percent humidity throughout the growth of the mushroom. Using a cheap humidity sensor can be very helpful",
                "If done using a humidity tent or bag, lift the bag 2-5 times a day to allow fresh air in and mist the block gently with water while doing so",
                "If done correctly, the block will start to create pins around the cut areas. These pins are the beginning of the mushrooms fruiting body",
                "Allow enough space for the mushroom to fully develop, this can take anywhere from 10 days (oyster mushrooms) to 60 days (trametes versicolor)",
                "The fruits are ready to be harvested depending on their tell-tale sign. For oyster mushrooms, the cap switches from drooping downwards to fanning out upwards. Different types have different tells",
                "Blocks can be be harvested from multiple times before being used up. Once they are used up, the substrate should become lighter and pull back from the bag. This usually happens after the 2-3 flush",
                "Once the block is finished fruiting, discard the plastic mushroom bag and compost the leftover block",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 75 $",
            "img_href": "teks/mushroomBlock.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },
        # "Fungi Guide" : {
        #     "affiliateItems": [
               
        #     ],
        #     "desc": 
        #         '''
        #         Fungi are a varied collection of creatures that include single-celled organisms as well as multicellular filamentous species. Only a portion of the diversity that exists is currently understood, according to estimates. Several species were introduced into research in the twentieth century as the simplest eukaryotic model systems that could be examined using cell biology, genetics, and biochemistry methodologies. The genome sequences of a few fungus are currently known, and work on the genome sequences of numerous other species is in progress. Fungi will be increasingly utilised in the twenty-first century not just for understanding their particular manner of life, but also for discoveries that have broader implications for higher creatures, such as the assembly of complex structures. biological rhythms, ageing, and death, intracellular organelles, adaptation to adverse environmental conditions, defence mechanisms for protection from invasion by foreign DNA, and biological cycles Their capacity to be transformed and transgenic strains to be cultivated in relatively simple nutritional medium in industrial-sized fermentors, as well as their extracellular protein secretion, are likely to be used for the synthesis of a range of enzymes (proteins), including human vaccines.
        #         ''',
        #     "steps": [
        #         "FUNGI are non-photosynthetic eukaryotic creatures that grow as solitary cells (yeasts) or multicellular filaments (moulds/fungi), obtaining nutrition from their surroundings by absorption. There is no biological material that is completely free of fungi. The vast majority of fungi breakdown dead matter and recycle critical mineral resources (especially nitrogen, phosphate, and potassium) required to create the cytoplasm, despite their unfavourable reputation for spoiling stored food and infecting plants.",
        #     ],
        #     "website": "literature",
        #     "item_type": "Guide",
        #     "price":"10 mins",
        #     "img_href": "",
        #     "shortDesc": "Evolution and Diversity",
        #     "level": "Beginner"
        # },
        "PF Tek" : {
            # "affiliateItems": [
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B0000BYCFU/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0000BYCFU&linkCode=as2&tag=bigfungus-20&linkId=91b53cc5b92863592fe9fe366458efd6"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0000BYCFU&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B07MZF9J2G/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07MZF9J2G&linkCode=as2&tag=bigfungus-20&linkId=60d2df268ab5871defea2d4f32c91a42"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07MZF9J2G&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',                
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B07N7PSQM1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07N7PSQM1&linkCode=as2&tag=bigfungus-20&linkId=9ff5a81e190df74b37553b119a02206d"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07N7PSQM1&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B00PG8RT6O/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00PG8RT6O&linkCode=as2&tag=bigfungus-20&linkId=b9d2b97c0976c9e06029b1eeed404295"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B00PG8RT6O&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B07J49CD76/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07J49CD76&linkCode=as2&tag=bigfungus-20&linkId=c5ac9d11b317e539cbe5bddc26c7634e"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07J49CD76&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
            #     '<a target="_blank"  href="https://www.amazon.com/gp/product/B000W7NNKA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B000W7NNKA&linkCode=as2&tag=bigfungus-20&linkId=9019181d34abbbd61bf31f4364d5b151"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B000W7NNKA&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            # ],
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
        "Uncle Ben's Tek" : {
            "affiliateItems": [
            ],
            "desc": "Instant Rice Grain Spawn Popularized by the subreddit <a href='https://www.reddit.com/r/unclebens/comments/el1d8q/part_2_inoculating_uncle_bens_for_colonization/'>/r/unclebens/</a>",
            "steps": [
                "Put on a hat, a mask, and gloves. Wipe your surfaces  with Isopropyl alcohol solution (ISO) and spray Lysol in the air space you are using. Allow time for the Lysol to settle."
                ,"To begin, wipe your gloves down with ISO. If you're using a still air box, do everything except the flame sterilisation inside the still air box."
                ,"Clean the body of your syringe with. Place the needle in place and wipe with ISO. I like to keep my syringe soaked in ISO on a paper towel until I need it."
                ,"Wipe the outside of Uncle Ben's bag (ideally Brown rice) with ISO. Make sure you cover every inch of it, particularly the front, where you'll inoculate. Allow time for it to dry."
                ,"Using your hands, break apart the rice in the bag. You want the rice to be free-moving."
                ,"Allow your scissors to dry after wiping them down with ISO. Cut a 1 inch diagonal slice out of one of the bag's top corners. Keep the bag closed until you tape it shut to prevent unwanted microorganisms from entering."
                ,"Homogenize the content of your spore syringe closed by vibrating it. The black spores are likely clumped together, ensure it is shook every time you inoculate to disperse them into the solution."
                ,"Squirt ~0.75cc (0.75mL) of the shaken spore solution from the sterilized syringe into the cut corner of the bag, only as far as the needle reaches inside."
                ,"Take your syringe out of your pocket and place it aside. For the next bag, it will need to be cleaned off and flame sterilized once more."
                ,"To make a gas exchange vent, use your micropore tape to cover the open corner in a way that keeps the corner-hole open."
                ,
            ],
            "website": "reddit",
            "item_type": "Tek (Technique)",
            "price":"~ 45 $",
            "img_href": "teks/UBtek.png",
            "shortDesc": "Instant Rice Grain Spawn",
            "level": "Beginner"
        },
    }
    if item == None:
        return teks
    else:
        print(teks[item])
        return {item : teks[item]}