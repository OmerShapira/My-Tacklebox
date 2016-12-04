# Tacklebox
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
