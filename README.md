# Shipt

UI Automation of Feature - StoreView based on zip code.

Tools used:Selenium

Feature Description:
* User should be able to see the stores name which have shipt service based on the delivery address selected.
* User should not be able to add an address to its address book where shipt service is unavailable(eg:Wyoming State).

High Level Scenarios:
1. Verify that a user is able to see the store names that have shipt service based on the delivery address selected.
2. Verify that the products are displayed after the store selection.
3. Verify that after the user changes the delivery address from dropdown, the store selection changes based on the shipt service availability. 
4. Verify that the user is not able to save an address where shipt service is unavailable.
5. Validate the error message is thrown when a user tries to save an address where shipt service is unavailable.
