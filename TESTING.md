# **Manual Testing**

## **Table of Contents**

* [**Manual Testing**](#manual-testing)
    * [**Bugs and Fixes During the Development Process**](#bugs-and-fixes-during-the-development-process)
    * [**Testing(post development phase)**](#testingpost-development-phase)
        * [**Validation**](#validation)
            * [**HTML**](#html)
            * [**CSS**](#css)
            * [**JavaScript**](#javascript)
            * [**Python - PEP8 - using pycodestyle**](#python---pep8---using-pycodestyle)
        * [**Lighthouse Scores**](#lighthouse-scores)

## **Bugs and Fixes During the Development Process**

Below is a list of bugs and fixes found while creating a feature:

* Issue - Was not receiving emails for signup, successful order etc.
* Cause - Did not have the correct email for the "EMAIL_HOST_USER" in the config variables on heroku.
* Solution - Changed the email to the correct one to send out emails.

* Issue - Product images would not load correctly on the site, when uploaded an image for a new product it would also not displaying.
* Cause - I had a typo in my config variables for "AWS_SECRET_ACCESS_KEY", i had 3 C's instead of 2.
* Solution - Corrected the typ with the correct spelling.

* Issue - On my products page the Category icon didnt display properly and would send you to a products page with "Category=None" instead of the correct categories.
* Cause - I was using "models.ManyToManyField" so products could have multiple categories and i didnt adjust the rest of the code to accomodate this.
* Solution - I had to adjust code in "products.html" so the code would loop through the categories.

* Issue - My custom 404.html page was not displaying when it needed to.
* Cause - I was trying to figure it out looking deeper than i needed, it was displaying a "Internal Server Error (500)" because i did not have a favicon that was overriding the 404 page from displaying.
* Solution - Added a custom favicon to the site and it was resolve my 404.html page from not displaying.

* Issue - Order confirmation email was not sending.
* Cause - I accidently changed the wrong email.txt file when i was trying to setup email verification and this lead to an error being displaying because i was using {{ order.username }} instead of {{ order.full_name }}.
* Solution - I changed the email.txt file back to the original.

* Issue -  Delivery price was incorrect.
* Cause - I was using "STANDARD_DELIVERY_PERCENTAGE = 10" in my settings.py which made the delivery cost super high.
* Solution - Changed my settings.py to "STANDARD_DELIVERY_CHARGE = 3.99" and adjusted models.py and contexts.py to display the correct delivery price at all times.

* Issue - Delivery price was constantly being displaying in the shopping bags even when items had not been added
* Cause - I was using the wrong code in base.html {% if grand_total %}
* Solution - Adjusted {% if grand_total %} to {% if product_count > 0 %}

## **Testing(post development phase)**

### **Validation**

#### **[HTML](https://validator.w3.org)**

No errors were found within my HTML.

![HTML Validation](docs/images/validation/html-validator.png)

#### **[CSS](https://jigsaw.w3.org/css-validator/)**

No errors were found within my CSS.

![CSS validation](docs/images/validation/css-validator.png)

#### **[JavaScript](https://jshint.com/)**

Checking my static JS files with jshint, there were no issues.

![Jshint](docs/images/validation/js-validator-1.png)

![Jshint](docs/images/validation/js-validator-2.png)

#### **Python - PEP8 - using pycodestyle**

I used pycodestyle to check my python code. pycodestyle is a command line installed with pip. I ran the command "pycodestyle --first <-appname->". This command checks all files in the directories and subdirectories of the app and returns the first error found. With this and cross-checking in the terminal of VScode, I found the only errors were some lines being too long(E501) and expecting 2 blank lines(E302).

### **Lighthouse Scores**

#### **Home page**

##### **Desktop**

![lighthouse home](docs/images/lighthouse/home-desktop.png)

##### **Mobile**

![lighthouse home mobile](docs/images/lighthouse/home-mobile.png)

#### **Products page**

##### **Desktop**

![lighthouse products page](docs/images/lighthouse/products-desktop.png)

##### **Mobile**

![lighthouse products page mobile](docs/images/lighthouse/products-mobile.png)

#### **Product Details Page**

##### **Desktop**

![lighthouse details page](docs/images/lighthouse/product-detail-desktop.png)

##### **Mobile**

![lighthouse details page mobile](docs/images/lighthouse/product-detail-mobile.png)

#### **Contact us page**

##### **Desktop**

![lighthouse contact page](docs/images/lighthouse/contact-desktop.png)

##### **Mobile**

![lighthouse contact page mobile](docs/images/lighthouse/contact-mobile.png)

#### **Shopping Cart page**

##### **Desktop**

![lighthouse cart page](docs/images/lighthouse/cart-desktop.png)

##### **Mobile**

![lighthouse cart page mobile](docs/images/lighthouse/cart-mobile.png)

### **Reviewing the Lighthouse Scores**

I noticed the Accessibility score is a bit low, a big part of this is cache date, i tried to fix this by changing the meta data on my files in S3 but the cache data would not update for some reason and due to the time i had to finish this i decided to leave it. If i had more time i would of looked into this further. The performance score was generally a little lower on mobiles however testing from several mobile devices the site was responsive and responded well. I also note that any path disallowed in the robots.txt had its SEO score suffer with the robots.txt being specified as a cause.

### **Manual Testing of User Stories**

For the following, I will skip the type of user, i.e. "As a shopper, I can…” and only list the latter part of the story as a heading.

#### **EPIC 1 - Set up and Deployment:**

Most of this epic were tasks for the development phase; therefore, the testing is the working of the overall site. Below is the one story that tested all tasks as one.

|passed | **Access a live url** so that I can **use the site on any device**.
|:---:|:---|
|&check;| Can access the site via the deployed URL on the desktop.
|&check;| Can access the site via the deployed URL on mobile.
|&check;| Can access the site via the deployed URL on a tablet.
|&check;| All images and styles are tacked and as expected.

#### **EPIC 2 - Viewing and Navigation:**

|passed | .**Clearly identity the sites purpose upon visiting** so that I can **determine if the site is what I am looking for.**
|:---:|:---|
|&check;| The site has a clear purpose and is easy to navigate.

|passed | **View a list of products** so that I can **select some to purchase.**
|:---:|:---|
|&check;| The site has a list of products.
|&check;| The list of products is paginated.
|&check;| The product list is ordered by default by ID.
|&check;| The list of products can be ordered by name ascending and descending.
|&check;| The list of products can be ordered by price ascending and descending.
|&check;| The list of products can be ordered by rating ascending and descending.
|&check;| The list of products can be filtered to show only those with an active sale.
|&check;| The list of products shows stock status, i.e., in stock/out of stock.
|&check;| Add to cart button works as expected on all products and product details pages.
|&check;| User cannot add more items to their cart that are in stock.
|&check;| When an item is out of stock, the add to cart button is disabled.

|passed | **View individual product details** so that I can **identify the price, description, detailed reviews, and product image enabling me to compare how the product differs from other items.**
|:---:|:---|
|&check;| The site has a product details page.
|&check;| The product details page shows the product image.
|&check;| The product details page shows the product name.
|&check;| The product details page shows the product price.
|&check;| The product details page shows the sale price if the item has a sale.
|&check;| The product details page shows the product description.
|&check;| The product details page shows the product rating.
|&check;| The product details page shows the product reviews.
|&check;| The product details page shows the review form if there are no reviews already.
|&check;| The product details page shows the product quantity selector.
|&check;| The product details page shows the product add to cart button.

|passed | **View the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
|:---:|:---|
|&check;| The site has a cart page.
|&check;| The cart page/preview shows the product image.
|&check;| The cart page/preview shows the product name.
|&check;| The cart page/preview shows the product price.
|&check;| The cart page/preview shows the current quantity in the cart.
|&check;| Cart preview shows when the item is added from any page.
|&check;| The cart page shows the product quantity selector, and the user can update their order quantity.
|&check;| The cart page/preview shows the cart total.
|&check;| The cart page/preview shows the amount left to spend to get free delivery.
|&check;| The cart page shows the delivery cost and grand total.
|&check;| The cart page allows the user to completely remove an item from their cart and updates the cart total.
|&check;| When the quantity is updated in the user's cart, the cart total updates accurately.

|passed | **Leave a review** so that I can **share my opinion of a product and leave a star rating.**
|:---:|:---|
|&check;| The site has a review form.
|&check;| The review form has a title field.
|&check;| The review form has a rating field.
|&check;| The review form has a body field.
|&check;| When a review is submitted, the review is added to the product detail page.
|&check;| User cannot enter a value greater than 5 for the rating field.
|&check;| User cannot enter a value less than 1 for the rating field.
|&check;| User cannot submit a review without a title.
|&check;| User cannot submit a review without a rating.
|&check;| Overall rating is calculated and displayed on the product detail page/product card.
|&check;| Overall rating is adjusted when a review is deleted or edited.
|&check;| Author of the review can edit their review.
|&check;| Author of the review can delete their review.
|&check;| Author of the review can not edit or delete another user's review.
|&check;| Success message is displayed when a review is submitted.

|passed | **View reviews of a product** so that I can **see what other people think of a product.**
|:---:|:---|
|&check;| The site has a review section on the product detail page.
|&check;| The review section shows the review title.
|&check;| The review heading indicates the review rating.
|&check;| The review heading previews the review body.
|&check;| The review heading shows the review author.
|&check;| The review heading indicates the review date.
|&check;| The review edit/delete buttons only show to the author and super users.
|&check;| If reviews, there is a button above for the user to add a review.

|passed | **Quickly identify deals, clearance items and special offers** so that I can **take advantage of special savings on products I'd like to purchase.**
|:---:|:---|
|&check;| The site has a promotions page.
|&check;| The promotions page shows only active sales items.

|passed | * ... **See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
|:---:|:---|
|&check;| The site has a pleasant colour scheme.
|&check; | The site has a pleasing font scheme.
|&check; | The site has a pleasing layout.
|&check; | The site has pleasant navigation.
|&check; | The site has a pleasant footer.
|&check; | The site has a nice header.
|&check; | The site has an enjoyable product card.
|&check; | The site has a pleasant product detail page.
|&check; | The site has a nice cart page.
|&check; | The site has a nice checkout page.
|&check; | The site has a pleasant promotions page.
|&check; | Everything is aligned and spaced correctly.

|passed | **Easily contact the store owner** so that I can **ask questions about the products or the site.**
|:---:|:---|
|&check;| The site has a contact page.
|&check;| Contact form cannot be submitted with required fields blank.
|&check;| Contact form cannot be presented with an invalid email address.
|&check;| Contact form submits a message to the database.
|&check;| Message can be read in the admin panel.
|&check;| Success message is shown to the user when a message is submitted.
|&check;| Message can be updated as done.
|&check;| Pending reply is automatically ticked and can be un-ticked to indicate the message is complete
|&check;| Message can be deleted.

#### **EPIC 3 - Sorting and Searching:**

|passed | **Sort the list of available products** so that I can **easily identify the best rated, best priced and categorically sorted products.**
|:---:|:---|
|&check;| Products can be sorted by name in ascending order.
|&check;| Products can be sorted by name in descending order.
|&check;| Products can be sorted by price in ascending order.
|&check;| Products can be sorted by price in descending order.
|&check;| Products can be sorted by rating in ascending order.
|&check;| Products can be sorted by rating in descending order.

|passed | **Search for a product by name or description** so that I can **find a specific product I'd like to purchase.**
|:---:|:---|
|&check;| Search bar is visible on all pages.
|&check;| Search returns results based on the search term.
|&check;| Search query matches product name and description.
|&check;| search terms are displayed above the search results.
|&check;| Number of products returned is displayed above the search results.

|passed | **Sort a specific category of product** so that I can **find the best-priced or best-rated product in a specific category, or sort the products in that category by name.**
|:---:|:---|
|&check;| Products can be filtered by category via the navbar links.
|&check;| Products can be filtered by sub-category via the navbar links.

|passed | **Easily see what I've searched for and the number of results** so that I can **quickly decide whether the product I want is available.**
|:---:|:---|
|&check;| Search returns results based on the search term.
|&check;| Search query matches product name and description.
|&check;| search terms are displayed above the search results.
|&check;| Number of products returned is displayed above the search results.

#### **EPIC 4 - Registration and User Accounts:**

|passed | **Easily register for an account** so that I can **save my personal details and view my order history online.**
|:---:|:---|
|&check;| The site has a registration page.
|&check;| Users can not register with an email address that is already in use.
|&check;| Users can successfully register for the site
|&check;| Users can not register with a username that is already in use.
|&check;| Users can not register with a password similar to their user name.
|&check;| Users can not register with a password similar to their email address.
|&check;| Users can not register with a too short password.
|&check;| Errors are displayed to the user if any of the above are attempted.
|&check;| Success message is displayed to the user if registration is successful.
|&check;| User sees message to verify their email.
|&check;| Users can not log in until they have verified their email.
|&check;| Verification email is sent to the user.
|&check;| Verification email contains a link to confirm the user's email.
|&check;| Once verified, users, can log in with their username or email.
|&check;| Users are redirected to the login in page once the email is verified.

|passed | **Easily login or logout** so that I can **access my personal account information and protect it from unauthorized viewing on shared devices.**
|:---:|:---|
|&check;| Log in/out options are visible on all pages under the account dropdown.
|&check;| Once logged out, personal information is no longer visible.
|&check;| Once logged in, the account options change to reveal a profile link.
|&check;| Once logged in/out, the user is redirected to the home page.
|&check;| User receives a success message when they log in/out.

|passed | ...**Save my personal details to my profile from the checkout page** so that I **don’t have to enter them every time I make a purchase.**
|:---:|:---|
|&check;| The site has a profile page.
|&check;| The profile page has a form to update the user's details.
|&check;| Checkout form takes the information available in the profile for the checkout process
|&check;| Details from checkout save if save info box checked
|&check;| Details from checkout do not save if the save info box is not checked
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Have a personalized user profile** so that I can **view my personal order history and order confirmations, save my payment information and update information.**
|:---:|:---|
|&check;| User can update their details on the profile page.
|&check;| Appropriate error messages are shown if the user enters invalid information.
|&check;| Success message is displayed if the user updates their details successfully.
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Easily recover my password in case I forget it** so that I can **recover access to my account.**
|:---:|:---|
|&check;| The site has a password reset page.
|&check;| The password reset page has a form to enter the user's email address.
|&check;| Email is sent with password reset token.
|&check;| Link in the email takes the user to the password reset page.
|&check;| Password reset page has a form to enter the new password.
|&check;| User gets a success message once the password has been reset
|&check;| Users can now log in with their new password.

|passed | **Receive an email confirmation after registering** so that I can **verify that my account registration was successful.**
|:---:|:---|
|&check;| Email sent upon registration asking for the user to verify their email address.

#### **EPIC 5 - Purchasing and Checkout:**

|passed | **Select a quantity of a product** so that I can **buy the required amount of the product.**
|:---:|:---|
|&check;| Quantity can be selected on the product page.
|&check;| Quantity can be selected on the product detail page.
|&check;| User cannot set the quantity selector to more than the in-stock level
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to the in-stock level
|&check;| User can set the quantity selector to 1
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.
|&check;| User receives a message if an item is added to the cart.

|passed | **View items in my bag to be purchased** so that I can **identify the total cost of my purchase and all items I will recieve.**
|:---:|:---|
|&check;| The site has a shopping cart page.
|&check;| The shopping cart page has a list of all the items in the user's cart.
|&check;| The shopping cart page has a total price for all the user cart items.
|&check;| The shopping cart page has a button to proceed to checkout.
|&check;| The shopping cart page has a button to remove items from the cart.

|passed | **Adjust the quantity of individual items in my bag** so that I can **easily make changes to my purchase before checkout.**
|:---:|:---|
|&check;| The quantity of each item in the cart can be changed and updated from the cart page.
|&check;| Total recalculates each time the quantity is adjusted.
|&check;| User is shown a success/error message when the state changes in the cart.
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to 1.
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.

|passed | **Easily enter my payment information** so that I can **check out quickly and with no hassles.**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the user's payment details.
|&check;| The checkout page has a form to enter the user's shipping details.
|&check;| Payments are handled by Stripe.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return the user to the shopping cart.
|&check;| The checkout page has a button to save the user's details for future use.
|&check;| If checked, the details from the checkout form are saved to the user's profile.
|&check;| If it exists, the users saved details are pre-filled in the checkout form.
|&check;| If the user has saved details, the checkbox is unchecked by default.

|passed | **View an order confirmation after checkout** so that I can **verify that I haven't made any mistakes.**
|:---:|:---|
|&check;| The site has a checkout success page.
|&check;| The checkout success page has a message to confirm the order was successful.
|&check;| The checkout success page has a button to return to the home page.|
|&check;| The checkout success page has a button to take the user to the special offers page.
|&check;| Email is sent to the user confirming the order.
|&check;| Order is available to the customer who made the order in their order history page.
|&check;| Checkout success page for an order made by a registered user can only be seen by that user from the profile.
|&check;| Once an order is confirmed on screen, the order confirmation can only be revisited from a registered user's profile/non-registered users cannot revisit the checkout success page.

|passed | **Receive an email confirmation after checking out** so that I can **keep the confirmation of what I've purchased for my records.**
|:---:|:---|
|&check;| Email is sent to the user confirming the order.
|&check;| Email contains the order number.
|&check;| Email has the order total.
|&check;| Email includes the order date.
|&check;| Email contains the delivery address.
|&check;| Email includes the delivery cost.

|passed | **View my order history** so that I can **see the orders I have made previously.**
|:---:|:---|
|&check;| The site has an order history page for registered users.
|&check;| The order history page lists all the orders made by the user.
|&check;| The order history page has a link to view the order details.
|&check;| The order history page has a link to return to their profile page.
|&check;| The order history page can only be accessed by the user who made the order.
|&check;| Unregistered users cannot access their previous order confirmation.
|&check;| Appropriate error message is shown if a user tries to access an order confirmation that is not theirs.
|&check;| Appropriate error message is displayed if an unregistered user tries to get back to their order confirmation using a URL.

|passed | **Access the checkout page** so that I can **review my order whilst entering my payment/shipping details**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the user's payment details.
|&check;| The checkout page has a form to enter the user shipping details.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return it to the shopping cart.
|&check;| The checkout page has a button to save the user's details for future use.
|&check;| If checked, the details from the checkout form are saved to the user's profile.
|&check;| If it exists, the users saved details are pre-filled in the checkout form.
|&check;| Saved points the checkbox is unchecked by default.

|passed | **Feel my personal and payment information is safe and secure** so that I can **confidently provide the needed information to make a purchase.**
|:---:|:---|
|&check;| Stripe payment system is used.
|&check;| Stripe payment system is PCI compliant.

#### **EPIC 6 - Admin and Store Management:**

|passed | **Add a product** so that I can **add new items to my store.**
|:---:|:---|
|&check;| Product can be added via the admin panel and front end and is visible in the store front end.
|&check;| Newly added items had full functionality of pre-existing items.

|passed | **Edit/update a product** so that I can **change product prices, descriptions, images, and other product criteria.**
|:---:|:---|
|&check;| Product can be edited via the admin panel and is visible in the store front end.
|&check;| Quick edits can only be made from the front end by super users.

|passed | **Delete a product** so that I can **remove items that are no longer for sale.**
|:---:|:---|
|&check;| Product can be deleted via the admin panel and is no longer visible in the store front end.
|&check;| Quick delete can only be made from the front end by super users.
|&check;| Product cannot be deleted by non-superuser using the URL.

#### **EPIC 7 - Product Reviews:**

|passed | **Leave a review** so that I can **share my opinion of a product and leave a rating.**
|:---:|:---|
|&check;| The site has a review form.
|&check;| When there are reviews, they are displayed in an accordion with all relevant details visible.
|&check;| When there are reviews, there is a button to add a review.
|&check;| The leave review button takes the user to the review form page with the correct product name in the title and image displayed.
|&check;| The review form has a field to enter the review title, rating, and text.
|&check;| The review form has a button to submit the review.
|&check;| Rating cannot be above five or below one.
|&check;| Rating is a number field.
|&check;| Overall rating is re-calculated when a review is added.

|passed | **View reviews of a product** so that I can **see what other people think of a product.**
|:---:|:---|
|&check;| Once successfully submitted, the review is visible on the product details page.
|&check;| Author's name is in the accordion item heading.
|&check;| Review title is in the accordion item heading.
|&check;| Review text is previewed in the body of the accordion item.

|passed | **Edit my reviews of a product** so that I can **update my public opinion should it ever change**
|:---:|:---|  
|&check;| Review cannot be edited by a user who did not create the review (unless superuser) even by using the URL.  
|&check;| Edit review for is pre-populated with the review details.  
|&check;| A superuser can edit all reviews.  
|&check;| All reviews can be edited by the user who created the review.  
|&check;| Overall rating is re-calculated when a review is edited.  

|passed | **Delete my reviews of a product** so that I can **remove previous reviews should I see fit**
|:---:|:---|
|&check;| Review cannot be deleted by a user who did not create the review (unless superuser) even by using the URL.
|&check;| A superuser can delete all reviews.
|&check;| All reviews can be deleted by the user who created the review.
|&check;| Overall rating is re-calculated when a review is deleted.

#### **EPIC 8 - Marketing:**

|passed | **Set up a social media page** so that I can **promote my business and products to the global market.**
|:---:|:---|
|&check;| Facebook page is set up.
|&check;| Facebook page is linked on the site.
|&check;| Facebook page links have correct rel attributes.

|passed | .**Increase my search engine ranking** so that I can **increase the number of visitors to my site.**
|:---:|:---|
|&check;| Each page has a meta description.
|&check;| Each page has a meta title.
|&check;| Each page has meta keywords.
|&check;| Site map done
|&check;| Robots.txt done

|passed | .**Setup a newsletter signup** so that I can **inform the customers with news on products**
|:---:|:---|
|&check;| The site has a newsletter signup page.
|&check;| Newsletter form cannot be submitted with required fields blank.
|&check;| Newsletter form cannot be presented with an invalid email address.
|&check;| Newsletter form submits a message to the database notifying superusers they have signed up for Newsletters.
|&check;| Success message is shown to the user when they have signed up.


[Back to Readme](README.md)