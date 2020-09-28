# Ciphertool Documentation
---------------------------
Ciphertool is an application meant to be able to encrypt and decrypt fields of text with a variety of different cipher algorithms.
This document will provide a user-manual for the application through the use of descriptions that outline the various functions of the application.

# Compiling and running
In order to compile, simply navigate to the final/ directory (the same directory this file should be found in) and execute "flask run" in the CS50 IDE.
Then open the link that flask creates.

# The navigation bar
The first page you will be brought to is the index page, "/". You'll be greeted with a message that reads "Welcome to CIPHERTOOL!". At the top, you'll
notice a navigation bar containing the items "CIPHERTOOL", "Encrypt", and "Decrypt". The "CIPHERTOOL" item will bring you back to the index page,
as will the "Encrypt" item, on click. The "Decrypt" item will bring you to the /decrypt page.

# The index page
The index page acts as the page from where the user will be able to begin encrypting their message. Under the "Welcome to CIPHERTOOL!" heading, the
text urges the user to use the dropdown menu to select a cipher method. Above the dropdown exists a dynamic field of text that changes based on what
is currently selected in the dropdown. The dynamic field of text will give a brief description of the algorithm selected from the dropdown, or otherwise
ask the user for more information, such as a key value for the caesar algorithm. If the user tries to click the "CONTINUE" button when no algorithm is
selected, ie. "---", the page will simply refresh. Should the user successfully select an algorithm, the page will redirect to the /text page.

# The decrypt page
The decrypt page is functionally identical to the index page. The messages will reflect the fact that the page is used for decryption, asking the user
to select the algorithm with which the text they want to decrypt was encrypted by. Selecting the different algorithms will update the dynamic text with
a description of what the algorithm would have done. Upon pressing "CONTINUE", the page redirects to the /text page.

# The text page
Here, the user will be able to type or paste their text (whether to be encrypted or decrypted) into the text field. Upon pressing continue, the page
will redirect to the /result page.

# The result page
Here, a read-only text field will display the result of the user's inputted text, either encrypted or decrpypted, read-onlu as to easily allow for
copying. The "RETURN" button will lead the user back to the index page, "/".