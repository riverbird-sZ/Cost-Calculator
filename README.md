# Cost-Calculator

### Task: **"Creating a Cost-Splitting Calculator"**

#### Description:
Create an application to split expenses among friends after a group trip or dinner. The application will have a simple frontend for entering expenses and displaying results.

#### Task Details:

1. **Backend Functionality (Python):**
   - Accept input data for:
     - The number of participants.
     - Their names.
     - The expenses each participant incurred.
   - Calculate:
     - How much each participant spent in total.
     - How much each participant owes or should be reimbursed so that everyone is "even."
   - Display the results clearly (e.g., "Anna owes Mark 10 EUR").
   - Save the results in a text file (`.txt`).

2. **Frontend (HTML + CSS):**
   - Create a simple HTML page that allows:
     - Input for the number of participants and their names.
     - Input for individual expenses for each participant.
     - A button to calculate and display the expense split results.
   - After clicking the button, the frontend should send the data to the Python script.

3. **Requirements:**
   - Use only the basics covered in the first three chapters of *Automate the Boring Stuff with Python*:
     - Variables, lists, loops, conditionals, and basic functions.
     - File handling for generating the `.txt` report.
   - The frontend should be static HTML with basic CSS styling.
   - The backend should not use advanced libraries like Flask or Django.

4. **Bonus Features (Optional):**
   - Add validation to check if the input values are valid numbers (e.g., negative numbers are not allowed).
   - Allow the input of shared expenses that all participants split equally (e.g., car rental).
   - Expand it with features like exporting results to CSV files or adding more input validation.
 
