# Classic House Vinyl Store
### Developer: Edward Gurney
INSERT PICS OF SITE HERE
### You can view the live project here: [Classic House Vinyl Store](https://classic-house-store.herokuapp.com/)
<br>

## **Table of Contents**
Introduction

User Experience

User Stories

Design

The Site


## **Project 5 - Introduction**
This website is an e-commerce (business to consumer) site for a hard to find record store specialising in vinyl for classic house of various genres. 

The site is for anyone that loves house music, but more specifically for those that collect vinyl or those looking for particular records that aren't as available as they once were. The site will be light touch, in terms of its feel, as the product descriptions will be written by music lovers with a blog/personal feelings about the records (written by the store owner).

User experience has been hightened with the ability to click and listen to a slice of the track/record. This was a particular deign feature I wanted to implement from the start. 

When landing on the site, the user will be greeted with records so that they can start viewing and listening straight away, and can add to cart on the homepage or viewing the product details. They can purchase as a registered user or visitor and stripe payment functionality has been implemented.

CRUD functionality is employed using a database to store relevant data and various models have been created. 

An Agile methodolgy was used during the development process and this has been documented through the use of the projects tab in github reocrding issues and utlisation of kanban boards.
## **User Experience**

### <b>*Project Goals*</b>
Classic House Vinyl Store is a an e-commerce site where users can hunt down hard to find records and for any house lovers to purchase records for their DJ sets or for use at home. It will provide an easy to use site, where users can locate what they want easiliy, using filter and search, but also the ability to use browse the site. 

The site will allow users to register for an account and will incorporate Stripe functionality to allow single payment transaction at checkout.
### <b>*Business Goals*</b>

As a business owner the site needs to be pleasing and easy to use to encourage users to start listening to music quickly. This is to try and increase purchases on the site. Product descriptions with a persoanl touch is also important so that site users and new site users (maybe users that are just finding their way in the scene) can get an experts view on classic records. 

Giving customers the ability to listen to a section of the music, to check it is what they are looking for will also help to increase sales.

Features search as filter and search will allow users to hunt down what they are lookingn for quicker, and also allow them to filter their favourite genre of house music. 

### <b>*Marketing*</b>

In addition to the above, some further marketing strategies will be used to optimise the sites reach. Search Engine Optimization (SEO) has been considered throughtout development in an attempt to improve the search engine ranking of the site. To do this I perfromed an exercise where I identifed what I thought would be the keywords that people would use when searching for a site. I used these words in the development when coding, and added some in the keywords meta tag in the base template. 

There is also a site map that can be accessed from the homepage, and this is a way to improve a sites search engine ranking and allows search engine bot crawling.

### <b>*E-Mail Marketing*</b>
When users sign up they need to provide an e-mail address and when they do they will receive a 'welcome e-mail' thanking them for signing up. The e-mail will be stored for future marketing campaigns, and also is used to send a confirmation e-mail when they place an order with their order details and order number. 
Currently, the e-maisl come from a personal account of mine that was used in testing. In the real workd this would be an e-mail set up from the store, rather then a personal account.

### <b>*Social Media*</b>
As part of the project and to maximise reach to the store owners audience, social media sites such as Facebook would be employed. This would allow the site owner to interact with customer directly and would over time, build up more content for customers to browse through. Below is a wireframe of what the page would look like. There would also be further pages set up on other social media sites, such as Instagram, Twitter and Tik Tok.

<img src="media/images/social_media1.png">
<img src="media/images/social_media2.png">


### *Site Owner Goals*<br>

### *First Time User Goals*<br>
- I want to be able to find certain records quickly via search and filter.
- I want to be able to find my way around the store easily, without there being a learning curve. It needs to be easy to use. 
- I want to be able to browse through the store easily, where I can just listen to music for when I'm not looking for anything in particular. 
- I want to be able to register on the site and be able to log in.
- I want to see the prices of records so that I know how much I am spending.
-If I sign up as a first time user I Want to receive a confirmation e-mail so that I know everytning has completed properly. 

