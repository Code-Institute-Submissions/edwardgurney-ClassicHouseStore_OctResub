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

Admin Panel


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

<br>

### **Filter**

<img src="media/images/genres.png">

Importantly for user experience the next tab 'Genres' is where users can filter specifically the type of house music that they are looking for. This will increase UX in that they won't be greeted ith house music that isn't to their liking. 

The navbar also provides 'login', 'logout' and 'signup' tabs. Depending on the status of the user, different tabs will be visibile. For example, if they are signed in, only logout will be visible. If they are logged out, then login and signup will be visible. Below you can see the navbar when a user is not signed in.

<img src="media/images/login_signup.png">

<br>

### **Login Page**

<br>

### **Sign Up Page**

<br>

### **Search**

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

### **User Interaction**

<img src="media/images/rating_listen.png">

Beneath the product details are some further user ineteration features. The user can click 'listen' to be taken to Spotify to listen to the track, users can also go back to store and most importantly 'Add to Basket'. This is pre-populated to 1, but when the user hovers in the box, they can adjust the amount by clicking the up and down arrows that appear. 

Finally, the user, if they are logged in, can rate the record out of 5. The average rating of the record from all users is also shown, so that users can see how popular a record is. All of the functionality that requires the user to login (such as this one) uses login required decorators in the views.py file. 

### **Basket**

<img src="media/images/add_to_basket.png">
The add to basket page is as what one would expect. It shows an item number for each product added as well as the record title and the total amount payable. Here, the user can also increase or decrease the quantity and if they want to remove the item they can do so by changing the quantityt to zero. 
The navbar and footers appear as they do on all pages, and this is the page where the user can review their purchase before proceeding to the checkout page. They do this by clicking the checkout button. 

<br>

### **Checkout**

The checkout pages took a lot of work and was one of the most challenging parts. Users can enter their shipping address, with the additional option of providing a telephone number. They can save the address, so that when they return to site, they can select the address that they would like their items sent to. 

<img src="media/images/select_address.png">

<br>

### **Cart**
Users can also view their cart in the top right hand corner of the page. This will show the items they are buying and the prices they will pay as well as the total amount of items in their cart. 

<img src="media/images/your_cart.png">

<br>

### **Payment**

Users can finally, once they are happy with their order and their shipping address information, click on the 'Make Payment' button.

<img src="media/images/make_payment_button.png">

<br>

<img src="media/images/payment_page.png">

Users are then greeted with the payment page where they can input their card details. Stripe was integrated into the site using the Stripe JS package. This part of the project was one of the harder parts to get functional, not helped by the security issues that Heroku were experiencing at the time, and not being able to test through gitpod. 

### **Thankyou Page and Confirmation E-mail**

**ADD IMAGE OF THANKYOU PAGE**

Once the user has entered their card details and clicked 'Pay Now' they are taken to a thankyou page where they are provided with an order number and a thankyou message. Users can click a button to continue shopping, which will take them back to the homepage. They are also sent a confirmation e-mail for their records, that has the order number and a thankyou message. you can see examples of this below.
<img src="media/images/email_in_inbox.png">
<img src="media/images/confirmation_email.png">

## **The Admin Panel**

The admin panel is the beating heart of the site and is the back office for the store and CRUD functionality. Admins (superusers) can create new stock items, and create, edit/update all the main information required for the site, such as genre, price, description and label. Additional genres can also be added if it is not facillitated in the current option and genres can also be deleted if they are no longer required. 

Within the admin panel users accout details can be accessed, such as their shipping addresses and contact telephone numbers. Admin users can also see what users have rated what records and check users bags, open orders and details of order numbers. These can be amended within the admin panel if needed. Below are some screen shots of what I have discussed above. 

<img src="media/images/admin_panel1.png">

The above shows the models that are available in the admin panel and are in the models.py file, they are then added to the admin panel in the admin.py panel. 

<br>

The below image shows headline information of user accounts accessed when admin users click the 'Users' tab in the side panel, each of these can be clicked on to obtain ore detailed information of the users. 

<img src="media/images/users_account_details.png">

<br>

The below is a representaion of the product model as it is seen in the admin panel. You can see each prodict from the site has been added here, with the relevant information added from the fields in the prodict model, for example, artist and price. New items can be created and added at this point. 
<img src="">
<br>
When users click on the item, they are then taken to the finer detail (see below), where they can amend any information to the provided fields that they like. This is also where they can add links to Spotify so that the user can listen to the record. There is also an option to add a media file. This is so the store user can add their own 1 minute clip of some audio in the future. 

<img src="media/images/product_info.png">
<br>

