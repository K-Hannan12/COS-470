/*
Designate has/1 and location/1
as dynamic. Which means they can
be changed using assertz and retract.
*/
:- dynamic(has/1).
:- dynamic(location/1).
:- dynamic(contains/2).

/****************************************
These facts are not really needed.
I've given them here, just so you have
a list of the room and things.

room(dungeon).
room(crypt).
room(basement).
room(graveyard).
room(garden).
room(church).
room(hall).
room(kitchen).
room(shed).
room(gate).
room(lab).
room(tower).
room(diningroom).

room(nowhere). A fake room where things go when
taken.

thing(message).
thing(code).
thing(key).
********************************************/


/* Note: These edges are UNDIRECTED.
Meaning the player can move from one
location to another in either direction.
You code will need to account for that.
*/
edge(dungeon, crypt).
edge(crypt, basement).
edge(graveyard, crypt).
edge(garden, graveyard).
edge(church, garden).
edge(garden, shed).
edge(basement, hall).
edge(garden, hall).
edge(gate, hall).
edge(kitchen, hall).
edge(kitchen, diningroom).
edge(tower, diningroom).
edge(hall, tower).
edge(lab, tower).
edge(shed, crypt).

/* The starting location of the things.
*/
contains(lab, message).
contains(dungeon, code).
contains(church, key).

/* Initial state:
- Player has nothing
- Player's location is the kitchen.
*/
has(false/0).
location(kitchen).

/* The win condition. After running
your game using play/0, I should be able to type:
win(), and prolog responds: true.
*/
win() :-
    (
	has(message),
	has(code),
	has(key),
	location(gate)
    )
    -> format('You are free of the spooky mansion.~n').

/* You may only use this predicate
to move the player between locations.
This only moves the player from one
location to another if the room the
player's current location are directly
connected (one edge away).
*/
move(X) :-
    canmove(X)
    -> (
		%location(CurrentLoc), For Debuging
        %format('Moving from ~w to ~w~n', [CurrentLoc, X]), For Debuging
	    retract(location(_)),
	    assertz(location(X))
	);
    false.


/* You may only use this predicate
to take things from the environment.
The take/1 predicate will take the
thing X if the player is currently
in the location where it is located.
Once taken, a thing is moved into a
nowhere location that is not reachable
to simulate the player has it. This
prevents the player from taking it
multiple times.
*/
take(X) :-
    (
	location(Y),
	contains(Y, X)
    )
    -> (
		%format('~nTaking ~w from ~w~n~n', [X, Y]), For Debuging
	    assertz(has(X)),
	    retract(contains(Y,X)),
	    assertz(contains(nowhere,X))
	);
    false.

/****************************************
Write your code below. Think of the
play/0 predicate as the main() function.
It should start the simulation. When
play/0 is called, the simlation should
do the following:

- Move to one of the things and take it.
- Move to the next and take it.
- Move to the third and take it.
- Move to the gate.

Hints:
- Don't hard-code the solution. When I test
your code, I will rearrange a
few connections and a thing or two. If you
hard-code your solution, it will not work
when I test it.
- I will NOT change the names of the rooms
or things. Your code can assume fact names
stay the same.
- The gate will always be the exit.
- The player will always start in the kitchen.
- Your code must programmatically
find the correct path to each thing and
then to the gate.
- I suggest you create a cleanup/0 predicate
that uses retract or retractall, to reset
the simulation back to its initial state;
otherwise, facts created during previous
runs will persist.

All of the above should happen automatically
when the play/0 predicate is called.

Once the player has all three things and is
in the gate location, the win condition will
be true.
****************************************/

/* You will need to fill in play/0.
You can write as many additional predicates
as necessary. You may alter the predicates
I have provided for testing alternate maps
but note that I will use my own. For
grading */


% Kaleb Hannan
% COS470
% HW4
% 11/14/2024

% resetWorld: (This resets the word to the default as from when I got the assinment.)
reset():-
	retractall(location(_)),
	assertz(location(kitchen)),	
	retractall(has(_)),
	retractall(contains(_,_)),
	assertz(contains(lab, message)),
	assertz(contains(dungeon, code)),
	assertz(contains(church, key)).

%
%
% Rule to see if a player can move to a room
canmove(X) :-
    location(Y),
    (edge(X, Y); edge(Y, X)).
%
%
% Get path from one location to another
canFindMove(X,Y):-
	edge(X, Y); edge(Y, X).

%
% Get path from one location to another	
path(Start, End, Path) :- 
    pathHelper(Start, End, [Start], Path).

% Path helper with visited tracking to avoid loops
pathHelper(End, End, Visited, Visited). % Base case for recursive function
pathHelper(Start, End, Visited, Path) :-
    canFindMove(Start, NextLoc),
    \+ member(NextLoc, Visited),
    pathHelper(NextLoc, End, [NextLoc | Visited], Path).
%
% Move along path
moveAlongPath([]). % Base case for recersive function
moveAlongPath([Room|ResetOfPath]):-
	move(Room),
	moveAlongPath(ResetOfPath).
%
%
removeheadOfPath([_|Tail], Tail).
%Clean path
cleanPath(Path,CleanPath):-
	reverse(Path, ReversPath),
	removeheadOfPath(ReversPath,CleanPath).

% Get thing
getThing(Thing):-
	location(X),
	contains(Loc, Thing),
	path(X,Loc,Path),
	cleanPath(Path,CleanPath),
	moveAlongPath(CleanPath),
	take(Thing).
%
%
% Go to exit (gate)
goToExit():-
	location(X),
	path(X,gate,Path),
	cleanPath(Path,CleanPath),
	moveAlongPath(CleanPath).
%
%
play():-
	getThing(message),
	getThing(code),
	getThing(key),
	goToExit().