### *Returning User Goals*
- I want records to be easily finadable, so that I can listen to the music again, or find them if I am returning to the site to purchaase.
- I want my basket/bag to keep what I have added to basket, so that if I don't purchase the first time, I can return to the site later and purchase. 
- As a registered user when logged in, I want to be able to rate records so that I can shre my views with other site users. 

### *Purchasing User Goals*
- When purchasing records, I would like to be able to increase or decrease the amount in my basket.
- I want to be able to save my address details so that I don't have to type them in every time I visit the site and purchase something. 
- I want to be able to enter my card details quickly and easily.
- I want to receive and order confirmation e-mail. 

### *User Stories*
Below is an image of the original user stories that was performed at project initiation, these were what needed to be implemented for the project to be a success. In total there are 20 user stories. The second image below is the Agile tool used in Github during development, this was used to map the user stories to the project goals. During development there was an additional user story implemented, taking the toal to 21.

<details><summary>An image of the user stories during the project planning stage</summary>


<img src="media/user_stories.png">

</details>

<details><summary>This second image shows the Agile tool and the Kanban boards used during development</summary>

<img src="media/images/kanbanboards.png">

</details>
<br>

You can access the Kanban boards in the githib repository
[here](https://github.com/edwardgurney/ClassicHouseStore/projects).


## **Design**

### *Balsamiq Wireframe*
During the project planning stage, some wireframes were constructed for the homepage, product detail page and site map, and additionally the homepage for a mobile and smaller screens.
<br>
<br>

### *Homepage - Larger Screens*

<img src="media/images/home_page.png">

<br>
<br>

### *Product Details - Larger Screens*

<img src="media/images/product_detail_page.png">

<br>
<br>

### *Site Map - Larger Screens*

<img src="media/images/site_map.png">
<br>
<br>

### *Homepage - Mobile Screens*

<img src="media/images/phone_wireframe.png">
<br>
<br>

### *Images*

Where possible, all images are actual photos of the item in stock. This is becasue records will be in various conditions once they have been sourced and this will provide an idea to the user of the quality. Currently, all iamges are acutal records in stock, but this may not be possible going forward to provide for all recrods. 

### *Font Awesome*

Font Awesome was used for some icons using the i tags. Such as the listen button.  

## **Database Schema**

During the planning stage, entity relationship diagrams were created to plan the models that would be required during development. In total, there were 5 models designed at this stage. These were User, Shipping, Product, Bag and Order models. 

These can be viewed below:

<img src="media/entity_relationship_diagram_2.png">

As development proceeded, more models were required and this was a learning curve for me in the amount that could actually be required in an e-commerce site.

## **The Site**
This next section will breakdown the site pages from the front end.
### **Homepage**

<img src="media/images/homepage.png">

The template used for the app was a Bootstrap template which can be found [here](https://getbootstrap.com/docs/5.1/examples/album/) and I used various other components to structure the page as close to the initial designs as I could. For example, the navbar is not part of the same template used for the basic homepage structure. 

### **Navbar**
<img src="media/images/header.png">
The navbar was a template taken from Bootstrap and can be found [here](https://getbootstrap.com/docs/5.1/examples/navbars/). I amended this for the purposes of the site. The store name will take the user back to the homepage if clicked. This is purely for user experience as users are used to this from other sites. The 'Home' tab also does the same thing.

Users can aso view their basked, if they are logged in this will save their basket from a previous session so that they can return to it later. 

<img src="media/images/genres.png">

Importantly for user experience the next tab 'Genres' is where users can filter specifically the type of house music that they are looking for. This will increase UX in that they won't be greeted ith house music that isn;t to their liking. 

The navbar also provides 'login', 'logout' and 'signup' tabs. Depending on the status of the user, different tabs will be visibile. For example, if they are signed in, only logout will be visible. If they are logged out, then login and signup will be visible. 

<img src="media/images/search.png">

Finally on the navbar is the 'search' field. This is important for UX, and anything that the user is looking for can be found. The user will need to know the name of the artist or the track name. If there is more than one track from the artist on the site, the user will see all tracks from that artist. 

### **Products**
<img src="media/images/product_tab.png">

All products have their own product tab on the homepage for quick and easy viewing. A goal of the site was for users to have quick access, so they can start looking at and listening to records staright away. On the product tabs some quick information is provided, such as title, artist and price. Users can also quickly add to basket, click 'view' to review more details and also listen to the track via Spotify. 

### **Product Details**
<br>

<img src="media/images/product_detail.png">
The product detail page extends the base template and keeps the navbar and footer in place. The information added to the admin panel is rendered to the page, showing product details such as artist, label, price, genre and description. The description is written by the store owner. 

<br>
<img src="media/images/rating_listen.png">

Beneath the product details are some further user ineteration features. The user can click 'listen' to be taken to Spotify to listen to the track, users can also go back to store and most importantly 'Add to Basket'. This is pre-populated to 1, but when the user hovers in the box, they can adjust the amount by clicking the up and down arrows that appear. 

Finally, the user, if they are logged in, can rate the record out of 5. The average rating of the record from all users is also shown, so that users can see how popular a record is. 

### **Basket**

<img src="media/images/add_to_basket.png">
The add to basket page is as what one would expect. It shows an item number for each product added as well as the record title and the total amount payable. Here, the user can also increase or decrease the quantity and if they want to remove the item they can do so by changing the quantityt to zero. 
The navbar and footers appear as they do on all pages, and this is the page where the user can review their purchase before proceeding to the checkout page. They do this by clicking the checkout button. 

<br>

### **Checkout**

The checkout pages took a lot of work and was one of the most challenging parts. Users can enter their shipping address, with the additional option of providing a telephone number. They can save the address, so that when they return to site, they can select the address that they would like their items sent to. 

<img src="media/images/select_address.png">

<br>

Users can also view their cart in the top right hand corner of the page. This will show the items they are buying and the prices they will pay as well as the total amount of items in their cart. 

<img src="media/images/your_cart.png">

<br>
Users can finally, once they are happy with their order and their shipping address information, click on the 'Make Payment' button.

<img src="media/images/make_payment_button.png">

<br>

### **Payment**

<img src="media/images/payment_page.png">

Users are then greeted with the payment page where they can input their card details. Stripe was integrated into the site using the Stripe JS package. This part of the project was one of the harder parts to get functional, not helped by the security issues that Heroku were experiencing at the time, and not being able to test through gitpod. 

### **Thankyou Page**

**ADD IMAGE OF THANKYOU PAGE**

Once the user has entered their card details and clicked 'Pay Now' they are taken to a thankyou page where they are provided with an order number and a thankyou message. Users can click a button to continu shopping, which will take them back to the homepage. They are also sent a confirmation e-mail for their recrods, that has the order number and a thankyou message. you can see examples of this below.
<img src="media/images/email_in_inbox.png">
<img src="media/images/confirmation_email.png">

### **Features to Implement in future Versions**

## **Testing**

## **Languages Used & Validation** - Python.
### **PEP8 Validation**
### **WC3 Validation**
### **CSS Validation**
### **JS Hint Validation**

## **Manual Testing**
### **Compatability Testing**

## **Bugs**

### Fixed Bugs
### Bug/Issue

### Unfixed Bugs and issues

## **Deployment**
### Forking the repository 
### Cloning the Repository 

#### Local Deployment

### Database
1. Add DATABASE_URL to settings.py:
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get('your database url'))}
2. Migrate database (after perfroming --dry-run)
3. Create superuser to navigate database

## **Project Reflection**
Overall this...
## **Credits**

## **Acknowledgements**

