# My example test module

## Description 

This module tests addition works correctly for the bank transaction.

## Tests

### Test foo

#### Intent

Test that the foo function works (positive flow) for a range of values

#### Walkthrough of steps

1. Set up session
1. Send POST {foo} to create a foo (store its foo id)
1. Send PUT {add:5} to add 5 to the foo function
1. Send GET /<foo_id> (check it is correct)

#### Expected outcome

The foo functionality should work for a range of values (positive flow)

### Test bar

#### Intent

Test that the bar function rejects bad data (negative flow)

#### Walkthrough of steps

1. Set up a session
1. Send POST {bar} to create a bar (store its bar_id)
1. Sent PUT (empty body) {} (check error 4xx response returned)
 
#### Expected outcome

Test that the bar function rejects an invalid input