
# Insp3ct0r

## Category: 
Web exploitation

## Author: 
ZARATEC/DANNY

## Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511


## Solution

Visit the website on the browser, right click and choose to view source code(inspect elements), getting the first third of the flag, included as a html comment:

```html
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

The second part of the flag comes from the referenced CSS file mycss.cs:

/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */


The last part comes from the Javascript scipt myjs.js:

/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?1638dbe7} */



Hence combining the 3 parts gives the flag:

picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?1638dbe7}