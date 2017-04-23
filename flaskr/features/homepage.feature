# Created by Hema at 4/23/2017
Feature: Home Page

  Scenario: Visit homepage
    Given a user visits the site
    Then she should see Coin Mart

  Scenario: Logout Link
    Given a user visits the site
    When she logs in
    And she returns to the site
    Then she should see the Logout link