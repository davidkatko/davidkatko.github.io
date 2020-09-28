# Ciphertool Implementation
---------------------------
Ciphertool is an application meant to be able to encrypt and decrypt fields of text with a variety of different cipher algorithms.
This document will provide a description of the implementation and design processes behind the application.

# Structure
Some headers of this design document will feature a paired description of the implementation of an html page and it's associated function in the
application.py file, ie. index.html and index().

# Styling
The majority of the styling is done with bootstrap, initialized in the layout.html page, which will be covered in greater depth in the nextsection. There are,
however, supplementary styling elements in the static/ folder, which contains a favicon used for the dropdown menu (created by me, though it's just 4 pixels
in a square), and a styles.css sheet where I make the dropdown menu look not-quite-so-bad compared to the default html select tag.

# layout.html
The layout.html file contains the links to the stylesheets, javascript and bootstrap functionalities used in the rest of the application. It also implements
the navbar present on every page of the application, "CIPHERTOOL" and "Encrypt" redirecting to "/", and "Decrypt" redirecting to "/decrypt". A body block
is then created for the other pages to implement whatever is contained within their bodies.

# application.py, general
In application.py, the Flask library is imported first and foremost. In addition, various global variables are declared for use in later functions. These
variables are "text", which stores user text input for encryption or decryption, "key", which stores they shift value should the user choose the caesar
algorithm, and then "caesarCi", "reflectCi", "reverseCi", and "decryptCi". Each of these global variables are booleans, denoting in the first three variables
what algorithm was selected in the dropdown menu at the time that the user click the "CONTINUE" button on the index/decrypt pages. The "decryptCi" variable
is used to keep track of whether the user is decrypting or encrypting, which changes what functions are called for the /result page.

# index.html, index(), "/"
The index.html page uses a jumbotron class from bootstrap to display a welcome, description, and dynamic text field. Within the jumbotron I have implemented
a html select menu, with difference choices for every algorithm available to the user in addition to "---", the sort of 'none', initial choice. When one of
the drop down choices is selected, I have a javascript section which changes the aforementioned dynamic text field, giving a description of the algorithm
chosen. Furthermore, if caesar is chosen, the form will display a number input field. The bootstrap-implemented "CONTINUE field" will post to the page, where
index() takes over. When the "/" page is first accessed, index() will simply return index.html, and set all the global boolean variables to false should the
user return to the index page in the middle of decrypting or encrypting a set of text. When it is posted to, all the boolean global variables will be linked
inside of the function, and the option selected at the time of post will be obtained. If "---" was selected, aka. initial, the page will redirect to itself.
If any of the algorithms are chosen, the boolean global variable for that algorithm will be set to "True". If the caesar algorithm was selected, the
user-inputted number for the key field will also be saved to the global variable "key". The page will then redirect to "/text".

# decrypt.html, decrypt(), "/decrypt"
The decrypt.html page is essentially identical to index.html, save for changed text fields that reflect decryption as opposed to encryption. It is meant to
simply allow the user to select what algorithm to decrypt by. decrypt() also works fairly similarly. When first opened, the "/decrypt" page will return
decrypt.html. If posted to, the global boolean variables will be linked in the function, and the "decryptCi" variable will be set to true, indicating the
user is in the process of decrypting rather than encrypting text. The decrypt() function will then act identically to the index() function, obtaining which
option was selected at the time of post, in addition to a key value if caesar was selected. It will then redirect to "/text".

# plaintext.html, plaintext(), "/text"
As a note, this page was originally obtained with "/plaintext", but I renamed it to "/text" after realizing that if the user is trying to decrypt, they would
have encrypted text as opposed to plaintext. The plaintext.html file simply contains a title with instructions, and then a bootstrap-implemented text field of
pre-determined size, in addition to yet another "CONTINUE" button. For plaintext(), the page will first bring you to plaintext.html when accessed. If posted to,
it means the user has typed their text, so the global variable text is linked, and it's value is set to the input the user entered into the text field. The page
then redirected to "/result".

# result.html, result(), "/result"
Result.html is also essentially identical to plaintext.html, the only difference being in some of the text fields ("Result: " and the button is "RETURN") and
the fact that the text field is readonly, due to the fact that it's display the result of either the encrypted or decrypted text. The text displayed is
implemented with jinja, to be replaced later in the program with the result of a (de)cipher algorithm. result() is different in the fact that the majority of
it's implementation is found in the "GET" rather than "POST" method to the page. When the user presses "RETURN", and the page is posted to, they're simply
redirected to "/", the index page. When the page is first accessed, however, every single global variable in application.py is linked. The function then
checks whether the user is encrypting or decrypting via the state of "decryptCi". For both of these cases, the function then checks which one of the global
boolean algorithm variables is set to true, for each of caesar, reflect, and reverse. The function will then execute the algorithm functions linked to the
encryption/decryption for every cipher algorithm depending on whether encrypting or decrypting. Each of those functions will return text that is saved to a
variable named result, the algorithm boolean variable is set to "False" (as it's been completed), and the result variable is passed into the read-only text
field in result.html.

# application.py, algorithms
These algorithms are used to encrypt and decrypt the user's inputted text. With that said, reflect() and reverse() can be used to BOTH encrypt and decrypt
text, as performing the same algorithm can encrypt a text and decrypt the same text. caesar(), however, requires a revised algorithm, hence decaesar().
## caesar()
The caesar() function takes in user-inputted text in addition to a key, and immediately declares a string variable "cipher". The function then reads every
single character in the text. If the character IS NOT a letter, it is added to "cipher". If it is a letter, the ASCII value of the letter is saved to a
variable "num", and "num" is added to with the value of the key entered previously. A series of checks are then performed. If the value of "num" is then
greater than the ASCII value of 'z'/'Z', "num" is subtracted by 26 as a form of wrapping around the alphabet to the value that the letter should have been
with the key. If the value of "num" is less than the value of 'a'/'A', "num" is added to by 26 to, once again, wrap around the alphabet. After these checks,
the character that "num" represents is then added to "cipher", and the loop continues to the next character. After every character is read, caesar() returns
the contents of "cipher".
## reflect()
The reflect cipher works by mirroring half of the alphabet to the other half, ie. every letter in "ABCDEFGHIJKLM" becoming letters in the same place as
"NOPQRSTUVWXYZ" and vice versa. The reflect() function takes in the user text from the "/text" page, declares a string variable "cipher", and then
reads in every character. If the character currently being read is a letter, the character's ASCII value will be saved to a variable called "num". If it
isn't, the character will be added to "cipher", and the loop will continue to the next character. Depending on whether the character is before n (or "N"
if the character is uppercase) or on/after n, "num" will be added to or subtracted by 13 to reflect the other half of the alphabet. The result will then
be added to "cipher" as the character equivalent of the ASCII value, and progresses to the next character. Once every character has been read, the function
returns the entire string saved to "cipher".
## reverse()
The reverse() function takes in the user text from the "/text" page, declares a string variable "cipher", and then reads to a variable called "i" the amount
of characters in the user's text. It then uses a while loop to add to "cipher" every character in the user's text starting from the very end. This continues
for every character, as "i" is continually decreased by 1, until i becomes 0. reverse() then returns "cipher", containing the reverse of the entirety of the
user's inputted text.
## decaesar()
decaesar() works identically to caesar(), save for the fact that at the beginning, when the character read is a letter, the character's ASCII value is saved
to "num" and the key is SUBTRACTED from "num" rather than added to. This reverse the caesar() algorithm, and returns "cipher".