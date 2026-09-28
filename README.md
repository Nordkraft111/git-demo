# Git-demo — Tema 2

En selvstændig øvelse i Git, GitHub, HTML og CSS. Siden kan åbnes direkte ved at dobbeltklikke på `index.html`.

## Det faktiske forløb

Codex oprettede og ændrede projektet den 28. september 2026 efter Magnus' ønske. De tre commits er faktiske snapshots, lavet i denne rækkefølge med den eksisterende Git-identitet på computeren. Datoerne er ikke ændret. Historikken dokumenterer kodeændringerne, ikke at Magnus selv har klikket gennem øvelsen i PhpStorm.

1. **Første version**: `index.html` med overskriften “Mit første Git-projekt” og et kort tekstafsnit. `.gitignore` indeholder `.idea/`.
2. **Tilføjet velkomsttekst**: overskriften ændres til “Velkommen til mit Git-projekt”, og der tilføjes et velkomstafsnit.
3. **Bygget responsiv portfolio og dokumenteret Git-øvelsen**: siden udbygges til en enkel portfolio med separat CSS, en dokumenteret AI-prompt og kontrolvejledning.

Den fulde prompt og gennemgangen står i `PROMPT.md`. Portfolioen er en studieøvelse med links til to eksisterende projekter. Den er ikke en ny kommerciel hjemmeside.

## Git-begreber med dette projekt som eksempel

- **Repository**: projektets filer sammen med Git-historikken i den skjulte `.git`-mappe.
- **Working tree**: de filer, man har åbne og redigerer. En gemt fil er ikke automatisk et commit.
- **Staging area**: de ændringer, man har valgt til næste commit med `git add`.
- **Commit**: et gemt snapshot af de valgte filer med en besked og et ID. De tidligere versioner kan sammenlignes med den nye.
- **Branch**: en navngivet udviklingslinje. Denne øvelse bruger `main`.
- **GitHub**: en onlinetjeneste til blandt andet Git-repositorier. Git er værktøjet, mens GitHub er en mulig vært for en kopi.
- **Remote**: en navngivet adresse til et andet repository, ofte `origin`.
- **Push**: sender lokale commits til en remote. Et lokalt commit er ikke i sig selv lagt på GitHub.
- **Clone**: henter en kopi af et repository inklusive historikken.
- **`.gitignore`**: angiver filer, Git normalt ikke skal begynde at spore. `.idea/` holder PhpStorms projektindstillinger ude. Den fjerner ikke automatisk filer, som allerede er tracked.

## Magnus' gennemgang i PhpStorm

1. Åbn mappen `git-demo` som projekt. Kontrollér, at Git registreres, og at branchen er `main`.
2. Åbn Git-vinduets log. Find de første to commits og se forskellen i `index.html`: ændret overskrift og et nyt afsnit.
3. Se tredje commit og gennemgå HTML-strukturen og CSS-filen. Prøv selv at forklare, hvad `header`, `nav`, `main`, `section` og medieforespørgslen gør.
4. Åbn `index.html` i browseren. Prøv en smal visning, tryk Tab gennem links, og brug “Gå til indhold”.
5. Lav eventuelt selv en lille, men meningsfuld ændring, se forskellen i PhpStorm og lav et nyt commit med en forklarende besked. De oprindelige commits behøver ikke ændres.
6. Åbn https://github.com/Nordkraft111/git-demo og sammenhold filer og commit-historik med det lokale projekt. Repositoriet er publiceret 28. september 2026; det er dette særskilte link, der hører til GitHub-øvelsen. RED SEA READY-repositoriet er en anden opgave.

## Kontrol

Fra projektmappen kan grundkontrollen køres uden ekstra Python-pakker:

```sh
python3 check.py
```

Kontrollen undersøger blandt andet interne links, overskriftshierarki, nødvendige filer, `.gitignore` og — når den er til stede — de første to versioner i Git-historikken. Den erstatter ikke en visuel eller faglig gennemgang. I ZIP-udgaven er Git-historikken ikke med, og den del springes derfor over.

Git-loggen kan også læses med:

```sh
git log --oneline --reverse
git status
```

## ZIP og Git bundle

ZIP-filen indeholder den aktuelle kildekode og dokumentation uden `.git`. En separat `.bundle`-fil bevarer hele Git-historikken. En bundle kan åbnes som et nyt lokalt repository:

```sh
git clone git-demo-2026-09-28.bundle git-demo-kopi
```

Kommandoen køres i den mappe, hvor bundle-filen ligger. `git-demo-kopi` skal være en ny mappe.

## Afgrænsning og status

Publiceret 28. september 2026 på https://github.com/Nordkraft111/git-demo. Repositoriet er offentligt, origin peger på dette repository, og main er sendt til GitHub. De første tre commits er bevaret; en efterfølgende dokumentationscommit registrerer publiceringen. Ingen dataindsamling, eksterne pakker eller login er nødvendige for at åbne siden. Magnus' egen gennemgang og eventuelle øvelsestrin i PhpStorm er fortsat særskilte, ikke dokumenteret som gennemført. Intet er afleveret i Moodle.

PhpStorm 2026.2.2 har gennemført en automatiseret kodeinspektion via sin officielle kommandolinje med en HTML/CSS-profil. Resultatet indeholdt kun staveforslag, primært danske ord og tekniske navne. Inspektionen er en afgrænset teknisk kontrol og dokumenterer hverken Magnus' manuelle arbejde eller fuld fejlfrihed.
