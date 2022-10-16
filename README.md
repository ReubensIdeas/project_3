# HANGMAN

Hello and welcome to Hangman! This game was created using Python and is a simple word guessing game. You guess the word by guessing which letters are in said word, or simply guess the word. However, there's a catch! You must guess the word within 6 tries otherwise the man gets hanged!
<hr>

## How to run the game
- Simply type, 'python run.py' into the terminal and the game will load
- Once the game has loaded, follow the on-screen instructions
<hr>

## Technologies and Frameworks used
<hr>

### Programming language
- Python
### Frameworks and Tools
- GitPod
- GitHub
- Heroku
### libraries
- random: Used to gather random words from my word lists
- os: Used to clear the terminal when needed
- sys: Used to allow the user to exit the game
- time: Used to make a print line fade away after 2 seconds
### Functions imported from external files
- words from word_list: This is the easy difficulty word list
- words_medium from medium_words: This is the medium difficulty word list
- words_hard from hard_words: This is the hard difficulty word list

## Project goals
<hr>

### User goals
- Play a simple word guessing game
- Enjoy the game through 3 different difficulty levels
- Lots of play time due to 30 different words available
- Rules to understand how to play the game
### Game creator goals
- Create a simple, easy to understand but fun game
- Make sure the player understands how to play the game
- Ensure there are no bugs when playing the game
- Create different difficulty levels for the sure to enjoy
- Ensure the words that are being guessed have been randomly selected
<hr>

## UI/UX (User Interface and User Experience)
<hr>

