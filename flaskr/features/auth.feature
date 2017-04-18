Feature: CoinMart login page authentication

  Scenario: User logs in
    Given CoinMart is set up
      When I log in with "admin" and "default"
      Then I should see the response message "You were logged in"

  Scenario: User logs in with incorrect username
     Given CoinMart is set up
      When I log in with "notright" and "default"
      Then I should see the response message "Invalid username"

  Scenario: User logs in with incorrect password
     Given CoinMart is set up
      When I log in with "admin" and "notright"
      Then I should see the response message "Invalid password"

  Scenario: User logs out successfully
     Given CoinMart is set up
      and I log in with "admin" and "default"
      When I log out
      Then I should see the response message "You were logged out"

  Scenario: User adds a valid credentials
    Given CoinMart is set up
      and I log in with "admin" and "default" and redirected to the registration page
      When I add a new entry with "test" and "Hema7067" as the username and password
      Then I should see the response message "New entry was successfully posted"

  Scenario: User adds a invalid credentials
    Given CoinMart is set up
      and I log in with "admin" and "default" and redirected to the registration page
      When I add a new entry with "test" and "test" as the username and password
      Then I should see the response message "Not a Valid Password. Password should be minimum 8 letters long with at least one capital letter a number"