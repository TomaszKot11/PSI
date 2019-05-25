 %FACTS
 kobieta(maria).
 kobieta(anna).
 kobieta(wanda).
 kobieta(ewa).
 kobieta(zofia).
 kobieta(katarzyna).

 mezczyzna(franciszek).
 mezczyzna(jan).
 mezczyzna(bogdan).
 mezczyzna(krzysztof).
 mezczyzna(wojciech).
 mezczyzna(robert).

 malzenstwo(jan, maria).
 malzenstwo(bogdan, anna).
 malzenstwo(wojciech, zofia).

 rodzic(franciszek, maria).
 rodzic(wanda, bogdan).
 rodzic(jan, krzysztof).
 rodzic(maria, krzysztof).
 rodzic(jan, wojciech).
 rodzic(maria, wojciech).
 rodzic(wanda, bogdan).
 rodzic(bogdan, zofia).
 rodzic(anna, zofia).
 rodzic(bogdan, ewa).
 rodzic(anna, ewa).
 rodzic(wojciech, katarzyna).
 rodzic(wojciech, robert).
 rodzic(zofia, katarzyna).
 rodzic(zofia, robert).

  %RULES
  %matka
  matka(M, D):- kobieta(M), rodzic(M, D).
  %ojciec
  ojciec(O, D):-mezczyzna(O), rodzic(O, D).
  %babcia
  babcia(B, D):-kobieta(B), rodzic(B, Y), rodzic(Y, D).
  %dziadek
  dziadek(S, D):-mezczynza(S), rodzic(S, Y), rodzic(Y, D).
  %siostra
  siostra(S, X):-kobieta(S), rodzic(Z, S), rodzic(Z, X), S\=X.
  %brat
  brat(B, X):-mezczyzna(B), rodzic(Z, B), rodzic(Z, X), B\=X.
  %syn
  syn(Z, S):-mezczynza(S), rodzic(Z, S).
  %córka
  corka(Z, C):-kobieta(C), rodzic(Z, C).
  %przodek
  przodek(Z, X):-rodzic(Z, X).
  przodek(Z, X):-rodzic(Z, P), przodek(P, X).
  %potomek
  potomek(X, Y):-rodzic(Z, X), potomek(Z, Y).
  potomek(X, Y):-rodzic(Y, X).
  %my own rule
  wnuk(X, W):-mezczyzna(W), rodzic(X, Y), rodzic(Y, W).