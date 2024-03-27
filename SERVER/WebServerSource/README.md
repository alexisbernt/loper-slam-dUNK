# Sample Web Application using HTML5, PHP and MySQL
The solution is based on the traditional framework of:  |HTML5| <--> |PHP| <--> |MYSQL|
-The FrontEnd basic compenents were developed using HTLM5 framework, designed using CSS 3.0 and animation was applied using Javascript and Bootstrap.
-The BackEnd was built on a MySQL database having a single table to store the different words and their frequencies.
-The Frontend and Bacakend were connected using PHP as the server-side scripting language.

# 1. Deployment
To ensure a hastle-free testing experience, I have deployed my website live at http://vcanteen.000webhostapp.com/. 
This was a vacant server available from one of my earlier hosted projects on 000webhost.com which is a site that provide a free hosting space of upto 2 websites.

NOTE: First test run, often results in a long wait/loading delay.
Just stop the page from loading and reload it. Should work fine for all the remaining test cases to be tested after that.

# 2. Front-End / Workflow of Website
- Index.html
This is the landing page of my website, and a neat and simple page to take us to the page where the user needs to enter the input.
Was built on HTML/CSS and Javascript.
- Input.html
This is the next stage of the website, once where the user needs to enter the value of N, based on which N-most frequent words from the input test file would be displayed on the next phase.
- Output.php
This is the final stage of the website, where a table displays the N-highest occuring words as recovered from the text file.

# 3. BackEnd Working and steps involved

1. On the 2nd stage at Input.html, user first enters the value of N, which needs to be carried to the next phase, as this is the number of results that we need to display on the final output. This the input stage. The input is captured using an HTML form in an input area, and the data is transmitted to the next page using POST method.

2. In this stage (Output.php) we need to show the first N words with highest frequency. First, we capture the value of N frm the previous form using $GET_POST method.

3. Next, the system then fetches the target file from a server located at http://terriblytinytales.com/test.txt This is done using PHP by the file_put_contents() command.

4. Once the  file is downloaded and saved on our server with the name test.txt, we can now read it directly. The file is read agan by PHP with the command file_get_contents(). This returns the entire text files, into an array of words, delimitted by a space. thus seperation of the entire string in tokens of words is done in this stage. this original array is called $words.

5. With the entire text file and its words available in the array, we now need to create another refined version of the array, which does not contain any duplicate or repatative words. We call this array as array $unique_words.

6. Now, we can move to the stage where the frequency is calcuated for each word.

# 4. Frequency Calculation Logic 

1. For each word in array with unique words,

2.     Loop through the original array

3.     Find the number of occurances of the word (keep a counter, increment it when a match is found)

4.     Store the words, and their final count in SQL table using an INSERT Query. SQL queries are executed in PHP script itself by    establishing a connection to the SQL server in PHP and firing queries through it.

5. Finally, once all the words and their frequencies are stored in the database, we now need to retrieve the results, as per Users requirement.

6. Similar to the INSERT Query, we now fire a Select query "SELECT * FROM test ORDER BY count DESC LIMIT $number"
such that it selects the top N rows from our database, IN SORTED ORDER (descending). Hence, no need to explicitly sort our table in SQL, while retrieving itself we can choose in which order we want it sorted.

7. Finally, these results are now iteratively displayed in a tabular format using HTML embedded in this php script.

# 5. Testing (Screen Shots attached)

Test Case 1: N=5
A table containing top 5 words with highest frequency was displayed successfully.

Test Case 2: N=10
A table containing top 10 words with highest frequency was displayed successfully.

Test Case 3: N=50
A scrollable table with fixed header containing top 50 words with highest frequency was displayed successfully.

Test Case 4: N=2
A table containing top 2 words with highest frequency was displayed successfully.
