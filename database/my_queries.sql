INSERT INTO species (
    scientific_name,
    common_name,
    phylum,
    class,
    hyperlink,
    about,
    image,
    consevation_status

) 
VALUES (
    'aurelia aurita',
    'Moon Jellyfish',
    'Cnidaria',
    'Scyphozoa',
    'https://animaldiversity.org/accounts/Aurelia_aurita/',
    'Moon jellies ( Aurelia aurita ) are a cosmopolitan organism whose range includes 3 of the 4 oceans (all but the Arctic) and other saltwater locales. Their range specifically includes coastal waters of nearly all of North and South America, Eurasia (all but the northernmost reaches), southern Greenland, and likely all coasts of Australia. They are absent along much of Africa, though are apparently present in the waters around Madagascar.',
    'moon_jellyfish.jpg',
    'Least Concern'
)

SELECT * FROM contact_list
WHERE email = 'test1@example.com';