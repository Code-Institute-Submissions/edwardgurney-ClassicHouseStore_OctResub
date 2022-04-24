# Classic House Vinyl Store
### Developer: Edward Gurney
INSERT PICS OF SITE HERE
### You can view the live project here: [Classic House Vinyl Store](https://classic-house-store.herokuapp.com/)
<br>

## **Table of Contents**

## **Project 5 - Introduction**
This website is an e-commerce (business to consumer) site for a hard to find record store specialising in vinyl for classic house of various genres. 

The site is for anyone that loves house music, but more specifically for those that collect vinyl or those looking for particular records that aren't as available as they once were. The site will be light touch, in terms of its feel, as the product descriptions will be written by music lovers with a blog/personal feelings about the records (written by the store owner).

User experience has been hightened with the ability to click and listen to a slice of the track/record. This was a particular deign feature I wanted to implement from the start. 

When landing on the site, the user will be greeted with records so that they can start viewing and listening straight away, and can add to cart on the homepage of viewing the product details. They can purchase as a registered user or visitor and stripe payment functionality has been implemented.

CRUD functionality is employed using a database to store relevant data and various models have been created. 

An Agile methodolgy was used during the development process and this has been documented through the use of the projects tab in github reocrding issues and utlisation of kanban boards.
## **User Experience**

### *Project Goals*
Classic House Vinyl Store is a an e-commerce site where users can hunt down hard to find records and for any house lovers to purchase records for their DJ sets or for use at home. It will provide an easy to use site, where users can locate what they want easiliy, using filter and search, but also the ability to use browse the site. 

The site will allow users to register for an account and will incorporate Stripe functionality to allow single payment transaction at checkout.
### *Business Goals*

As a business owner the site needs to be pleasing and easy to use to encourage users to start listening to music quickly. This is to try and increase purchases on the site. Product descriptions with a persoanl touch is also important so that site users and new site users (maybe users that are just finding their way in the scene) can get an experts view on classic records. 

Giving customers the ability to listen to a section of the music, to check it is what they are looking for will also help to increase sales.

Features search as filter and search will allow users to hunt down what they are lookingn for quicker, and also allow them to filter their favourite genre of house music. 

### *Marketing*

In addition to the above, some further marketing strategies will be used to optimise the sites reach. Search Engine Optimization (SEO) has been considered throughtout development in an attempt to improve the search engine ranking of the site. To do this I perfromed an exercise where I identifed what I thought would be the keywords that people would use when searching for a site. I used these words in the development when coding, and added some in the keywords meta tag in the base template. 

There is also a site map that can be accessed from the homepage, and this is a way to improve a sites search engine ranking and allows search engine bot crawling.

When users sign up they need to provide an e-mail address and they can also sign up to a newsletter.

### *Site Owner Goals*<br>

### *First Time User Goals*<br>
- I want to be able to find certain records quickly via search and filter.
- I want to be able to find my way around the store easily, without there being a learning curve. It needs to be easy to use. 
- I want to be able to browse through the store easily, where I can just listen to music for when I'm not looking for anything in particular. 
- I want to be able to like/rate records so that I can share my views, and also see an overall rating of other site users opinions on the records. 
- I want to be able to register on the site and be able to log in.

### *Returning User Goals*
- I want records to be easily finadable, so that I can listen to the music again, or find them if I am returning to the site to purchaase.
- I want my basket/bag to keep what I have added to basket, so that if I don't purchase the first time, I can return to the site later and purchase. 
### *User Stories*
Below is an image of the original user stories that was performed at project initiation, these were what needed to be implemented for the project to be a success. In total there are 20 user stories. The second image below is the Agile tool used in Github during development, this was used to map the user stories to the project goals. During development there was an additional user story implemented, taking the toal to 21.

<details><summary>An image of the user stories during the project planning stage</summary>


<img src="media/user_stories.png">

</details>

<details><summary>This second image shows the Agile tool used during development</summary>

<img src="media/user_stories.png">

</details>

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

## **Database Schema**

During the planning stage, entity relationship diagrams were created to plan the models that would be required during development. In total, there were 5 models designed at this stage. These were User, Shipping, Product, Bag and Order models. 

These can be viewed below:

<img src="media/entity_relationship_diagram_2.png">

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

