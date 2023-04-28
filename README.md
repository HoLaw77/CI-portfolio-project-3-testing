<h1>Lunch Survey</h1>

<p>Lunch Survey is a Python survey database system that enable user to input their lunch choice with their ages, gender, lunch choice, and willingness to buy again.</p>

<p>The aim of this survey project is to collect and analyse the relationship between the food choice and different age groups, gender. In order to provide sales data for supermarket in maximizing sales in lunch hours.</p>

<h1>How it works?</h1>

<p>The survey can be structured into four main parts: survey_input(), validate_survey(), update_worksheet(), and survey_result().</p>

<h2>survey_input()</h2>

<ul>

<li>Users will be requested to input their age, gender, food choice (sandwich, fish and chip, noodle and salad) and willing to buy again (yes or no). </li>

<li>If user input answer that does not match the required options, it will print out Error message and request user to reenter.</li>

<li>The result will be printed out for user reference.</li> 

<li>The result will be reorganised into a list format by append method. </li>

</ul>

<h2>update_worksheet()</h2>

<ul>

<li>After receiving user input and validated the data type is correct, they will be updated to the google worksheet named "sales" </li>

<li> It will append the list when user finish inputting</li>

<li> It will print out a statement saying the worksheet is successfully updated.</li>

<li> As each product also has their own worksheet, they will have a separate update function for updating the list data if the food choice matches the required choice for categorisation.</li>

</ul>

<h2>survey_result()</h2>

<ul>

<li>This function would collect data from the food choice spreadsheet (e.g."salad_sales" for salad).

<li>This function would loop through the data to screen out the number of male and female in the data list and the number of people who say yes to buy again.</li>

<li>This function will also get the age value from the google spreadsheet and canculate it to produce the mean of users' age within the food choice spreadsheet.</li>

<li>This function would also print the result out to show the result to the user.</li>

</ul>

<h1>Feature</h1>

<ul>
<li>Printing out the users' choice after they have entered</li>
<li>Break the function if users' answers do not match the required options</li>
<li>Print out average age, male and female, and number of people buy again with each food choice.</li>
</ul>

<h1>Testing</h1>

<ul>
<li></li>
<li></li>
</ul>