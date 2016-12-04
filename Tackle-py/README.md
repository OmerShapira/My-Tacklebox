# Tacklebox
Tacklebox is a configuration manager for people working on multiple computers. It handles:
* Making your local settings portable
* Updating any changes you make to your settings back into your collection
* Backing up anyone else's local settings while you work
* Searching snippets and other things you need
* Cleaning up after you're done with a computer

Tacklebox uses git as a backend. Any changes you make will be pushed back into your remote git repository.
## Usage

``` bash
tackle
# (usage)

tackle hook all
# stages all baits (packages)
tackle hook vimrc
# stages vimrc, backing up the previous one if it exists
tackle hook --overwrite vimrc
stages vimrc without backing up previous versions.
tackle unhook vimrc
# unstages vimrc, restoring backups.

tackle fetch
# (pull changes from main repo)
tackle refresh [bait/file]
# (deploy changes)
tackle collect [bait/file]
# (collects changes to baits and pushes them)

tackle inventory
# (shows baits)

tackle snip glsl
# (returns a list of all glsl snippets)
tackle snip glsl/noise
# (prints glsl/noise.glsl into the console)
tackle snip -c glsl/noise
tackle clip glsl/noise
# copies glsl/noise snippet to clipboard

tackle wipe 
# clear everything from the computer

```
