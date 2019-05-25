%FACTS
dobra_kondycja(marek).
dobra_kondycja(jan).

biega(jan).
biega(marek).

plywa(adam).
plywa(jan).

%Rules
sportowiec(X):- plywa(X); biega(X).
startuje_zawody(X):- sportowiec(X), dobra_kondycja(X).
pilkarz(X):- biega(X), dobra_kondycja(X).