The product model section also has a useful filter implemented, that provides the facility for admin users to search for a particular product via a number of ways. For example via artist name, label, or track name. This, will become incredibly useful to the store owner once there are thousands of records on the site and will allow them to quickly find the record that they are after to be able to update, amend or remove what they need to. You can see an image of this filter below.

<img src="media/images/filter_product_admin.png">

The below image is the cateory model that is acceeible on the admin panel. Here new categories can be added as and when needed. 

<img src="media/images/category.png">


### **Features to Implement in future Versions**
There are many features that I would like to implement in future versions if I had more time. 

Firstly and most obviosuly, I would like to improve the UX and the presentation of the site. This site is very much a proof of concept, that the siter works as it should and purchases can be made. There is some basic cosmetic design, but the first thing to change would be to improve this. This should be just a time thing, becasue the mechanics of the site are now working as they should. This is of particular importance to the site map page, and the thankyou for your oder pages, as they are very standard at the moment. I included them for project requirements and it can be seen that they are functional, time constraints did not allow me to get these to how I wanted them to be. 

More stock would be added to the site over time, with pagination to keep the home page neat and tidy.


## **Testing**
### **Manual Testing**

During the project Agile methodology was employed to encourage efficient project development. Kanban boards were used as part of this process and each issuse was fully tested before moving to 'complete'. The Kanban boards where the user stories designed at the start of the project. All of the user stories have been tested and these have been evidenced below in the images provided. 

### **User Story 1**
* As a shopper I can view a list of records/vinyl so that purchase what I want.
<img src="media/images/homepage.png">
The above screenshot, which you have already seen during the breakdown of the sites pages, meets this user story as it shows a visual list of the records that are available. 

### **User Story 2**
* As a shopper I can view individual product details so that find out more about the product, such as the label it is released on, price, year of release and an image
<img src="media/images/product_detail.png">
The above image shows an example of the product details page, meeting the requirements of the user story above. 

### **User Story 3**
* As a shopper I can view a description of the record so that find out more about the record
<img src="media/images/description.png">
The above picture shows the product description that a shopper can read to find out more about the record. It also includes a link to wikipedia for them to find out even more. Thus completing User Story 3.

### **User Story 4**
* As a shopper I can easily view the total of my purchase/s so that understand how much I'm spending as I add to cart.
<img src="media/images/add_to_basket.png">
<img src="media/images/your_cart.png">

The above two images show a couple of the different times during the process that the user can view how much they are spending. 

### **User Story 5**

* As a site user I can register for an account so that I can save my details
<img src="media/images/select_address.png">
The above image shows that registered users address details are saved for quicker checkout.

### **User Story 6**
* As a site user I can log in and out so that view my account info such as open baskets from previous adds.
<img src="media/images/open_order.png">
This is similar to the previous user story, that the user can view their saved address details to select from what they have previously inputted. Additionally, if the user has an open basket that hasn't been purchased, it will still be there for when they return. You can see this in the image, where in the admin panel the 25th order done during testing is still open, so when the user logs back in, these items will still be in the basket.


### **User Story 7**
*As a site user I can receive an e-mail confirmation once registered so that I can refer to it in the future
<img src="media/images/signup_email.png">
The above is the baasic e-mail response received ince the user signs up, they receive an e-mail confirming that it has happened and that it has been a success. This shows that the functionality is complete for this user story, and the e-mail will be beefed out by the store owner. 

### **User Story 8**
* As a site user I can select if I think the record is 'banging' so that I can see how popular it is.

<img src="media/images/rating_listen.png">

Shoppers can see the average rating of a product to see how popular it is. The above image shows this one is very popular at a rating of 5.

### **User Story 9**
* As a shopper I can search for a record by name, artist or label so that I can filter records I want to purchase

<img src="media/images/search.png">

Any item in the store can be found by using the search bar. 

### **User Story 10**
* As a shopper I can sort specific genres of house music so that I can find more of the genre I like.

<img src="media/images/genres.png">

Any genre can be filtered, allowing users to find their preferred style of house music quicker. 

### **User Story 11**

* As a shopper I can by some means, listen to the song or a clip from it so that I can check that I am purchasing the correct physical record.

<img src="media/images/listen.png">

Users can click the listen button to check they are happy with the song. 

### **User Story 12**
* As a shopper I can select the quantity of a product when adding to cart so that I can order more than one if I want to.
<img src="media/images/quantity.png">

As you can see, users can increase or decrease the amount of records of the same name they want in their basket. 

### **User Story 13**
* As a shopper I can view my bag before purchasing so that check what I have ordered and check final cost.

<img src="media/images/your_cart.png">

Users can view their total in the Order Summary page, which is the checkout url.

