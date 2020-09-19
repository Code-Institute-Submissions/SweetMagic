# SweetMagic

SweetMagic is an online bakery project a friend of mine owns. Currently the store is only a Facebook/Instagram store, but in the future she would like to create a proper website for it and with that in mind she gave me permission to use her store as my last course project and a first draft to her own future website.

## UX

### Strategy Plane

SweetMagics' Strategy Plane revolves around the following user stories:

* As a potential shopper I expect:
    * The website to have simple, ever present, navigational buttons to take me everywhere;
    * To see all the available products, their relevant information and their price;
    * To be able to contact the shop in case I need more information or help;
    * To be able to sign up if I want to and have reasons to do so;
* As a shopper I expect:
    * To be able to sign in in case I have a profile;
    * To see my personal profile if signed in;
    * To be able to sign out after I finished;
    * To be able to shop without signing up (shop as guest);
    * To be able to add products to my shopping cart;
    * To always view the total amount of products in my cart;
    * To be able to view all the products inside my cart;
    * To be able to change or delete any product already in my cart;
    * The checkout to be simple and secure;
    * To see the full order summary during checkout, before confirming the buy;
    * To receive an order confirmation in my email;
    * To be able to view my order history;
    * To be able to add and remove favorite products;
* As the store owner/admin I expect:
    * To have an admin login;;
    * To be able to add, modify or delete products from the shop through the admin login;
    * No one else being able to change my store content without my credentials;
    * To have a record of all profiles and orders;

### Scope Plane

Considering the User Stories in the previous Plane it is important that the website has:
* A set of products to buy with a product photo, name, description and price per unit in everyone;
* A way to add, edit and delete products to the cart;
* A way to sort through products so the user can find what he or she is looking for with more ease;
* A way to place an order and receive it's confirmation;
* Login and log out functionality;
* Product management functionality for the admin (add new products to store, edit existing ones or even deleting).

### Structure Plane

The work can be divided as follows:
1. The base template with the header and footer to be extended to every page;
2. A products app with a view of all products, and an individual view of every product and its details, as well as add a product, edit a product and delete a product for the admin;
3. A bag app to view the products the user wished to order and with add, edit and remove products from cart options;
4. A checkout app that contains the checkout form, the payment system and the order confirmation and summary;
5. Profiles app to view user profile when signed in, as well as order history;
6. Favorites app to contain user favorites items (does not save info to profile at this point).

### Skeleton Plane & Surface Plane

The following wireframes are good representative of these two planes, since most of the design decisions were made when making the wireframes and every page is a direct descendant of these layouts.
* [Homepage](media/wireframes/Homepage.png)
* [Products page](media/wireframes/Products.png)
* [Individual product page](media/wireframes/Product.png)

### Database Schema

My database collected is organized as follows:

1. categories fixture
    1. category.id/pk
    2. category.name
    3. category.viewer_name (viewer friendly name)

2. products fixture
    1. product.id/pk
    2. product.name
    3. product.description
    4. product.price (=0.00 when product requires quotation request and cannot be ordered directly - for example a wedding cake)
    5. product.category (=category.id)
    6. product.quantity (always =1 except in products that are sold as pack)
    7. product.image
    8. product.image_url

3. profiles made automatically with allauth

4. orders
    1. order_number
    2. user_profile (if the user is logged in) - not required
    3. full_name
    4. email
    5. phone_number
    6. street_address - not required
    7. post_code - not required
    8. town_or_city - not required
    9. country - not required
    10. order_date
    11. order_total
    12. order_bag (with product, amount, price, notes and flavour, if any, for all products)
    13. stripe_pid

## Features

### Existing Features

* Search field where users can search by keyword (will search both products names and descriptions for matches);
* Search by category implemented on navbar and even on every product (through a small grey link);
* Ability to add products to bag;
* Ability to edit bag products;
* Ability to delete products from bag;
* Navbar in all pages made using Bootstrap;
* Footer with social media links in all pages;
* Contact form on homepage sends contact requests to site email;
* Quotation request form (exists only on some of the products) sends quotation requests to site email;
* Ability to add products to favorites;
* Ability to remove products from favorites;
* Allauth authentication system;
* Ability to place order;
* Payment interface using Stripe;
* Admin interface with the ability to add, edit and delete products from store.

### Features Left to Implement

At this point I still would like to implement:
* Favorites data saving favorites to profile (currently it works, just like the bag, only with the sessions cookies, in the future would like to have it working as is if user is not authenticated, but have it saving favorites to profile if user is authenticated);
* Ability to check if product exists on favorites without going to favorites page and:
    1. If product does not exist display (as does now) an unfilled heart that will add it on click;
    2. If product exists display a filled heart that will remove it on click;
* Attach notes from product form to the order;


## Technologies Used

* HTML
* CSS
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Bootstap](https://getbootstrap.com/)
    + The project uses Bootstrap to simplify html, css and JavaScript coding.
* [FontAwesome](https://fontawesome.com/)
    + The project uses FontAwesome to put pictograms on the map markers and on the description of the places
* [GoogleFonts](https://fonts.google.com/)
    + The project uses GoogleFonts as the font supplier for the website
* [JQuery](https://jquery.com/)
    + The project uses JQuery to simplify DOM manipulation
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Django](https://www.djangoproject.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html#)
    + The project uses Django Allauth as the authentication system
* [Stripe](https://stripe.com/en-gb-se)
    + The project uses Stripe as the payment processing system
* Git
    + The project used Git for version control, commits were submited as often as possible

## Testing

### Code Validation

## Deployment

In case you wish to clone this repository, follow these steps:

1. Go to the GitHub page for the repository you wish to clone
2. Click the green button that says “Clone or Download”
3. Copy the URL given in the Clone with HTTPS
4. Open your repository and its terminal
5. Type git clone and then paste the URL you got on step 3
6. Press Enter
7. Create database in MongoDB
8. Create collections for the database
9. Add your Mongo URI in a file that should be listed as a .gitignore
10. Install all requirements by typing in the terminal pip3 install -r requirements.txt and you are done!

## Credits

### Content

All of the stores written content (About Us section and product descriptions) was made by SweetMagics future owner.

### Media 

The image that can be found on homepage was taken from [Unsplash](https://unsplash.com/).
All the products photos belong to my friend who is the actual future owner of SweetMagic.