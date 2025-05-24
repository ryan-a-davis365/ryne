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
  * ...**View individual product details** so that I can **identify the price, description, detailed reviews, and product image enabling me to compare how the product differs from other items.**
  * ...**View the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
  * ...**Leave a review** so that I can **share my opinion of a product and leave a star rating.**
  * ...**View reviews of a product** so that I can **see what other people think of a product.**
  * ...**Identify any promotions that are available** so that I can **take advantage of them and obtain the best value for money possible.**
  * ...**See clearly when something goes wrong on the site** so that I can **correct any errors and continue with my purchase.**
  * ... **See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
  * ...**Easily contact the store owner** so that I can **ask questions about the products or the site.**