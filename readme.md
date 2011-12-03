Minecraft Log Parser
=====================
MCLP is a simple Python script that can generate statistics about a Minecraft server based on it's `server.log` file.

![MCLP in action](http://i.imgur.com/FJeRq.png)

## Current Features
 * Calculates total time played for each player.

As you can see, the feature list is pretty slim right now. The good news is I have some:

## Planned Features
 * Generate death counts
 * Calculate total play times based on how long it's been since they first joined the server (balancing old players vs new players, basically)
 * Generate an HTML summary, since the CLI is no fun to work with.
 * Server errors

I'm open to suggestions. If you have an idea for a statistic that could be generated feel free to suggest it in the issue tracker. If you're feeling extra generous, you could always implement a feature on your own and submit a pull request!

## Usage
Using MCLP is pretty basic. Just clone the git repository, cd to the directory your server.log resides in, and run the script.

**Example for the needy:**

	git clone https://stevenleeg@github.com/stevenleeg/Minecraft-Log-Parser.git
	cd ./mc-server
	python ../Minecraft-Log-Parser/parser.py

Then you should see some neat statistics show up!
