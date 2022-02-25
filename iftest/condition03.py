#!/usr/bin/env python3
# Alta3 Research || Author: RZFeeser@alta3.com
# Check hostname against expected value

## Collect input from user
hostname = input("What value should we set for hostname? ")  # add a whitespace at the end of our question

## normalize hostname
hostname = hostname.lower() # make it lowercase
hostname = hostname.strip() # removes all whitespaces that might be surroudning either side of hostname

## use the lower method to test if input value matches expected value
if hostname == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")


