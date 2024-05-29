# Define the hardcoded categories
CATEGORIES = [
    {'name': 'Vehicles', 'slug': 'vehicles', 'children': [
        {'name': 'Cars', 'slug': 'cars', 'children': [
            {'name': 'Hatchbacks', 'slug': 'hatchbacks'},
            {'name': 'Sedans', 'slug': 'sedans'},
            {'name': 'Coupes', 'slug': 'coupes'},
            {'name': 'Convertibles', 'slug': 'convertibles'},
            {'name': 'SUVs', 'slug': 'suvs'},
            {'name': 'Crossovers', 'slug': 'crossovers'},
            {'name': 'Minivans', 'slug': 'minivans'}
        ]},
        {'name': 'Bikes', 'slug': 'bikes', 'children': [
            {'name': 'Motorcycles', 'slug': 'motorcycles'},
            {'name': 'Scooters', 'slug': 'scooters'},
            {'name': 'ATVs', 'slug': 'atvs'},
            {'name': 'Sport Bikes', 'slug': 'sport-bikes'},
            {'name': 'Cruiser Bikes', 'slug': 'cruiser-bikes'},
            {'name': 'Touring Bikes', 'slug': 'touring-bikes'},
            {'name': 'Electric Bikes', 'slug': 'electric-bikes'}

        ]}

    ]},
    {'name': 'Property', 'slug': 'property', 'children': [
        {'name': 'Houses', 'slug': 'houses', 'children': [
            {'name': 'Residential', 'slug': 'residential'},
            {'name': 'Commercial', 'slug': 'commercial'}

        ]},
        {'name': 'Land', 'slug': 'land', 'children': [
            {'name': 'Residential', 'slug': 'residential'},
            {'name': 'Commercial', 'slug': 'commercial'}

        ]},
        {'name': 'Flats', 'slug': 'flats', 'children': [
            {'name': 'Residential', 'slug': 'residential'},
            {'name': 'Commercial', 'slug': 'commercial'}
            
        ]}

    ]},
    {'name': 'Phones', 'slug': 'phones', 'children': [
        {'name': 'Smartphones', 'slug': 'smartphones', 'children': [
            {'name': 'Samsung', 'slug': 'samsung', 'children': [
                {'name': 'Samsung Galaxy A50s', 'slug': 'samsung-galaxy-a50s'},
                {'name': 'Samsung Galaxy M30', 'slug': 'samsung-galaxy-m30'}

            ]},
            {'name': 'Apple', 'slug': 'apple', 'children': [
                {'name': 'Apple iPhone 11', 'slug': 'apple-iphone-11'},
                {'name': 'Apple iPhone 11 Pro', 'slug': 'apple-iphone-11-pro'}

            ]},
            {'name': 'Xiaomi', 'slug': 'xiaomi', 'children': [
                {'name': 'Xiaomi Redmi Note 8', 'slug': 'xiaomi-redmi-note-8'},
                {'name': 'Xiaomi Mi 9T', 'slug': 'xiaomi-mi-9t'}

            ]}

        ]},
        {'name': 'Featured Phones', 'slug': 'featured-phones', 'children': [
            {'name': 'Samsung Galaxy A50s', 'slug': 'samsung-galaxy-a50s', 'children': [
                {'name': 'Samsung Galaxy A50s', 'slug': 'samsung-galaxy-a50s'},
                {'name': 'Samsung Galaxy M30', 'slug': 'samsung-galaxy-m30'}

            ]},
            {'name': 'Apple iPhone 11', 'slug': 'apple-iphone-11', 'children': [
                {'name': 'Apple iPhone 11', 'slug': 'apple-iphone-11'},
                {'name': 'Apple iPhone 11 Pro', 'slug': 'apple-iphone-11-pro'}

            ]},
            {'name': 'Xiaomi Mi 10T', 'slug': 'xiaomi-mi-10t', 'children': [
                {'name': 'Xiaomi Mi 10T', 'slug': 'xiaomi-mi-10t'},
                {'name': 'Xiaomi Mi 9T', 'slug': 'xiaomi-mi-9t'}
                
            ]}
        ]}
    ]},
    {
        'name': 'Electronics', 'slug': 'electronics', 'children': [
            {'name': 'Laptops', 'slug': 'laptops', 'children': [
                {'name': 'HP', 'slug': 'hp', 'children': [
                    {'name': 'HP 15s', 'slug': 'hp-15s'},
                    
                ]},
                {'name': 'Asus', 'slug': 'asus', 'children': [
                    {'name': 'Asus VivoBook', 'slug': 'asus-vivobook'}

                ]},
                {'name': 'Acer', 'slug': 'acer', 'children': [
                    {'name': 'Acer Swift 3', 'slug': 'acer-swift-3'}
                ]},
                {'name': 'Apple', 'slug': 'apple', 'children': [
                    {'name': 'Apple MacBook Pro', 'slug': 'apple-macbook-pro'}
                ]},
            ]},
            {'name': 'Audio Equipment', 'slug': 'audio-equipment', 'children': [
                {'name': 'Headphones', 'slug': 'headphones', 'children': [
                    {'name': 'Sony WH-1000XM3', 'slug': 'sony-wh-1000xm3'},
                    {'name': 'Sennheiser HD 598', 'slug': 'sennheiser-hd-598'},
                    {'name': 'Bose QuietComfort 35 II', 'slug': 'bose-quietcomfort-35-ii'},
                    {'name': 'JBL Tune 500NC', 'slug': 'jbl-tune-500nc'}
            ]},
                {'name': 'Speakers', 'slug': 'speakers', 'children': [
                    {'name': 'JBL Flip 5', 'slug': 'jbl-flip-5'},
                    {'name': 'Bose SoundLink Revolve+', 'slug': 'bose-soundlink-revolve+'},
                    {'name': 'Sony MDR-1000XM3', 'slug': 'sony-mdr-1000xm3'},
                    {'name': 'Sony MDR-750X', 'slug': 'sony-mdr-750x'}
                ]},
                {'name': 'Microphones', 'slug': 'microphones', 'children': [
                    {'name': 'Shure SM58', 'slug': 'shure-sm58'},
                    {'name': 'Rode NTG-1', 'slug': 'rode-ntg-1'},
                    {'name': 'Shure SM7B', 'slug': 'shure-sm7b'},
                    {'name': 'Rode NTG-3', 'slug': 'rode-ntg-3'}
                ]},
                {'name': 'Accessories', 'slug': 'accessories', 'children': [
                    {'name': 'Rode Pg2', 'slug': 'rode-pg2'},
                    {'name': 'Rode Pg3', 'slug': 'rode-pg3'},
                    {'name': 'Rode Pg5', 'slug': 'rode-pg5'},
                    {'name': 'Rode Pg8', 'slug': 'rode-pg8'}
                ]}
            ]},
        ]
    },
    {'name': 'Home', 'slug': 'home', 'children': [
        {'name': 'Furniture', 'slug': 'furniture', 'children': [
            {'name': 'Sofas', 'slug': 'sofas', 'children': [
                {'name': 'Leather Sofa', 'slug': 'leather-sofa'},
                {'name': 'Fabric Sofa', 'slug': 'fabric-sofa'},
                {'name': 'Corner Sofa', 'slug': 'corner-sofa'}
            ]},
            {'name': 'Tables', 'slug': 'tables', 'children': [
                {'name': 'End Tables', 'slug': 'end-tables', 'children': [
                    {'name': 'Coffee Table', 'slug': 'coffee-table'},
                    {'name': 'Side Table', 'slug': 'side-table'}
                ]},
                {'name': 'Dining Tables', 'slug': 'dining-tables', 'children': [
                    {'name': 'Dinner Table', 'slug': 'dinner-table'},
                    {'name': 'Dining Set', 'slug': 'dining-set'}
                ]},
            ]},
            {'name': 'Chairs', 'slug': 'chairs', 'children': [
                {'name': 'Leather Chairs', 'slug': 'leather-chairs'},
                {'name': 'Fabric Chairs', 'slug': 'fabric-chairs'},
                {'name': 'Corner Chairs', 'slug': 'corner-chairs'}
            ]}
        ]},
        {'name': 'Decor', 'slug': 'decor', 'children': [
            {'name': 'Paintings', 'slug': 'paintings', 'children': [
                {'name': 'Abstract Paintings', 'slug': 'abstract-paintings'},
                {'name': 'Landscape Paintings', 'slug': 'landscape-paintings'},
                {'name': 'Portrait Paintings', 'slug': 'portrait-paintings'}

            ]},
        ]}

    ]},
    {'name': 'Beauty', 'slug': 'beauty', 'children': [
        {'name': 'Skincare', 'slug': 'skincare', 'children': [
            {'name': 'Face Care', 'slug': 'face-care', 'children': [
                {'name': 'Cleansers', 'slug': 'cleansers'},
                {'name': 'Moisturizers', 'slug': 'moisturizers'},
                {'name': 'Serums', 'slug': 'serums'}

            ]},
        ]},
        {'name': 'Makeup', 'slug': 'makeup', 'children': [
            {'name': 'Lipstick', 'slug': 'lipstick', 'children': []},
            {'name': 'Foundation', 'slug': 'foundation', 'children': []},
            {'name': 'Mascara', 'slug': 'mascara', 'children': []},
            {'name': 'Eyeliner', 'slug': 'eyeliner', 'children': []},
            {'name': 'Eyeshadow', 'slug': 'eyeshadow', 'children': []},
            {'name': 'Brushes', 'slug': 'brushes', 'children': []},
            {'name': 'Palettes', 'slug': 'palettes', 'children': []},
            {'name': 'Lip Gloss', 'slug': 'lip-gloss', 'children': []},

        ]},
        {'name': 'Haircare', 'slug': 'haircare', 'children': [
            {'name': 'Shampoo', 'slug': 'shampoo', 'children': []},
            {'name': 'Conditioner', 'slug': 'conditioner', 'children': []},
            {'name': 'Hair Oil', 'slug': 'hair-oil', 'children': []},
            {'name': 'Hair Serum', 'slug': 'hair-serum', 'children': []},
            {'name': 'Hair Spray', 'slug': 'hair-spray', 'children': []},
            
        ]},

    ]},
    {'name': 'Fashion', 'slug': 'fashion', 'children': [
        {'name': 'Women', 'slug': 'women', 'children': [
            {'name': 'Dresses', 'slug': 'dresses', 'children': [
                {'name': 'Maxi Dresses', 'slug': 'maxi-dresses'},
                {'name': 'Mini Dresses', 'slug': 'mini-dresses'},
                {'name': 'Midi Dresses', 'slug': 'midi-dresses'},

            ]},
            {'name': 'Tops', 'slug': 'tops', 'children': [
                {'name': 'T-Shirts', 'slug': 't-shirts'},
                {'name': 'Blouses', 'slug': 'blouses'},
                {'name': 'Shirts', 'slug': 'shirts'},
                {'name': 'Sweaters', 'slug': 'sweaters'},
                {'name': 'Cardigans', 'slug': 'cardigans'},
                {'name': 'Hoodies', 'slug': 'hoodies'},
                {'name': 'Jumpers', 'slug': 'jumpers'},

            ]},
            {'name': 'Pants', 'slug': 'pants', 'children': [
                {'name': 'Jeans', 'slug': 'jeans'},
                {'name': 'Trousers', 'slug': 'trousers'},
                {'name': 'Shorts', 'slug': 'shorts'},
                {'name': 'Skirts', 'slug': 'skirts'},

            ]},
            {'name': 'Shoes', 'slug': 'shoes', 'children': [
                {'name': 'Heels', 'slug': 'heels'},
                {'name': 'Sandals', 'slug': 'sandals'},
                {'name': 'Flats', 'slug': 'flats'},
                {'name': 'Boots', 'slug': 'boots'},
                {'name': 'Sneakers', 'slug': 'sneakers'},

            ]},
        ]},
        {'name': 'Men', 'slug': 'men', 'children': [
            {'name': 'Shirts', 'slug': 'shirts', 'children': [
                {'name': 'T-Shirts', 'slug': 't-shirts'},
                {'name': 'Shirts', 'slug': 'shirts'},
                {'name': 'Polos', 'slug': 'polos'},
                {'name': 'Sweaters', 'slug': 'sweaters'},
                {'name': 'Hoodies', 'slug': 'hoodies'},
                {'name': 'Jumpers', 'slug': 'jumpers'},

            ]},
            {'name': 'Pants', 'slug': 'pants', 'children': [
                {'name': 'Jeans', 'slug': 'jeans'},
                {'name': 'Trousers', 'slug': 'trousers'},
                {'name': 'Shorts', 'slug': 'shorts'},
                {'name': 'Joggers', 'slug': 'joggers'},

            ]},
            {'name': 'Shoes', 'slug': 'shoes', 'children': [
                {'name': 'Sneakers', 'slug': 'sneakers'},
                {'name': 'Boots', 'slug': 'boots'},
                {'name': 'Sandals', 'slug': 'sandals'},
                {'name': 'Flats', 'slug': 'flats'},

            ]},
        ]},
        {'name': 'Kids', 'slug': 'kids', 'children': [
            {'name': 'Girls', 'slug': 'girls', 'children': [
                {'name': 'Dresses', 'slug': 'dresses', 'children': [
                    {'name': 'Maxi Dresses', 'slug': 'maxi-dresses'},
                    {'name': 'Mini Dresses', 'slug': 'mini-dresses'},

                ]},
                {'name': 'Tops', 'slug': 'tops', 'children': [
                    {'name': 'T-Shirts', 'slug': 't-shirts'},
                    {'name': 'Blouses', 'slug': 'blouses'},
                    {'name': 'Shirts', 'slug': 'shirts'},
                    {'name': 'Sweaters', 'slug': 'sweaters'},
                    {'name': 'Cardigans', 'slug': 'cardigans'},

                ]},
                {'name': 'Pants', 'slug': 'pants', 'children': [
                    {'name': 'Jeans', 'slug': 'jeans'},
                    {'name': 'Trousers', 'slug': 'trousers'},
                    {'name': 'Shorts', 'slug': 'shorts'},
                    {'name': 'Skirts', 'slug': 'skirts'},

                ]},
                {'name': 'Shoes', 'slug': 'shoes', 'children': [
                    {'name': 'Heels', 'slug': 'heels'},
                    {'name': 'Sandals', 'slug': 'sandals'},
                    {'name': 'Flats', 'slug': 'flats'},
                    {'name': 'Boots', 'slug': 'boots'},

                ]},
            ]},
            {'name': 'Boys', 'slug': 'boys', 'children': [
                {'name': 'Tops', 'slug': 'tops', 'children': [
                    {'name': 'T-Shirts', 'slug': 't-shirts'},
                    {'name': 'Shirts', 'slug': 'shirts'},
                    {'name': 'Polo Shirts', 'slug': 'polo-shirts'},
                    {'name': 'Sweatshirts', 'slug': 'sweatshirts'},

                ]},
                {'name': 'Pants', 'slug': 'pants', 'children': [
                    {'name': 'Jeans', 'slug': 'jeans'},
                    {'name': 'Trousers', 'slug': 'trousers'},
                    {'name': 'Shorts', 'slug': 'shorts'},
                    {'name': 'Joggers', 'slug': 'joggers'},

                ]},
                {'name': 'Shoes', 'slug': 'shoes', 'children': [
                    {'name': 'Sneakers', 'slug': 'sneakers'},
                    {'name': 'Boots', 'slug': 'boots'},
                    {'name': 'Sandals', 'slug': 'sandals'},
                    {'name': 'Flats', 'slug': 'flats'},

                ]},

            ]},
        ]},
    ]},
    {'name': 'Sport', 'slug': 'sport', 'children': [
        {'name': 'Outdoor', 'slug': 'outdoor', 'children': [
            {'name': 'Camping', 'slug': 'camping', 'children': [
                {'name': 'Tents', 'slug': 'tents'},
                {'name': 'Sleeping Bags', 'slug': 'sleeping-bags'},
                {'name': 'Sleeping Pad', 'slug': 'sleeping-pad'},
                {'name': 'Sleeping Bag Insulation', 'slug': 'sleeping-bag-insulation'},
                {'name': 'Sleeping Bag Accessories', 'slug': 'sleeping-bag-accessories'},
                {'name': 'Sleeping Bag Sets', 'slug': 'sleeping-bag-sets'},

            ]},
            {'name': 'Hiking', 'slug': 'hiking', 'children': [
                {'name': 'Hiking Boots', 'slug': 'hiking-boots'},
                {'name': 'Hiking Shoes', 'slug': 'hiking-shoes'},
                {'name': 'Hiking Shoes Accessories', 'slug': 'hiking-shoes-accessories'},
                {'name': 'Hiking Shoe Sets', 'slug': 'hiking-shoe-sets'},
                {'name': 'Hiking Backpacks', 'slug': 'hiking-backpacks'},
                {'name': 'Hiking Backpack Accessories', 'slug': 'hiking-backpack-accessories'},

            ]},
            {'name': 'Running', 'slug': 'running', 'children': [
                {'name': 'Running Shoes', 'slug': 'running-shoes'},
                {'name': 'Running Shoes Accessories', 'slug': 'running-shoes-accessories'},
                {'name': 'Running Shoe Sets', 'slug': 'running-shoe-sets'},
                {'name': 'Running Backpacks', 'slug': 'running-backpacks'},
                {'name': 'Running Backpack Accessories', 'slug': 'running-backpack-accessories'},

            ]},
            {'name': 'Swimming', 'slug': 'swimming', 'children': [
                {'name': 'Swimming Goggles', 'slug': 'swimming-goggles'},
                {'name': 'Swimming Cap', 'slug': 'swimming-cap'},
                {'name': 'Swimming Towel', 'slug': 'swimming-towel'},
                {'name': 'Swimming Suit', 'slug': 'swimming-suit'},
                {'name': 'Swimming Suit Accessories', 'slug': 'swimming-suit-accessories'},
                {'name': 'Swimming Suit Sets', 'slug': 'swimming-suit-sets'},

            ]},
            {'name': 'Fitness', 'slug': 'fitness', 'children': [
                {'name': 'Fitness Equipment', 'slug': 'fitness-equipment'},
                {'name': 'Fitness Clothes', 'slug': 'fitness-clothes'},
                {'name': 'Fitness Accessories', 'slug': 'fitness-accessories'},
                
            ]},
            {'name': 'Soccer', 'slug': 'soccer', 'children': [
                {'name': 'Soccer Balls', 'slug': 'soccer-balls'},
                {'name': 'Soccer Cleats', 'slug': 'soccer-cleats'},
                {'name': 'Soccer Gloves', 'slug': 'soccer-gloves'},


            ]},
            {'name': 'Basketball', 'slug': 'basketball', 'children': [
                {'name': 'Basketball Balls', 'slug': 'basketball-balls'},
                {'name': 'Basketball Shoes', 'slug': 'basketball-shoes'},
                {'name': 'Basketball Gloves', 'slug': 'basketball-gloves'},

            ]},
            {'name': 'Tennis', 'slug': 'tennis', 'children': [
                {'name': 'Tennis Balls', 'slug': 'tennis-balls'},
                {'name': 'Tennis Racket', 'slug': 'tennis-racket'},
                {'name': 'Tennis Shoes', 'slug': 'tennis-shoes'},

            ]},
            {'name': 'Badminton', 'slug': 'badminton', 'children': [
                {'name': 'Badminton Racket', 'slug': 'badminton-racket'},
                {'name': 'Badminton Shoes', 'slug': 'badminton-shoes'},
                {'name': 'Badminton Net', 'slug': 'badminton-net'},

            ]},
            {'name': 'Volleyball', 'slug': 'volleyball', 'children': [
                {'name': 'Volleyball Balls', 'slug': 'volleyball-balls'},

            ]},
            {'name': 'Golf', 'slug': 'golf', 'children': [
                {'name': 'Golf Balls', 'slug': 'golf-balls'},
                {'name': 'Golf Clubs', 'slug': 'golf-club'},
                {'name': 'Golf Gloves', 'slug': 'golf-gloves'},

            ]},
            {'name': 'Cycling', 'slug': 'cycling', 'children': [
                {'name': 'Cycling Bicycles', 'slug': 'cycling-bicycles'},
                {'name': 'Cycling Clothes', 'slug': 'cycling-clothes'},
                {'name': 'Cycling Accessories', 'slug': 'cycling-accessories'},

            ]},
            {'name': 'Skating', 'slug': 'skating', 'children': [
                {'name': 'Skating Shoes', 'slug': 'skating-shoes'},
                {'name': 'Skating Helmets', 'slug': 'skating-helmets'},
                {'name': 'Skating Protective Gear', 'slug': 'skating-protective-gear'},

            ]},
            {'name': 'Martial Arts', 'slug': 'martial-arts', 'children': [
                {'name': 'Karate', 'slug': 'karate', 'children': []},
                {'name': 'Jiu-Jitsu', 'slug': 'jiu-jitsu', 'children': []},
                {'name': 'Tae Kwon Do', 'slug': 'tae-kwon-do', 'children': []},

            ]},
            {'name': 'Boxing', 'slug': 'boxing', 'children': [
                {'name': 'Boxing Gloves', 'slug': 'boxing-gloves'},
                {'name': 'Boxing Bags', 'slug': 'boxing-bags'},
                {'name': 'Boxing Shoes', 'slug': 'boxing-shoes'},

            ]},
            {'name': 'Fencing', 'slug': 'fencing', 'children': [
                {'name': 'Fencing Swords', 'slug': 'fencing-swords'},
                {'name': 'Fencing Shields', 'slug': 'fencing-shields'},
                {'name': 'Fencing Bags', 'slug': 'fencing-bags'},

            ]},
            {'name': 'Wrestling', 'slug': 'wrestling', 'children': [
                {'name': 'Wrestling Gloves', 'slug': 'wrestling-gloves'},
                {'name': 'Wrestling Bags', 'slug': 'wrestling-bags'},
                {'name': 'Wrestling Shoes', 'slug': 'wrestling-shoes'},

            ]},
            {'name': 'Yoga', 'slug': 'yoga', 'children': [
                {'name': 'Yoga Mat', 'slug': 'yoga-mat'},
                {'name': 'Yoga Clothes', 'slug': 'yoga-clothes'},
                {'name': 'Yoga Accessories', 'slug': 'yoga-accessories'},

            ]},
            {'name': 'Pilates', 'slug': 'pilates', 'children': [
                {'name': 'Pilates Mat', 'slug': 'pilates-mat'},
                {'name': 'Pilates Clothes', 'slug': 'pilates-clothes'},
                {'name': 'Pilates Accessories', 'slug': 'pilates-accessories'},

            ]},
            {'name': 'Zumba', 'slug': 'zumba', 'children': [
                {'name': 'Zumba Mat', 'slug': 'zumba-mat'},
                {'name': 'Zumba Clothes', 'slug': 'zumba-clothes'},
                {'name': 'Zumba Accessories', 'slug': 'zumba-accessories'},
            ]},
            {'name': 'Dancing', 'slug': 'dancing', 'children': [
                {'name': 'Dancing Shoes', 'slug': 'dancing-shoes'},
                {'name': 'Dancing Clothes', 'slug': 'dancing-clothes'},
                {'name': 'Dancing Accessories', 'slug': 'dancing-accessories'},

            ]},
            {'name': 'Gymnastics', 'slug': 'gymnastics', 'children': [
                {'name': 'Gymnastics Balls', 'slug': 'gymnastics-balls'},
                {'name': 'Gymnastics Bars', 'slug': 'gymnastics-bars'},
                {'name': 'Gymnastics Rings', 'slug': 'gymnastics-rings'},

            ]},
            {'name': 'Water Sports', 'slug': 'water-sports', 'children': [
                {'name': 'Kayaking', 'slug': 'kayaking', 'children': []},
                {'name': 'Canoeing', 'slug': 'canoeing', 'children': []},
                {'name': 'Windsurfing', 'slug': 'windsurfing', 'children': []},
                {'name': 'Sailing', 'slug': 'sailing', 'children': []},

            ]},
        ]},
        {'name': 'Indoor', 'slug': 'indoor', 'children': [
            {'name': 'Arts and Crafts', 'slug': 'arts-and-crafts', 'children': []},
            {'name': 'Board Games', 'slug': 'board-games', 'children': []},
            {'name': 'Card Games', 'slug': 'card-games', 'children': []},
            {'name': 'Chess', 'slug': 'chess', 'children': []},
            {'name': 'Cooking', 'slug': 'cooking', 'children': []},
            {'name': 'Dancing', 'slug': 'dancing', 'children': []},
            {'name': 'Fitness', 'slug': 'fitness', 'children': [
                {'name': 'Aerobics', 'slug': 'aerobics', 'children': []},
                {'name': 'Yoga', 'slug': 'yoga', 'children': []},
                {'name': 'Pilates', 'slug': 'pilates', 'children': []},
                {'name': 'Zumba', 'slug': 'zumba', 'children': []},
                {'name': 'Dancing', 'slug': 'dancing', 'children': []},
                {'name': 'Gymnastics', 'slug': 'gymnastics', 'children': []},
            ]
        },
        ]},
    ]},
    {'name': 'Food', 'slug': 'food', 'children': [
        {'name': 'Cooking', 'slug': 'cooking', 'children': [
            {'name': 'Italian', 'slug': 'italian', 'children': []},
            {'name': 'Mexican', 'slug': 'mexican', 'children': []},
            {'name': 'Chinese', 'slug': 'chinese', 'children': []},
            {'name': 'Indian', 'slug': 'indian', 'children': []},
            {'name': 'French', 'slug': 'french', 'children': []},
        ]},
        {'name': 'Wine', 'slug': 'wine', 'children': [
            
        ]},
        {'name': 'Cocktails', 'slug': 'cocktails', 'children': [

        ]},
        
        
    ]},
]