### **User Story 14**
* As a shopper I can change the quantity in my bag so that I can amend if I change my mind or am spending too much.
<img src="media/images/quantity.png">
Again, similar to a previous user story, this one is achieved on the basket page before the user clicks checkout so that they can make any final decisions based on their bag total. 

### **User Story 15**
*As a shopper I can enter payment information so that I can checkout quickly
<img src="media/images/payment.png">
Implementing Stripe into the site allows users to enter payment information quickly. 

### **User Story 16**
* As a shopper I can order safe in the knowledge that my personal and payment info is safe so that feel confident in providing that info.
<img src="media/images/confirmation_email.png">
The confirmation email that users receive once completing their order should provide the comfort required that the order has been made to a reputable company. 

### **User Story 17**
*As a shopper I can view and order confirmation so that I can be sure the order has been a success.
<img src="media/images/thanks_conf.png">
Once the order is placed, the user is sent to an order confirmation page.

### **User Story 18**
* As a shopper I can receive an email confirmation so that I have a copy for my records
<img src="media/images/confirmation_email.png">
The above image it is taken from an automated e-mail received once an order is placed and thus completing this user story. 

### **User Story 19**
* As an admin I can add a product so that I can add items as they become available

<img src="media/images/add_product.png">

The above image is taken from the admin panels 'products' page. This will allow site admin to add new products and fill out the required data to populate the information. 

### **User Story 20**

* As an admin I can edit/update a product so that I can change anything about the product I want to, such as price
<img src="media/images/product_info.png">

The above image shows that data can be edited and updated. 


### **User Story 21**

*As an admin I can delete a product so that I can remove items that are currently out of stock

<img src="media/images/delete_save.png">

In the above image you can see how as an admin they can delete a product if the item goes out of stock. 

<br>
<br>

### **Additional Testing**
* The site has been used by friends and family to try and find any errors. There are no known errors in this version that have been found that haven't been fixed during the development process.
* Throughout the process the developer has navigated through the site on a continual basis and no issues are currently noted. They have been fixed as the development has progressed and the majority of these I have documented in the bugs section of this file. 
* Google Chrome Developer tools has been used throughout to identify styling issues that impact upon display and UX. Dveloper tools was used to find the errors and amend.
* All links were tested multiple times during the development process and after deployment

### **Compatability Testing**

## **Languages & Technology Used** - Python.


### **Languages**
#### **Python**
#### **JavaScript**
#### **HTML5**
#### **CSS**

### **Technology and Validation**
#### **Stripe**

#### **PEP8 Validation**

[PEP8](http://pep8online.com/) was used to check for any errors. All of the code passes with no errors or warning present due to bad code. Example screen shots of some of the code are below:

This screen shows the top of the file and the code being accepted on Pep8 for Python code. All python code was tested using this process. I removed all genuine errors and there were a few 'line too long' warnings. Originally I left some of these in becasue they were long variable names rather than bad code. I was also of the opinion that, whilst I am aware of the 'line too long' item, it applied to a time when monitors were smaller and a max line limit of 80 was the accepted convention. Nowadays with bigger screens this is no longer the case, and longer lines are still readable/accepted. However, after discussion with my mentor I decided to break these lines down so that they fit with convention, even if I don't think it is aboslutely necessary all of the time.

<br>

#### **WC3 Validation**

The [WC3](https://validator.w3.org/nu/) validator was used to check for any errors in the HTML code. All code passes with all major errors removed. 
#### **CSS Validation**

#### **JS Hint Validation**



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

I would have loved to have completed this course as a full time student, like a lot of my colleagues are able to. Working full time and being a father to two children under 3 has meant that the amount of time that I have been abe to spend on it is significantly lower, yet I am still proud of what I have been able to do. When I look at the presentation of other submissions, it can be disheartening becasue I know that if I was able to put 40 hours a week into the course, and still get my weekends off I would have been able to maintain some more merit grades and maybe even a distinction or two. My mentor Chris Quin, who has been amazing to me, has made me see that the race is just against myself and nobody else. However, I work in the week and then my weekends are taken for the course, which has led to very little time off over the last year, which has been a struggle and my mental health has suffered and my marraige has been under additioal strain. Adding onto this my father having a heart attack and my 3 month old son being admitted to hospital just in the last few weeks has added to the strain. I think that CI should not be advertising this course as 12-15 hours per week, becasue for people with no coding background, it is certainly not. It is 20-25 hours just to keep up, and when you are working 40+ hours a week in full-time work, this is very hard to do. 
## **Credits**
My amazing wife who has managed our two children on her own a lot over this past year. Time I won;t get back but I am greatful for her and hopefully now I can get back to helping her and being a good father to my two amazing children.

My mentor Chris Quin, 


## **Acknowledgements**

