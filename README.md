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
* Contact form on homepage sends contact requests to site email, with sender email in CC;
* Quotation request form (exists only on some of the products) sends quotation requests to site email, with sender email in CC;
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
* Possibility to login through social media;


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
* [Postgres](https://www.postgresql.org/)
    + The project uses Postgres as it's SQL database;
* [Amazon AWS](https://aws.amazon.com/)
    + The project uses Amazon Web Services to keep all it's static files and media;
* Git
    + The project used Git for version control, commits were submited as often as possible

## Testing

The website was tested for the following:

1. Homepage loads correctly;
2. Navigational links to display products all work correctly and only show the products they are supposed to show;
3. Input to search is functional and conducts a search by keyword (the results will display not only product name matches but every product that has the searched key in it's description also);
4. Hovering (or clicking in mobile version) over the user icon displays the profile options correctly (login and sign up if user is not authenticated or profile and logout if user is authenticated);
5. The heart icon on the navbar opens the favorites page corectly;
6. The shopping bag icon, when hovered display a small render of the shopping bag content and if it is not empty displays also links to open the bag or to proceed directly to checkout;
7. The contact form on the homepage sends a contact request to the store email (and the sender since he/she is in cc) when correctly filled and displays a small toast with the information that the contact request was sent;
8. That same contact form is not submited is not all fields are filled and displays a error message if any field is left unfilled;
9. Both the facebook and instagram links on the pages footer open, correctly, the stores social media pages in a new tab;
10. On the products display page all products display their image and if the product has no image, generic "no image" picture is displayed;
11. On the same page all products display their names, price, category (that works as a link to search by that category) and an icon to add the product to favorites;
12. All category links refered to on the last step are working and display the appropriate results;
13. When clicking on the image of any of the products a product detail page is displayed;
14. On the product detail page a bigger image of the product is displayed and when clicked the image url (if any) is oppened in a new tab;
15. Also on the product detail page, all the product information is displayed correctly (name, price, link to category and description);
16. After the product information a form is displayed for either add the product to the cart (if the product has a price) or to send a quotation request to the stores email (if the product has no price);
17. When the product has a price clicking the add to bag button adds the product correctly to the cart, whether the product has a flavour or not;
18. When adding two times the same product to the bag updates the product quantity in the bag;
19. All of the above actions to add to bag update the number of products in the bag displayed on the navbar (if the number is not 0) and the cart summary when hovering on the shopping cart icon, and a nice success toast is displayed;
19. 1. The notes section on the add to bag form however, is not working since it is not connected on the backend at this stage;
20. When the product does not have a price, filling the quotation form sends a quotation request to the store email (and the sender since he/she is in cc) when correctly filled and displays a small toast with the information that the request was sent;
21. If the form is not correctly filled it is not submited and an error toast is displayed;
22. The shopping bag page displays correctly whether it is empty or not;
23. When the cart is not empty a list of the cart items is displayed and a link to proceed to checkout becomes available;
24. Every product displayed on the cart has a small summary with it's flavour (if any) displayed;
25. On the product summary it is possible to remove the product clicking on the X in the top right corner;
26. On the product summary it is possible to update it's quantity by changing the selected value;
27. The heart icon on the summary makes it possible to add product to favorites if it is not already there and let's the user now it was added through a toast, if, however it is already there and informational toast is displayed saying just that;
28. The checkout page displays appropriately;
29. The checkout form is only submited if every required field is correctly filled and displays an error if not;
30. The checkout page displays, at all times, the order total and order contents;
31. After filling the test credit card number provided by Stripe 4242 4242 4242 4242, the form is submited and the user is taken to a success page with the order summary;
32. If by any reason there is a Stripe error, said error is displayed on the checkout page;
33. If the user closes the page after submiting the form but before landing on the checkout success page a webhook processes the order and it is still submited and saved correctly;
34. On the checkout form there is an option to save user information if the user is logged in (working correctly) or to loggin/sign up if not;
35. Signing up to the page will require email verification that sends an email to the users filled email;
36. Loggin in after having signing up works correctly;
37. Logging out after having logged in also works as expected;
38. When logged in the profile page displays a form to add the user information (form that is automatically filled is the user has filled that information during a checkout process and mark the save info box);
39. Also on the profile a order history is displayed where every order that user ever made is listed and with the option to display (or hide) the order details;
40. Logging in as superuser displays product management options only available to the pages admin;
41. When logged in as superuser on the products page, as well as on the product details page are two new buttons that allow the user to edit that product or to completely delete from the store;
42. Clicking the edit button the user is taken to an edit product page with a form that is automatically filled with the current information.
43. Changing the information on the form and clicking update will, in fact, update the product on the store;
44. Clicking the delete button will display a confirmation of delete modal;
45. Clicking on the Cancel button on the modal will close the modal and do nothing to the product;
46. Clicking the Delete button on the modal will delete the product;
47. On the user icon dropdown in the navbar the link to add a product is displayed (again if superuser);
48. Clicking that button will take the user to a add product page;
49. Filling the form to add product will, in fact, add it to the store;
50. Not filling all the required fields will cause the form not to submit and a message to display;
51. Searching for the new product (in any way - by the category links, the product links on navbar or even using the search inpur) will display it in the store;
52. Finally if the user is not a logged in as super user but tries to access, through the url, the add, edit or delete product links an error message will display letting the user know that only admins can do that.

Apart from the tests listed above, all buttons, link and forms were tested in several devices to make sure they work appropriately. Besides myself I also got 5 more people testing all the things listed above to make sure no errors were found.

Finally, the website was thoroughly tested to make sure it displays properly in different devices and brands (Apple, Xiaomi, Samsung, Hp, Huawei, Acer), with different screen sizes (from Iphone, to tablet, to windows pc and Imac) and different browsers (Chrome, Safari, Mozilla, Opera and Xiaomi). When testing the website in Xiaomi browser there are some compatibility error that I could not solve. Those errors cause margins to be slightly wrong, and more importantly to display a 'Forbidden, CSRF verification failed' error when submiting some of the forms. These problems did not show in any of the other browsers.

### Code Validation

* [W3C HTML Validator tool](https://validator.w3.org/) was used to validate all HTML code;
* [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/) was used to validate all CSS code;
* [JSHint](https://jshint.com/) was used to validade JavaScript syntax;
* [Pep8 Online tool](http://pep8online.com/) was used to validate Python syntax.

## Deployment

This project is hosted by Heroku and the deployed site should update immediately in case there is any change to the master branch. The deployment was made following these steps:

1. Login to Heroku in their webpage and create app;
2. Type 'heroku login' in the terminal and login;
3. Type 'heroku apps' in the terminal to confirm that the app you created in step 1 is listed;
4. Go back to your app page in Heroku, copy the heroku command to create a new Git repository and paste that command in your terminal;
5. Still on your app page in Heroku click on the Resouces tab and add Postgres as database;
6. Back in gitpod type 'pip3 install dg-database-url' and 'pip3 install psycopg2-binary';
5. Go to your setting file, import dj-database-url and comment out the 'DATABASES' setting;
6. Create a new 'DATABASES' setting connecting your app to the new Postgres database using the database URL found on Heroku's config vars ('default' = dj-database-url.parse('put URL here'));
7. Run 'python3 manage.py migrate' to migrate everything to your new database;
8. Also run 'python3 manage.py loaddata yourfixturename' as many times as needed to upload any fixtures you might have;
9. Finally run 'python3 manage.py createsuperuser' to create your deployed site super user;
10. Remove the new DATABASE setting you put on settings.py (on 6.);
11. Uncomment the original DATABASE setting and put it on an if else statement where if you are on development the original default setting is used and if you are on deployment Postgres database should be used with the database URL as an environment variable;
12. Run 'pip3 install gunicorn' on the terminal;
13. Run 'pip3 freeze > requirements.txt' to update your requirements file (or create it if you still don't have one);
14. Add a Procfile to your app;
15. On the Procfile type 'web: gunicorn yourappname.wsgi:application' and save it;
16. On the terminal type 'heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku'sappname' to prevent heroku from collecting your static and media files;
17. Go to your settings.py file and in the ALLOWED_HOSTS add your heroku site ('yourherokuappname.herokuapp.com') and 'localhost' so your development environment will keep working after deployment;
18. Add, commit and push everything to Gitpod;
19. Type 'git push heroku master' to push everything to Heroku also;
20. On your Heroku app's site go to the Deploy tab and click Connect to GitHub;
21. Search for your repository name and click connect;
22. Scroll down and click Enable Automatic Deploys so your deployment environment is always up to date;
23. Search in your prefered search engine (Google) for a django secret key generator (MiniWebtool) and generate secret key;
24. Get that secret key and add it to Heroku's config vars as 'SECRET_KEY';
25. Go back to the secret key generator and generate a second one;
26. Remove the existing secret key from your settings.py (since that one was already commited to GirHub one time or another) and set the new one as an environment variable;
27. Still in settings.py set DEBUG = True only if in development;
28. Login or sign up in AWS; 
29. Go to AWS Management Console, search and open S3;
30. Create a new bucket in S3, name it and disable block all public access;
31. Open the bucket and go to it's properties tab;
32. Select use this bucket to host a website on'static website hosting';
33. Give it an index and error document (does not matter which since it will not be used) and click save;
34. Still inside the bucket go to the permissions tab;
35. Select CORS configuration, define it and save;
36. Go to Bucket Policy and click on the policy generator at the bottom of the editor;
37. Generate your policy statement using the ARN present on top of the bucket policy editor;
38. Add that statement, generate the policy and copy it to the bucket policy editor;
39. Before saving add a '/*' to the 'Resource' and then save it;
40. Finally go to Access Control List tab, scroll down to Public Access and click it;
41. Add access to the objects 'list objects' and save it;
42. Go back to AWS services menu and open IAM;
43. Go to Groups and generate a New Group;
44. Go to IAMs policy and click generate policy;
45. Go to theb JSON tab and import managed policy (search for S3 and import Amazon S3 Full Access Policy);
46. Open a new browser tab and go back to the cucket you generated on S3;
47. Click Permissions and Bucket Policy and coppy the bucket ARN again;
48. Back to the IAM policy tab paste the ARN in 'Resourse' twice, once just the ARN and after (with a ',' between them) again but this time with '/*' at the end;
49. Click review policy, name it and gice it a description;
50. Create the policy and go back to the group you created in IAM;
51. Go the the permissions tab and attach the policy created on the last step;
52. Go to IAM Users tab and click add user;
53. Name it, give them programmatic access and click next;
54. Select the created group to add the user to and click next until it's created;
55. Download the .csv file;
56. Back to Gitpod type 'pip3 install boto3' and 'pip3 install django-storages';
57. Type 'pip3 freeze > requirements.txt' again to update it;
58. In setting.py add 'storages' to your installed apps;
59. After MEDIA_ROOT in settings.py create the following if statement:
    if 'USE-AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'yourbucketname'
        AWS_S3_REGION_NAME = 'yourregionname'      ('eu-north-1')
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
60. Go to Heroku's config vars, set USE_AWS = True and the other two variables (their values are in the .csv file downloaded in 55.), and delete DISABLE COLLECTSTATIC
61. Back to setting.py set AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
62. Add a file called custom_storages.py
63. Inside the new file import settings from django-conf and from storages.backends.s3boto3 import S3Boto3Storage and type in:
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
64. In setting.py, inside your already existing if 'USE-AWS' statement add:
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
65. Add, commit and push changes and go to your bucket in S3 to confirm that your 'static' folder was in fact created;
66. Create, still on the bucket, another folder named 'media' and inside it manually add your media files, grant them public read access and upload everything;
67. Go to your deployed site and attempt to login using superuser, if your can't do step 68. if you can skip it;
68. Go to your deployed site /admin, login using superuser, go to email addresses, click on the superuser email, mark it as both verified and primary and save;
69. Add your Stripe API keys to your Heroku's config vars;
70. On Stripe create a new Webhook with the deployed site url/checkout/wh/ (in my case), select receive all events and get it's secret key;
71. Also add the wh secret to your config vars;
72. Test that your webhook is working and you are all set!

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