Do uruchomienia algorytmu konieczny jest Python w wersji 2.7.1rc1+

Interfejs uruchomienia programu:

python GraphModifiedDFS.py test_file_3 35 N C

Kolejne argumenty uruchomienia:
Pierwszy: nazwa pliku wejściowego z grafem.
Drugi: z (Suma punktów na ścieżce z P do K)
Trzeci: Wierzchołek początkowy P
Czwarty: Wierzchołek końcowy K


Przypadek pierwszy:
python GraphModifiedDFS.py test_file_1 16 A C

OCZEKIWANY REZULTAT:
A(5) -> B(3) -> D(6) -> C(2)
(Obraz grafu w dokumentacji końcowej)


Przypadek drugi:
python GraphModifiedDFS.py test_file_2 25 A E

OCZEKIWANY REZULTAT:
Ścieżka nie istnieje
(Obraz grafu w dokumentacji końcowej)


Przypadek trzeci:
python GraphModifiedDFS.py test_file_3 57 N C

OCZEKIWANY REZULTAT:
N(2) -> X(16) -> H(1) -> Y(6) -> K(14) -> L(9) -> A(0) -> G(5) -> C(4)
(Obraz grafu w dokumentacji końcowej)




