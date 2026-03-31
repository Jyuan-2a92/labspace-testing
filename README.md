# Command-Line-Quiz

**Command-Line-Quiz** is an interactive, user-friendly application designed to facilitate engaging quiz experiences directly in the terminal. Ideal for both educators and learners, the application allows users to create and take customizable quizzes composed of multiple-choice questions. Users can easily input their own questions and answers, save them as JSON files for future access, and take quizzes at their convenience.

The application features a simple command-line interface that provides a straightforward menu for navigating options, including creating new quizzes and taking existing ones. After each quiz session, users receive immediate feedback on their performance, including their score and the correct answers for any questions they missed. With the ability to randomize question order and save created quizzes, **Command-Line-Quiz** promotes active learning and allows for a dynamic and personalized educational experience. The application combines convenience and functionality, making learning both accessible and enjoyable in a terminal environment.

### Key Features
1. **Question Creation:** 
* Users can interactively create and define their own quiz questions.
* Prompts the user to enter both the question and the correct answer.
2. **Quiz Storage:**
* Saves quizzes in JSON format, allowing for easy storage and retrieval.
* Quizzes are named by the user and saved as separate files.
3. **Quiz Loading:**
* Users can load existing quizzes to take them at any time.
* Checks if the quiz file exists before attempting to load it, providing user feedback.
4. **Quiz Randomization:**
* Randomizes the order of questions to ensure a different experience each time the quiz is taken.
5. **User Interface:**
* Provides a command-line menu for a user-friendly experience, allowing easy navigation between creating, taking, and exiting the quiz.
6. **Score Tracking:**
* Tracks and displays the user’s score after taking the quiz, providing immediate feedback.

### Acceptance Criteria

* When application starts, it displays three different options: take quiz, create quiz, exit.
* Show error message if asking for a quiz that does not exist.
* When user choose create quiz, the application should ask the quiz name and it should not be empty.
* Each quiz can have more than one question.
* Each question only has a correct answer.
* When user choose take quiz, the correct answer will prompt success message, vice versa.