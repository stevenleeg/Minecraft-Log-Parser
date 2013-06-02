Minecraft Log Parser
=====================
MCLP is a simple Python script that can generate statistics about a Minecraft server based on it's `server.log` file.

![MCLP in action](http://i.imgur.com/dweVw.png)

## Current Features
 * Calculates total time played for each player.

As you can see, the feature list is pretty slim right now. The good news is I have some:

## Planned Features
 * Generate death counts
 * Calculate total play times based on how long it's been since they first joined the server (balancing old players vs new players, basically)
 * Generate an HTML summary, since the CLI is no fun to work with.
 * Server errors

I'm open to suggestions. If you have an idea for a statistic that could be generated feel free to suggest it in the issue tracker. If you're feeling extra generous, you could always implement a feature on your own and submit a pull request!

## Installation/Usage
I tried to make using MCLP as easy as possible. As long as you have `pip` installed, usage is as simple as:

	pip install mclp
    mclp /path/to/server.log

Then you should see some neat statistics show up!

## License
Minecraft Log Parser is released under the [MIT License](http://opensource.org/licenses/MIT). Have fun and make awesome things with it!
