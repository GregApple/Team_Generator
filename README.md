# Techdegree-Project-2
Create a new script
The very first step you will want to do after opening the workspace or unzipping the .zip file into your project folder is to create a new and blank Python script named app.py or application.py.

Proper use of Dunder Main
Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file:

Dunder main statement looks like this:

if __name__ == "__main__":

HINT: Unit 1 project files/workspace had an example of this.

NOTE: This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported.

Import player data
Import from constants.py the players' data to be used within your program.

NOTE: Python has no concept of actual constants like other languages have. But it is a convention you may see in the real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or a value that you cannot change/alter.

Create a clean_data function
Write the logic to:

1) read the existing player data from the PLAYERS constants provided in constants.py 2) clean the player data without changing the original data (see note below) 3) save it to a new collection - build a new collection with what you have learned up to this point.

Data to be cleaned:

Height: This should be saved as an integer
Experience: This should be saved as a boolean value (True or False)
HINT: Think Lists with nested Dictionaries might be one way.

NOTE: Ensure you **do not directly modify the data in PLAYERS or TEAMS constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection. If you are unsure of what this means, checkout this instruction step.

Create a balance_teams function
Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.

HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)

Console readability matters
When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

Displaying the stats
When displaying the selected teams' stats to the screen you will want to include:

Team's name as a string
Total players on that team as an integer
The player names as strings separated by commas
NOTE: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma separated string so the user cannot see any hints at what data type players are held inside.
