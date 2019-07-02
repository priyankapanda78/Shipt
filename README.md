# Shipt Assignment
**1. Navigate to www.shipt.com. Choose a feature of the site and write a description or test
case to describe how to test the feature.**

**Answer**:

**Feature: StoreView based on zip code**

**Description**:User should be able to see the stores name which have shipt service based on the delivery address selected.

**Edge Case**: User should not be able to add an address to its address book where shipt service is unavailable(eg:Wyoming State).

**High Level Scenarios:**

1. Verify that a user is able to see the store names that have shipt service based on the delivery address selected.

2. Verify that the products are displayed after the store selection.

3. Verify that after the user changes the delivery address from dropdown, the store selection changes based on the shipt service availability. 

4. Verify that the user is not able to save an address where shipt service is unavailable.

5. Validate the error message is thrown when a user tries to save an address where shipt service is unavailable.

**Q2. Locate one bug or bad workflow within the app.**

**a. Explain the behavior you are seeing**

**Answer**
Defect#1:
This test scenario covers Favorites feature in the Shipt app. Creating a Favorites group allows you to add products from the selected store. These Favorites products can be added to cart and checked out as well. Upon, switching the store Favorites products added from another store should not be eligible for check out. The app doesn't exhibit this behavior consistently.

**b. Include any useful errors or screenshots**

**Answer**
Attached the screen recording video for this workflow in the mail.

**c. Explain why and how it needs to be corrected**

**Answer**
This is a defect as the user is able to click on checkout and select a delivery date for this scenario. And in the final page the error thrown is ‘There was an error in calculating total’. The error message does not accurately reflect the actual error blocking the user from checkout. It creates confusion and bad experience for customers. 
To correct this the items should be in unavailable status from Store 2 when store 1 is selected for Favorites section. And it should not allow the user to add the items in cart from Store 2. This synchronization in Favorites section will result in a good experience for users.

**d. What are the steps you would take to report the issue?**

**Answer**
Steps taken to report the issue.
* Defect should be raised in JIRA (or any internal defect tracking system) with appropriate screenshots and steps to reproduce this defect like below:

1. Login to shipt.com
2. Click on the Favorites icon and create a group called test 3 for Store 1.
3. Add products to this Favorites group (test 3) for Store 1.
4. Products should be in available status from Store 1.
5. Select a new store as Store 2 from the home page.
6. Repeat the steps 2 and step 3.
7. Products should be in available status from Store 2 and products should be in unavailable status from Store 1.
8. Select Store 1 again from homepage and click on Favorites section.
9. Products from Store 2 should be in unavailable status instead of available status as seen on the app.
10. The user should not be able to add these products to the cart and select a delivery time.
Defect is raised with its priority, severity and assigned to the Development Team based on the authorization(or contact Test Lead or Program Manager).

* The defect should be mapped with the requirements serial number for tracking purposes.

* The test cases should be in Failed status and associated with the defect number.

* Notification email should be sent across the team(Development, Testing, Program Manager, Product Manager) to avoid duplication of the defect and to follow up with Dev Team for the status of defects.

**e. What priority would you give this bug (Scale of 1-5, 1 being highest) and why?**

**Answer**

The defect should be raised with priority 2 depending upon the requirements critical condition. As this defect currently is not blocking the user to shipt app and also there is a turn around to operate the app.

**Q3. What are the possible reasons for the following defect? How would you go about
debugging the problem and gathering more information?
On a web application, a user adds a phone number to their account. The user
then changes the phone number. Upon trying to re-enter the first phone number,
the user is allowed to click Save, and it seems to work, but the saved number
remains the second number rather than updating to the more recently entered
number. A page refresh does not change the result**

**Answer**

This might be a case that any update to an account could be a new insert query with phone number being a unique constraint. Suppose, thats the case so it will allow the user to save the same number on the client side which doesn't have any validation check but will fail in the databse because that number already exists.

The way to solve it can be using update scripts in the database than multiple inserts and having an audit table to see all the updates happening or else have a validation check in the client side where it will go check the databse first if the number exists and if not, it will update the phone number with a successful message.

**SQL Assignements:**

1. SELECT * FROM INTERVIEW.STORES WHERE ALLOWED_ALCOHOL = TRUE;

2. SELECT SP.PRICE,P.NAME FROM INTERVIEW.PRODUCTS P JOIN INTERVIEW.STORE_PRICES SP ON INTERVIEW.P.ID = INTERVIEW.SP.PRODUCT_ID WHERE STORE_ID = 1 ORDER BY PRICE DESC LIMIT 2;

3. SELECT P.NAME,P.ID FROM INTERVIEW.PRODUCTS P WHERE P.ID NOT IN (SELECT P.ID FROM INTERVIEW.PRODUCTS P JOIN INTERVIEW.STORE_PRICES SP ON INTERVIEW.P.ID = INTERVIEW.SP.PRODUCT_ID WHERE STORE_ID = 2);

4. SELECT INTERVIEW.P.NAME, SUM(OL.QTY) FROM INTERVIEW.PRODUCTS P JOIN INTERVIEW.ORDER_LINES OL WHERE P.ID = OL.ID GROUP BY P.ID ORDER BY SUM(QTY) DESC LIMIT 1;

5. UPDATE INTERVIEW.ORDER_LINES SET LINE_TOTAL =10.00;

Since the column ORDER_LINES is declared numeric it will allow values with any arbitrary precision or scale to be entered. Order_lines column logically should be an integer type hence the choice of a numeric data type seems to be an overkill.

**UI Automation**

To run the file: python UI_automation.py /path/to/Chromedriver

**API Automation**

To run the file: pytest starWars.py

**Automation Assessment Follow Up Questions:**

**1. If you chose to use a tool or language other than the recommended, briefly explain why.**

**Answer:**

NA. As I have used Selenium for UI Automation and Pytest for API Automation.

**2.How did you go about locating the elements for your tests?**

**Answer:**

I used Chrome Developer with Inspect option for locating elements. After getting the elements, I constructed my xpath selector such that it will return the unique elements or set of such elements. I also noticed most of the elements had attribute named ‘data-test’ which was useful in uniquely targeting elements. I have used this ‘data-test’ attribute extensively in my xpath selector.

**3.What do you believe are the most common causes for instability in UI automation?**

**Answer:**

Design changes like (layout of the page) leads to instability in UI automation. The test automation suite fails when the attribute values are changed like ids or there is a change in data. Most common failures are when developers change the attribute value without changing the automation suite. In such cases, xpath selectors will fail.
Also, based on different test environments AJAX elements take a variable amount of time to render. As a result, this finding dom elements within AJAX sections becomes flaky. This can result in the UI automation test giving inconsistent failures.

**4.How do you make your tests consistent and easy to debug?**

**Answer:**

For UI Automation tests:

1. Xpath selectors should be written using ids or special attributes that do not change often. Using css classes or dom hierarchy makes the selector liable to break.

2. Common utilities like login, selecting store should be abstracted into common helper functions.

3. All data used during test can be created in a separate class to be reused later.

4. A combination of implicit waits and explicit waits can be used before fetching AJAX elements from the dom. This approach can help eliminate randomly occurring NoSuchElementException in Selenium.

5. Using a remote driver can help standardize UI tests in a CI environment.

For API Automation tests(also applicable to UI tests):

1. One test case per class

2. Easy to understand test-case names and descriptions with each test-case that outlines the steps and expected outcome

3. All setup should be done with @Before annotation or a similar annotation supported by test framework











