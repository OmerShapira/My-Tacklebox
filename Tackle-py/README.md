# Tacklebox
## Usage

``` bash
tackle
# (usage)

tackle hook all
tackle hook vimrc
tackle unhook vimrc

tackle fetch
# (pull changes)
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
tackle snip -c glsl/nosie
tackle clip glsl/noise

tackle wipe 
# clear everything from the computer

```
