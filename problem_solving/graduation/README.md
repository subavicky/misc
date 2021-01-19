

if we write down the possibilities,

==========
n = 2 

AA
AP
PA
PP

tot = 4		abs = 2

==========
n = 3

AAA(x)	PAA
AAP 	PAP
APA 	PPA
APP 	PPP

tot = 7		abs = 3

==========
n = 4

AAAA(x)	PPAA
AAAP 	PPAP
AAPA 	PPPA
AAPP 	PPPP
AAAA(x)	PPAA
AAAP(x) PPAP
AAPA 	PPPA
AAPP 	PPPP

tot = 13	abs = 6

And the list continues,

n	tot	abs
2	4	2
3	7	3
4	13	6
5	24	11
6	44	20
7	81	37
8	149	68

there is a pattern associated with both these numbers which is similar to fibonacci series but here three numbers has to be summed up instead of two.
For total, the series starts with 1, 1, 2 and goes on as 4, 7, 13, 24, ..
For absent, the series starts with 1, 0, 1 and goes on as 2, 3, 6, 11, ..
