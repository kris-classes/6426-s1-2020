1:  
I had trouble with having multiple new sims/pixels being spawned on top of each other each time my code checked for where new sims can be placed. To fix this I implemented a system the prevents duplicates from being revived. Using a set resolves this.

2:  
It struggles with a higher number of sims, since it has to check all the sims surrounding it. My code often repeats checks and certainly could be optimized further.
It does really well when there is a small number of alive sims.

3:  
Conway's Game of Life is used to show evolution and how things can interact with each other with only a few simple rules. 

4:  
Since my code re-checks every possible sim/pixel position surrounding live sims, my code has to check 8 pixels for every live pixel.
