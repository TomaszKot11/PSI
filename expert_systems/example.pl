% Sentences from labs:
%  marek lubi kobiety ktore lubia kwiaty
%  joanna jest kobieta
%  joanna lubi kwiaty
%  czy marek lubi joanne?

%Facts
lubi_kobiety(marek).

lubi_kwiaty(joanna).

kobieta(joanna).
kobieta(julia).

%Rules
marek_lubi_kobiete(K):-lubi_kwiaty(K), kobieta(K).