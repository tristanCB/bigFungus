
def getMycoNetBuilds(item: str = None) -> dict: 
    teks = {        
        "Agar Plates" : {
            "images":[
                    "teks/plate/autoclaving_agar.png",
                    "teks/plate/cooling_down_agar.png",
                    "teks/plate/pouring_plates.png"
                ],
            "desc": "This procedure will give you a step by step on how to make your own petri dishes to isolate your mycelium",
            "steps": [
                "Dice 200g of potatoes",
                "Prepare a pot with 1L of water and bring to a boil",
                "After 15 minutes, remove the potatoes with a slotted spoon and put the potato water aside",
                "Mix the 1L of potato water with 20g of AGAR and 20g of dextrose (substitute with table sugar)",
                "Mix thoroughly and pour the mixture into 3 small mason jars. Put lid on but DO NOT close lid tightly as to not risk breaking the jar.",
                "Set the agar filled mason jars in your autoclave and sterilize for 1 hour. It is useful to use the extra autoclave space to sterilize your scalpel and razor blade",
                "Prepare petri dishes by disinfecting them in a bleach solution for 20 minutes. The recipe for the bleach solution is as follows [1L water : 70mL bleach] this will give a 3000 ppm solution",
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
            "images":[
                    "teks/tissue/selecting_a_piece_of_mycelium.png",
                    "teks/tissue/after_isolation.png",
                    "teks/tissue/results.png"
                ],
            "desc": "This procedure will give you a step by step on how to isolate your chosen mycelium on an empty petri dish",
            "steps": [
                "Note: it is recommend to wear a mask and nitrile gloves for this procedure to minimize bacterial contamination",
                "Find a suitable mushroom sample, it can be from a trusted market, grocery store, or even foraged from the forest (Make sure you know what you're getting!!)",
                "Clean the mushroom sample gently with running water to remove debris and spray lightly with isopropyl alcohol",
                "Wait for the sample to dry a bit while you compose yourself, take this moment to visualize the mushroom growing",
                "Using the Razor blade, slice the top of the mushroom down the center going a few centimeters deep, then grab both side of the mushroom to split it even down the center",
                "The reason for doing it this way is to avoid smearing surface bacteria into the center of the mushroom where you will take your sample",
                "Without touching the center of the mushroom you just exposed, take your sterilized scalpel and take a small shallow sample from the middle of the mushroom",
                "This sample should be taken where the cap meets the stem of the mushroom, this is where the mycelium will be most active",
                "Put a small section of the sample into each petri dish. The more you make, the more chance you have of getting a petri with no contamination",
                "You will now wait 2-3 weeks for the samples to cover your agar plate",
                "Some will have bacterial or fungal contamination",
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
        "CCFP Tek" : {
            "content": [
                '<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bigfungus.ca/video/7116706167249767685" data-video-id="7116706167249767685" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@bigfungus.ca" href="https://www.tiktok.com/@bigfungus.ca">@bigfungus.ca</a> coffee filter tek for mushroom grain spawn. <a title="growyourown" target="_blank" href="https://www.tiktok.com/tag/growyourown">#growyourown</a> <a title="mushrooms" target="_blank" href="https://www.tiktok.com/tag/mushrooms">#mushrooms</a> <a title="mushroom" target="_blank" href="https://www.tiktok.com/tag/mushroom">#mushroom</a> <a target="_blank" title="♬ original sound - user5582984906762" href="https://www.tiktok.com/music/original-sound-7116706134538406662">♬ original sound - user5582984906762</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>'
            ],
            "desc": "Cheap Coffee Filter Port tek for jar grain spawn. Used as a replacement to micron filter ports.",
            "steps": [
                "List: 4 x coffee filter (preferably for 12 - 8 cups), 1 mason jar (wide) with lid assembly, 1 drill bit (rated for metal) and substrate.",
                "Drill hole into mason jar's lid using drill bit ~ 1/4 of an inch.", 
                "Fill jar with desired substrate",
                "Place holed metal lid on the filled jar",
                "Place 4 coffee filters on top then secure the lid with the metal ring",
                "fold coffee the excess filter material on top of the jar",
                "Cover with aluminum foil",
                "Autoclave then use immediately once cooled",
                "Note that the aluminum foil on the top should be left during colonization of the substrate to minimize chance of contamination"
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 2.99 $",
            "img_href": "teks/coffeeFilterTek.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Beginner"
        },
        "Seed Spawn" : {
            "images": [
            
                ],
            "desc": "This procedure will give you a step by step on how to prepare your grain spawn to ready it for your chosen mycelium",
            "steps": [
                "Place 1kg of dry rye grain into a large pot with 1L of tap water",
                "Bring to a boil and let simmer for 15-20 minutes while stirring constantly to avoid sticking, a rice cooker helps greatly with this step",
                "The grain is ready when all the water is evaporated and you are left with a dry but hydrated grain",
                "Once the grain is sufficiently cooked, remove from heat and let air dry to let excess steam escape. For use with a rice cooker, simply leave it on the warm setting",
                "Wait 10-15 minutes for the grain to cool and for the surface moisture to evaporate from the grain",
                "Collect and use the cooked grain to fill as many mushroom grow bags as you wish. recommended 4-5 bags",
                "Fold the tops of the bags down to prevent them from touching the sides of the autoclave while still allowing air transfer between the inside and outside of the bag (to prevent rupture)",
                "Autoclave the grain spawn for 1 hour at 121 degrees Celsius",
                "Once the sterilization cycle is finished, place grain spawn bags in front of your flow hood or still air box (don't forget to turn the flow hood on)",
                "Put on gloves and mask and disinfect the outside of your isolated mycelium dish and your scalpel (if it is not sterilized already)",
                "Before inoculating your grain, make sure it has cooled to room temperature as to not kill the mycelium",
                "Using the scalpel, gently cut the agar in the petri dish into small pieces and put 1 petri dish per grain bag",
                "While remaining in front of your flow hood, seal the bag using a heat or impulse sealer, or simply tie the top of the bag tightly with a few elastics",
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
            "images":[
                    "teks/bulkSpawn/loading_bulk_grain_spawn.png",
                    "teks/bulkSpawn/innoculating_bulk_grain.png",
                ],
            "desc": "This procedure will give you a step by step on how to transfer seed spawn to bulk spawn in preparation for block inoculation",
            "steps": [
                "Place 4kg of dry rye grain into a large pot with 4L of tap water (more can be done in one shot, make sure your ratio remains 1:1)",
                "Bring to a boil and let simmer for 15-20 minutes while stirring constantly to avoid sticking, a rice cooker helps greatly with this step",
                "The grain is ready when all the water is evaporated and you are left with a dry but hydrated grain",
                "Once the grain is sufficiently cooked, remove from heat and let air dry to let excess steam escape. For use with a rice cooker, simply leave it on the warm setting",
                "Wait 10-15 minutes for the grain to cool and for the surface moisture to evaporate from the grain",
                "Collect and use the cooked grain to fill 4 mushroom unicorn bags",
                "Fold the tops of the bags down to prevent them from touching the sides of the autoclave while still allowing air transfer between the inside and outside of the bag (to prevent rupture)",
                "Autoclave the grain spawn for 1 hour at 121 degrees Celsius",
                "Once the sterilization cycle is finished, place grain spawn bag in front of your flow hood (don't forget to turn the flow hood on)",
                "Get your seed grain spawn ready by wiping down the outside with 70 percent isopropyl alcohol",
                "Gently break up the seed grain spawn into smaller kernels",
                "While remaining in front of your flow hood or still air box, pour the 1/4 of the seed spawn bag into each bulk spawn bag",
                "While still remaining in front of your flow hood, seal the bag using a heat or impulse sealer, or simply tie the top of the bag tightly with a few elastics. Hermetic seal is recommended",
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
            "desc": "This procedure will give you a step by step on how to make your own mushroom block and inoculate it with grain spawn to grown your own mushrooms, flow hood and autoclave strongly recommended",
            "steps": [
                "Prepare the following items for 1 block (adjust for number of blocks): 1kg of master's mix, 0.57kg tap water, 1g of gypsum, 1 mushroom bag, bulk grain spawn of choice",
                "Put your 1kg of masters mix pellets in your mushroom bag.",
                "Mix the gypsum with your water to dissolve it",
                "In one fast shot, dump all the water into the mushroom bag at the same time and immediately mix thoroughly . This will allow all the pellets to hydrate evenly",
                "Keep mixing for 2-3 minutes while the pellets hydrate fully",
                "Fold the top of the bag over and autoclave at 121 degrees C for 1h. Autoclaving for longer than this will caramelize the substrate and will inhibit nutrient uptake",
                "Once the substrate bag is sterilized, remove it from the autoclave and set it in front of your flow hood next to your bulk grain spawn. Make sure to let it cool down fully before use",
                "Disinfect the outside of the grain spawn bag with 70 percent isopropyl alcohol and break the bulk grain spawn bag up gently and cut the top corner off to make a 3-5 inch opening",
                "Poor 1/5 of the 1kg grain spawn bag to inoculate 1 substrate bag, you can inoculate 5 substrate logs/bags with 1 bag of bulk spawn from this method",
                "Immediately seal the substrate bag while remaining in front of the flow hood to minimize possible contamination sources",
                "If the rest of the grain spawn bag isn't to be used right away, seal it as well to prevent contamination (it is recommended to just use the full bag of grain spawn and make 5 substrate logs)",
                "Once the bag is sealed, it can be labelled and shaken gently to mix the grain around with the substrate. Make sure to get it into the bottom corners of the bag, they tend to get neglected ",
                "Leave to newly inoculated substrate logs in a dark 20 degree C room. Wait 10-15 days while your blocks inoculate. Deviations in different mushrooms and temperature can increase time to 30-60 days",
            ],
            "website": "bigfungus",
            "item_type": "Trusted recipe",
            "price":"~ 45 $",
            "img_href": "teks/block.png",
            "shortDesc": "Big Fungus approved procedure",
            "level": "Advanced"
        },

        "Mushroom Block" : {
            "desc": "This procedure will give you a step by step on how to fruit the mushroom blocks you have bought or crafted, it is relatively straightforward but requires some practice to get right",
            "steps": [
                "Depending on the type of mushroom you are trying to fruit, this procedure will vary slightly",
                "Mushroom fruiting of Enokitake and King trumpet or King oyster mushrooms is much more difficult since they require colder temperatures around 15 degrees C to trigger the growth of the mushroom",
                "For easier fruiting, other types are more commonly used such as black oysters, Italian oysters, lions mane, etc.",
                "Your mushroom bag is ready to fruit when it becomes fully inoculated with mycelium",
                "Set your mushroom block out in a cool, dimly lit place. There must be enough light to be able to read but no more than that, without light, mushrooms won't form properly",
                "The block needs access to fresh air while remaining above 85 percent humidity, the easiest way to achieve this is by making a fruiting bin",
                "You can make your own fruiting bin easily by putting holes into a plastic bin and lining the bottom with vermiculite. The vermiculite will retain moisture and holes will allow air exchange",
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
            "desc": "PF tek is a common and simple method for beginers. It involves using a spore syringe to inoculate pasterized or sterilized substarte made from vermiculite and brown rice flour. If you are just starting or like to keep things simple, this tek is what you are looking for.",
            "steps": [
                "Mix 450ml of water with 450g of vermiculite in a bowl",
                "Coat Vermiculite evenly with 250g of brown rice flour",
                "Loosely fill mason jars to leave approximately 1cm of head space in each",
                "Wide 1cm rim clean of any water or debri using a paper towel",
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
                ,"To begin, wipe your gloves down with ISO. If you're using a still air box, do everything except the flame sterilization inside the still air box."
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