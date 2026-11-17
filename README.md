Bumle Business

Introduktion
Vi har udviklet dette projekt på baggrund af virksomheden Bumle Business,
som ønsker bedre overvågning af deres VPN-forbindelser.

Virksomheden har oplevet mistænklig aktivitet på deres servere, og har derfor haft
behov for en løsning, der kunne hjælpe med at identificere en mulig trussel.

Formålet med projektet er at udvikle et Python-program, 
der kan indlæse og vise og analysere logdata fra filen cyber_security_log_sample.txt.

Programmet skal give brugeren et bedre overblik over logdataene gennem tabeller og forskellige diagrammer.
På den måde bliver det lettere at opdage mønstre, sammenhænge og mistænkelig aktivitet i logfilerne.


Scrum
I projektet har vi anvendt SCRUM som projektstyringsmetode. bla bla bla
Vi har gennemført projektet i ét sprint.

Vi har lavet seks user stories.
Indlæse logfilen i Python.
Gemme logdata og undgå dubletter.
Vise logdata i en overskuelig tabel.
Undersøge sammenhænge med scatter-plots.
Vise logdata i forskellige diagrammer.
Lave en menu, hvor brugeren kan vælge programmets funktioner.

Tasks
Vi har lavet Tasks til hver User Story. De beskriver de konkrete opgaver, 
vi skal udføre for at udvikle programmet.

Acceptkriterier
Vi har lavet acceptkriterier til hver User Story. 
De beskriver, hvad de forskellige funktioner skal kunne, før de er færdige.

Task Board
Vi har brugt et Task Board på Jira til at holde styr på vores opgaver.

Konklusion
3. Konklusion

I dette projekt har vi udviklet et Python-program til Bumle Business, der kan indlæse, vise og analysere VPN-logdata. Programmet har en menu, hvor brugeren kan vælge mellem en tabel over hele loggen, et søjlediagram over mislykkede loginforsøg pr. IP-adresse og et cirkeldiagram over fordelingen af log levels. Koden er delt op i flere filer, så indlæsning af data og de enkelte analyser er adskilt.

Det vigtigste resultat er, at diagrammerne gør det nemt at se mønstre, som er svære at finde i selve logfilen. Søjlediagrammet viser hurtigt, hvilke IP-adresser der har mange fejlede logins, hvilket kan være tegn på et brute force-angreb. Cirkeldiagrammet giver et overblik over, hvor mange af hændelserne der er almindelige informationer, advarsler eller fejl.

Vi har brugt SCRUM til at planlægge arbejdet i mindre opgaver og holde styr på, hvem der lavede hvad.

Programmet kan forbedres på flere måder. Det kan få bedre fejlhåndtering, så det ikke går ned ved ufuldstændige loglinjer. Det kan analysere, hvornår loginforsøgene sker, så man kan opdage mange fejl inden for kort tid. Det kan også give automatiske advarsler om mistænkelige IP-adresser og have flere filtreringsmuligheder.

Samlet set er programmet et godt udgangspunkt for at overvåge og analysere VPN-aktivitet.
