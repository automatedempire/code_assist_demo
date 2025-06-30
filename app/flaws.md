# Gemini Code Assist - Flaw discovery

I wanted to showcase the GitHub Gemini Code Assist bot's ability to review bad code, so I made Gemini write some _really_ bad code. Using the new Agent mode of Gemini Code Assist in my IDE (which was probably overkill, but I like playing with new toys), I had Gemini create a simple webapp.

> I am building a demo for showcasing Gemini's ability to debug code. I need you to create a simple Flask webapp with 3 routable paths that have noticeable flaws. 1. Add a SQL injection vulnerability to one path. 2. Add some poorly named variables to another path that will add two numbers and return the sum. 3. Make up some other medium code flaw that would be caught by a senior-level developer reviewing the code.

Here are the vulnerabilities it came up with:

## Flaw 1: SQL Injection Vulnerability
The `get_products` endpoint is vulnerable to SQL injection. An attacker could provide a malicious category string like:

  ' OR 1=1; --

## Flaw 2: Poorly Named Variables
The `add_numbers` endpoint uses poorly named variables, making the code hard to read.

## Flaw 3: Insecure Deserialization and Inefficient File Handling
Th `get_user` endpoint reads a file on every request and uses the insecure `eval()`
function to parse data, which can lead to arbitrary code execution.
