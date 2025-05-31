# **RYNE**

RYNE is a fictional gym clothing store that was designed and implemented with Django, Python, HTML and CSS. It aims to provide an easy-to-use interface where customers can browse all items at once or sort into specified categories. The site offers search functionality. Once signed in, users can save an address to their profile for easy and convenient checkout.

The deployed site can be visited here: [RYNE](link to site)

![RYNE](am-i-respnsive-screenshot)

## **Table of Contents**

* [**Planning Phase**](#planning-phase)
  * [**Strategy**](#strategy)
    * [***Site Aims***](#site-aims)
    * [***Opportunities***](#opportunities)
    * [***Scope***](#scope)
    * [***Structure***](#structure)
      * [**User Stories:**](#user-stories)
        * [**EPIC 1 - Set up and Deployment:**](#epic-1---set-up-and-deployment)
        * [**EPIC 2 - Viewing and Navigation:**](#epic-2---viewing-and-navigation)
        * [**EPIC 3 - Sorting and Searching:**](#epic-3---sorting-and-searching)
        * [**EPIC 4 - Registration and User Accounts:**](#epic-4---registration-and-user-accounts)
        * [**EPIC 5 - Purchasing and Checkout:**](#epic-5---purchasing-and-checkout)
        * [**EPIC 6 - Admin and Store Management:**](#epic-6---admin-and-store-management)
        * [**EPIC 7 - Product Reviews:**](#epic-7---product-reviews)
        * [**EPIC 8 - Marketing:**](#epic-8---marketing)
    * [**Skeleton**](#skeleton)
      * [**Wireframes:**](#wireframes)
        * [***Home Page:***](#home-page)
        * [***Products Page:***](#products-page)
        * [***Product Details Page:***](#product-details-page)
        * [***Shopping Cart Page:***](#shopping-cart-page)
        * [***Checkout Page:***](#checkout-page)
        * [***User Profile Page:***](#user-profile-page)
        * [***Order Confirmation Page:***](#order-confirmation-page)
      * [**Database Schema**](#database-schema)
      * [**SEO considerations**](#seo-considerations)
        * [***Keywords***](#keywords)
        * [***Page Titles***](#page-titles)
        * [***Robots.txt and sitemap.xml***](#robotstxt-and-sitemapxml)
      * [**Content**](#content)
      * [**Surface**](#surface)
        * [***Colour Scheme***](#colour-scheme)
        * [***Typography***](#typography)
    * [**Agile Development Process**](#agile-development-process)
    * [**E-commerce Application Type**](#e-commerce-application-type)
    * [**Marketing Strategy**](#marketing-strategy)

# **Planning Phase**

## **Strategy**

### ***Site Aims***

The aim of the RYNE website is to provide a seamless, user-friendly platform for customers to explore and purchase high-performance gym apparel. It is designed to reflect the brand’s core values and purpose. The site focuses on delivering a smooth shopping experience through easy to follow navigation, responsive design, and secure checkout. Whether users are browsing new arrivals, learning about products, or completing a purchase, RYNE’s digital presence is built to inspire confidence and support fitness goals.

### ***Opportunities***

In the course of providing a fully functioning E-commerce platform, the following opportunities are available: -

Opportunity | Importance | Viability/Feasibility
---|---|---
Mailing list | 5 | 5
Account profile | 5 | 5
Product Filters/searching | 5 | 5
SEO language throughout | 5 | 5
stripe payments | 5 | 5
User feedback for actions taken | 5 | 5
Check out system | 5 | 5
Guest checkout completion | 5 | 5
User login/register | 5 | 5
RYNE blog | 1 | 5
Delivery information | 3 | 5
User Role permissions | 5 | 5
Product reviews | 5 | 3
Full CRUD functionality | 5 | 5
Order History | 5 | 5
Stock management system | 5 | 3 |
Contact form | 3 | 5
Social Media pages | 5 | 5
Special offers | 5 | 5
Password Recovery | 5 | 5
Email confirmation of order | 5 | 5
Related products | 1 | 1
Saved customer details on checkout | 5 | 5
Admin can add/remove products via the front end | 3 | 5
Multiple currencies | 5 | 1
Trustpilot reviews | 5 | 1
Terms and conditions | 3 | 5
Order Status | 2 | 5
Generate sales reports | 5 | 1
Ability to edit order until status set to processing | 1 | 5

Totals | 127 | 130


### ***Scope***

Due to the time given for this project and the required grade criteria, there will need to be further trade-offs in the design/development process. Using the agile methodology, I will review my progress weekly and add, adapt, or remove features as applicable to the project at the review portion after each sprint to ensure my website is delivered fully functional by the deadline: -

To avoid scope creep, I have used the MoSCoW method to divide the above opportunities into the below categories aiding me to prioritize and ensure that I can achieve my goal of a fully functioning MVP by the deadline: -


* To create a minimum functional E-commerce site, UX efforts **must** address these opportunities: -
  * Full CRUD Functionality.
  * User login/register.
  * Checkout system.
  * Account profile.
  * Mailing list.
  * Product Filters/searching.
  * Stripe payments.
  * SEO language throughout.
  * Guest checkout completion.
  * User Role permissions.
  * Order History.
  * Social Media page.
  * Special offers.
  * Password Recovery.
  * Email confirmation of order.
  * User feedback for actions taken.
  * Saved customer details on checkout.


* To enhance the customer experience and increase the sites functionality, UX efforts **should** address these opportunities: -
  * Product reviews.
  * Stock management system.
  * Contact form.
  * Admin can add/remove products via the front end.
  * Delivery information.
  * Terms and conditions.
  * Order Status.

* To increase the sites popularity and customer base, UX efforts **could** address these opportunities: -
  * RYNE Blog.
  * Related products
  * Ability to edit order until status set to processing.

* As they are so far out of the scope of this project, UX efforts **will not** address these opportunities: -
  * Trustpilot reviews.
  * Multiple currencies.
  * Generate sales reports.

### ***Structure***

Using the above as a guide, I have created a flow diagram to help me visualize how the user will navigate through the site. During the agile process, minor tweaks may occur to this pre-planned user journey, but the overall structure will more or less remain the same.

![Flowchart](flow-chat-screenshot)

#### **User Stories:**

To assist the AGILE process, I have created several user stories to help me plan and implement the project. These will help me prioritize the features and functionality of the site and ensure that I am delivering a completed project by the deadline. The below user stories are divided into EPICs and will be reviewed and updated after each sprint.

##### **EPIC 1 - Set up and Deployment:**

This epic will be tasks rather than user stories since they will be aimed at me as the developer rather than the user. The below tasks will be completed before the first sprint and will be used to set up the project and ensure that it is deployed to Heroku with the AWS S3 bucket for static files. Some of these were taken/adapted from the Code Institute's sample project, Boutique ado.

* As a **Developer** I can...
  * ...**Create a Git hub repository** so that I can **Store my project files online.**
  * ...**Create a virtual environment on my local machine** so that I can **avoid polluting my machine on a global level.**
  * ...**Install Django and required libraries** so that I can **work with a postgress Database and cloudbased images from my local development IDE.**
  * ...**Set up my local coding environment** so that I can **develop on my local machine and deploy securely without revealing sensitive information.**
  * ...**Create a Heroku app** so that I can **link to the a virtually hosted Postgres database for the deployed site.**
  * ...**Create a new AWS S3 bucket** so that I can **store static files and images securely.**

The only user story in this Epic is related to the initial deployment; this is a user story rather than a task because it directly offers value to the user as opposed to being tasks required to create the project: -

* As a **User**, I can **access a live url** so that I can **use the site on any device**.

##### **EPIC 2 - Viewing and Navigation:**

* As a **Shopper** I want to be able to...
  * ...**Clearly identity the sites purpose upon visiting** so that I can **determine if the site is what I am looking for.**
  * ...**View a list of products** so that I can **select some to purchase.**
  * ...**View individual product details** so that I can **identify the price, description, product rating, product image and available sizes.**
  * ...**Easily view the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
  * ...**Leave a review** so that I can **share my opinion of a product and leave a star rating.**
  * ...**View reviews of a product** so that I can **see what other people think of a product.**
  * ...**Quickly identify deals, clearance items and special offers** so that I can **take advantage of special savings on products I'd like to purchase.**
  * ...**See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
  * ...**Easily contact the store owner** so that I can **ask questions about the products or the site.**

##### **EPIC 3 - Sorting and Searching:**

* As a **Shopper** I want to be able to...
  * ...**Sort the list of available products** so that I can **easily identify the best rated, best priced and categorically sorted products.**
  * ...**Search for a product by name or description** so that I can **find a specific product I'd like to purchase.**
  * ...**Sort a specific category of product** so that I can **find the best-priced or best-rated product in a specific category, or sort the products in that category by name.**
  * ...**Easily see what I've searched for and the number of results** so that I can **quickly decide whether the product I want is available.**

##### **EPIC 4 - Registration and User Accounts:**

* As a **Site User** I want to be able to...
  * ...**Easily register for an account** so that I can **save my personal details and view my order history online.**
  * ...**Easily login or logout** so that I can **access my personal account information and protect it from unauthorized viewing on shared devices.**
  * ...**Save my personal details to my profile from the checkout page** so that I **don’t have to enter them every time I make a purchase.**
  * ...**Have a personalized user profile** so that I can **view my personal order history and order confirmations, save my payment information and update information.**
  * ...**Easily recover my password in case I forget it** so that I can **recover access to my account.**
  * ...**Receive an email confirmation after registering** so that I can **verify that my account registration was successful.**
  
##### **EPIC 5 - Purchasing and Checkout:**

* As a **Shopper** I want to be able to...
  * ...**Select a quantity of a product** so that I can **buy the required amount of the product.**
  * ...**View items in my bag to be purchased** so that I can **identify the total cost of my purchase and all items I will recieve.**
  * ...**Adjust the quantity of individual items in my bag** so that I can **easily make changes to my purchase before checkout.**
  * ...**Easily enter my payment information** so that I can **check out quickly and with no hassles.**
  * ...**View an order confirmation after checkout** so that I can **verify that I haven't made any mistakes.**
  * ...**Receive an email confirmation after checking out** so that I can **keep the confirmation of what I've purchased for my records.**
  * ...**View my order history** so that I can **see the orders I have made previously.**
  * ...**Access the checkout page** so that I can **review my order whilst entering my payment/shipping details.**
  * ...**Feel my personal and payment information is safe and secure** so that I can **confidently provide the needed information to make a purchase.**

##### **EPIC 6 - Admin and Store Management:**

* As a **Store Owner** I want to be able to...
  * ...**Add a product** so that I can **add new items to my store.**
  * ...**Edit/update a product** so that I can **change product prices, descriptions, images, and other product criteria.**
  * ...**Delete a product** so that I can **remove items that are no longer for sale.**
  * ...**Manually manage the stock levels** so that I can **input received purchase orders and ensure that the stock levels are accurate in case of discrepancies or damages.**

##### **EPIC 7 - Product Reviews:**

* As a **Shopper** I want to be able to...
  * ...**Leave a review** so that I can **share my opinion of a product and leave a star rating.**
  * ...**View reviews of a product** so that I can **see what other people think of a product.**
  * ...**Edit my reviews of a product** so that I can **update my public opinion should it ever change.**
  * ...**Delete my reviews of a product** so that I can **remove previous reviews should I see fit.**.


##### **EPIC 8 - Marketing:**

* As a **business owner** I want to be able to...
  * ...**Set up a social media page** so that I can **promote my business and products to the global market.**
  * ...**Increase my search engine ranking** so that I can **increase the number of visitors to my site.**

### **Skeleton**

#### **Wireframes:**

Wireframes were created using Balsamiq wireframes to visualize how the site would look and function. Included below are the wireframes used to plan the site's layout.

##### ***Home Page:***

[Home page wireframe](home-page-pic)

##### ***Products Page:***

[Products page wireframe](product-page-pic)

##### ***Product Details Page:***

[Product details page wireframe](product-details-page-pic)

##### ***Checkout Page:***

[Checkout page wireframe](checkout-page-pic)

##### ***User Profile Page:***

[User profile page wireframe](user-page-pic)

### **SEO considerations**

#### ***Keywords***

During the creation of my website I added as many different phrases and keywords to my meta tags to assist in the SEO of the site. This was so my website would be easily searchable and that when users were looking for the products that my website provides they would be taken to my website.

#### ***Page Titles***

Each page shows an extra title after the store name to assist help with SEO.

#### ***Robots.txt and sitemap.xml***

Sitemap and robots.txt files have been added to the site's root to help with SEO.

### ***Content***

The site did not have too many opportunities for content in terms of paragraphs and text. A lot of the keywords are products themselves, so i have tried to use the heading tages and other semantic tags correctly so that the quality of my site's search rating is as high as possible.

### **Surface**

Once the project was planned I then had to decide on a theme. I wanted to keep it simple but have some colour to help it stand out. I also wanted to keep it clean and easy to navigate. I have used a lot of white space and a simple colour scheme to help with this.

#### **Colour Scheme**

Black and white feature heavily throughout the site. However, I added colour to help the content pop and to help with the branding. After researching various options for this project, I opted for the colour scheme below:

![Colour Palette](colour-palette-pic)

#### ***Typography***

I done some research on fonts to decide which one I wanted to use for this project, in the end I decided on:

* [Oswald](https://fonts.google.com/specimen/Oswald) - This font is used throughout the entire websites due to its clean and easy to read look, it also stands out well.

## **Agile Development Process**

## **E-commerce Application Type**

As already mentioned, RYNE is a B2C e-commerce application. Selling directly to consumers means that the site is designed to sell quickly, on impulse and in smaller quantities. Due to this being a B2C website only, a large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively.

## **Marketing Strategy**

As RYNE is a start-up business, the budget for marketing is limited compared to other businesses. However, there are several ways that RYNE can market itself to help increase sales and brand awareness. Using Facebook to get out content and drive traffic is the first and most straightforward. The use of paid ads allows the business to target specific demographics and increase brand awareness. The use of social media is also a great way to get feedback from customers and to help with customer service. There is an image of the Facebook page in the features section below and a link to the page [here](facebook-link).

The second is the use of google ads which are a great way to increase brand awareness and help with SEO. The use of google ads can also help with the use of long-tail keywords and help with the ranking of the site.

The third is the use of influencers. Influencers are a great way to increase brand awareness. Free samples could be sent to popular athletes, bodybuilders, strongmen etc. on youtube in exchange for a mention/hashtag/link in the description. Further helps raise brand awareness because the video could be posted on Facebook and the influencer tagged in the post, which with the help of the algorithm used at Facebook, would help bring an organic audience to the Facebook page and, hopefully, the store.


