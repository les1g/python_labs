# Find Max Algorithm

## Goal of this module

Demonstrate how an algorithm solves a computational problem by following a clear sequence of steps.  

This lab shows how to translate pseudocode into a working Python function.

## Computational Problem

**Input:**  
A list (array) of numbers.

**Question:**  
What is the largest value in the list?

**Output:**  
A single number: the maximum element.

This is a classic example of a computational problem:  
- You are given input data  
- You ask a specific question about that data  
- You compute the answer using an algorithm  

## Algorithm Description

The `FindMax` algorithm works by:

1. Assuming the first element is the maximum  
2. Scanning through the rest of the array  
3. Updating the maximum whenever a larger value is found  
4. Returning the final maximum value  

This algorithm runs in **O(n)** time because it examines each element once.