### Game start-up screen
![HANGMAN menu](https://i.imgur.com/YvicrNB.jpg)
- Once the game has loaded you will see this screen (main menu)
- This UI shows the name of the game in ASCII art (HANGMAN) along with a welcome message and immediately explains how to exit the game alongside how to go back to this menu screen if needed
- Below this is the option to select the difficulty of the game, by pressing 's' and the option to see the rules, by pressing 'r'

This UI brings an easy and effortless user experience due the simplicity of the instructions at hand and the two options of difficulty levels and rules to said game.

### Game rules
![HANGMAN rules](https://i.imgur.com/Yg6IQZQ.jpg)
- The rules menu explains the rules in a bullet point fashion for the user to read easily
- Underneath the rules are instructions on how to navigate back to the menu, start the game through selecting the user's difficulty preference, or how to exit the game

This UI was kept simple due to the simplicity of this game and to ensure the user experience is not dulled down by instructions.

### Difficulty selection
![HANGMAN difficulty](https://i.imgur.com/BrP7nM6.jpg)
- The difficulty selection screen is designed with a simply prompt, 'Choose you difficulty:' and three difficulty options, EASY, MEDIUM and HARD

The difficulty selection UI is as simply as it gets. The reason for this is streamline the user's expereince as to not add anything that's not needed.

### The hangman game
![HANGMAN game](https://i.imgur.com/QX4oMja.jpg)
- Once the difficulty has been selected, you will land here (see above image) and the game will select a word, at random, form one of three difficulty word lists. Each list has 10 words.
- The user is shown text at the top that indicates the game has started
- There is a hanging post showing the stages of the game (this will be filled in with different parts of the stickman to show how many guesses the user has)
- Underneath the hanging post there is the word the user is trying to guess. Each, '_' indicates a letter in the word. This is where the user will see each letter they have guessed.
- Finally, we have the prompt of where to guess the word, or letter. Alongside this there is information on how to navigate back to the main menu

The in-game UI was desinged so that the user experience is not cluttered by information, but they still have clear information that the game has started, the point they are at in the game and how many letters the word they are guessing has. 
It was also ensured that the user knows hwo to navigate back the main menu if they wish to change the difficuly or check the rules again.

### The end of the game
![HANGMAN end-screen](https://i.imgur.com/JA7psBv.jpg)
- Once the game has ended (either through winning or losing), the user will be presented with a prompt, 'Play again? (Y/N)'. If the user presses, 'y' the game will restart. If the user presses, 'n' they will return back to the main menu

This allows the user to quickly replay with a different word or return back to the main menu so check the rules or change the difficulty.
<hr>

## Testing
As this is an input only game, the tests where done through inputting different types of words or characters to ensure there were no bugs.
<hr>

### Main menu
- When any wrong character or word is inputted that the terminal should say, 'Please select a valid option!'
> Result: Works as expected
- When, 'exit' was inputted for the game to shut down
> Result: Works as expected
- When, 'r' is inputted for the game to show the rules menu
> Result: Works as expected
- When, 's' is inputted for the game to clear the terminal and show the difficulty selection menu
> Result: Works as expected

### Rules menu
The same testing from the main menu section was done through the rules screen, with the exeption of the below.
- When, 'menu' is inputted for the game to clear the terminal and show the main menu screen
> Result: Works as expected

### Difficulty level
The same testing from the main menu and rules menu section was done through the difficulty selection screen, with the exeption of the below.
- When, 'easy' is inputted for the game to clear the screen and start the hangman game in the easy difficulty
> Result: Works as expected
- When, 'medium' is inputted for the game to clear the screen and start the hangman game in the medium difficulty
> Result: Works as expected
- When, 'hard' is inputted for the game to clear the screen and start the hangman game in the hard difficulty
> Result: Works as expected

### The hangman game
The same testing from the above sections was done whilst in the hangman game, with the exeption of the below.
- When a correct letter is guessed the terminal should print, 'Well done,  **guess** is correct' and the letter the user has inputted will replace a '_' from the word
> Result: Works as expected
- When a correct word is guessed the terminal should print, <br>
'Congratulations, you guessed correctly! You WIN!' 
<br>
'Play again? (Y/N)' <br> and the word the user has inputted will replace the '_'s from the word
> Result: Works as expected
- When a wrong letter is guessed the terminal should print, '**guess** is not in the word.' and the hanging post adds another part of the stickman to it
> Result: Works as expected
- When the same letter is guessed twice, the terminal should print, 'You already guessed the letter **guess**'
> Result: Works as expected
- When a wrong word is guessed the terminal should print, '**guess** is not the word.' and the hanging post adds another part of the stickman to it
> Result: Works as expected
- When a word is guessed that has more or less letter than the supplied word, the terminal should print, 'Not a valid guess.'
> Result: Works as expected
- When the same word is guessed twice, the terminal should print, 'You already guessed the word **guess**'
> Result: Works as expected
- When the user has run out of guesses, the game should end and the terminal should print, <br>
'Sorry, you're out of tries. The word was: **word**.'
<br>
'Play again? (Y/N)' <br>
If 'y' is typed the game should restart. If 'n' or any other letter is typed the user should go back to the main menu
> Result: Works as expected
<hr>

## Target audience
This game is advised to be played by participants above the age of 5 due to some words being quite difficult to guess.
Besides this age advisory there is no target audience.
<hr>

## Bugs/Warnings
<hr>

Solved bugs:
- The game would exit if any input that it did not recognise was inputted
> This was solved by adding in an 'else:' statement followed by, 'print("Please select a valid option!") time.sleep(2)' to my inputs
- The game would only go back to the main menu if the user inputted, 'menu' twice
> This was fixed by creating a variables for my inputs so that the programme would expect one input

Unsolved warnings:
- There are 3 warnings relating to the .gitpod.yml file. These are due to GitPod not syncing with them. This is an error on GitPod's end and will be fixed at a later time

## Validation
<hr>

Due to PEP8's website being down, this project was validated through the IDE by installing, 'pycodestyle' and running it's in-built linter.
This received no errors, but 3 warnings (as mentioned above: Unsolved warnings).

## Deployment
<hr>

### Heroku
Heroku was used to deploy this game throgh GitHub. Below are the steps that were taken:
1. Create an account on herkou.com or sign in.
2. Click, 'Create new app' add your project name and choose your region then click 'Create app'.
3. Once the new page is loaded, navigate to the settings tab.
4. Click, 'Reveal Config Vars'. Type, 'PORT' into the 'KEY' section and '8000' into the 'VALUE' section then click, 'Add'.
5. Scroll down and click, 'Add buildpack'. When presented with the options select, 'python' and then, 'Save changes'. Do the same for, 'nodejs'. **Ensure that, 'python' is above, 'nodejs'**.
6. Navigate to, 'Deploy'. Scroll down to, 'Deployment method' and select 'GitHub'. Once the 'Connect to GitHub' button has appeared, click that.
7. Search for you GitHub repository you wish to deploy. Once you have found your repository, click 'Connect'.
8. Now you are ready to deploy your project. If you wish to allow Heroku to automatically deploy your project, click 'Enable Automatic Deploys'. If you wish to manually deploy your project, select 'Deploy Branch'. In this case, I chose to manually deploy my project.
9. Heroku will now build your project.
10. Once your project is built, you can click, 'View' to view your project.
### GitHub
This project was deployed to GitHub pages. The steps to deploy are as follows:
1. In the GitHub repository, navigate to the Settings tab.
2. From the source section drop-down menu, select the 'Main' branch.
3. Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
4. The live link can be found here - https://reubensideas.github.io/project_3/

## Credits
<hr>

- Code Institute - for supplying the IDE template

## Acknowledgements
<hr>

- My mentor, Chris Quinn - Chris has supplied wonderful guidance
- Code Institute Support Team - The team has been incredible at getting me through tricky coding questions