# Created by dheid at 3/12/2024
Feature: Filtering

   Scenario: User can filter by sale status Last Units
    Given Open the main page
     When Log in to the page
     When Click on “off plan” at the left side menu
     Then Verify off-plan in url
     When Filter by sale status of “Last Units”
     Then Verify each product contains the "Last Units" tag