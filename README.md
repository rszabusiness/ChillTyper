# ⌨️ ChillTyper - Magyar QWERTZ Vakírás Tanuló & Gyakorló

**ChillTyper** egy modern, böngészőben futó, interaktív gépírás-oktató webalkalmazás, amelynek célja, hogy lépésről lépésre tanítsa meg a tízujjas vakírást a **magyar QWERTZ billentyűzetkiosztás** alapján.

---

## ✨ Főbb Funkciók

- **Magyar QWERTZ Kiosztás**: Eredeti magyar billentyűzet-elrendezés az összes ékezetes karakterrel (`á`, `é`, `í`, `ó`, `ö`, `ő`, `ú`, `ü`, `ű`).
- **Ujjrendi Színkódolás**: A virtuális billentyűzeten minden billentyű az ahhoz rendelt ujj színével jelenik meg (8 ujj + hüvelykujjak).
- **Vizuális Segítség ("Melyik Ujj")**: Valós idejű útmutató mutatja, hogy az éppen leütendő karaktert melyik ujjaddal kell megnyomnod.
- **Fokozatos Karakter-Feloldás**: 47 egymásra épülő szint. Az `F`, `J` és `Szóköz` alapoktól indulva szintről szintre **egyetlen új karakter** oldódik fel.
- **Strict Pontossági Feltétel**: A következő szint feloldásához legalább **90%-os pontosság** szükséges.
- **Beépített Hanghatások (Web Audio API)**: Lágy gombnyomás hangok, hibajelzések és fanfárok külső audiófájlok nélkül (némítási opcióval).
- **Adatmentés (localStorage)**: A feloldott szintek, kitüntetések és statisztikák automatikusan elmentődnek a böngésződben.
- **Single-File Architektúra**: Nem igényel telepítést, node modult vagy build lépést — egyetlen `.html` fájlként fut a böngészőben.

---

## 🎮 Játékmódok

### 1. 🌱 Kezdő Mód (Dinamikus Cél)
- **Célja**: Nyomásmentes izommemória-építés.
- **Működése**: Nincs időkorlát vagy időmérés. Három sorban jelennek meg 3 betűs karakterblokkok.
- **Skálázódó leütési cél**: A szintek haladtával emelkedik a szükséges leütésszám (pl. 128 leütés az 1. szinten).
- **Sorfolytonosság**: A szint vége nem szakítja félbe a gépelést; mindig befejezheted az aktuális sort.

### 2. ⚡ Haladó Mód (Mért Idő)
- **Célja**: A gépelési sebesség és ritmus fejlesztése.
- **Működése**: Valós idejű statisztikákat mér:
  - **CPM** (Characters Per Minute / Leütés per perc)
  - **WPM** (Words Per Minute / Szó per perc)
  - **Pontosság** (%)
  - **Hibák száma**
  - **Eltelt idő**

### 3. 💬 Mondat Mód (Minden Betű Elérhető)
- **Célja**: Értelmes magyar mondatok szabad gyakorlása.
- **Működése**: Nem igényel feloldott szinteket, az összes magyar billentyű aktív. Három soros, keretbe illeszkedő elrendezésben generál véletlenszerű mondatokat.

---

## 🏆 Kitüntetések (Badges System)

A **Mondat Mód**-ban gépelve különféle sebességi, pontossági és kitartási kitüntetéseket szerezhetsz meg:

| İkon | Kitüntetés Neve | Feltétel / Leírás |
| :---: | :--- | :--- |
| 🐢 | **Kezdő Tempó** | Érj el 15 WPM (75 CPM) sebességet |
| 🏃 | **Mágus Író** | Érj el 30 WPM (150 CPM) sebességet |
| ⚡ | **Villám Gépíró** | Érj el 50 WPM (250 CPM) sebességet |
| 🚀 | **Hangsebesség** | Érj el 70 WPM (350 CPM) sebességet |
| 🎯 | **Pontos Szem** | Érj el legalább 95%-os pontosságot |
| 💎 | **Tökéletes Kéz** | 100% hibátlan gépelés egy körben |
| 💬 | **Mondat Mester** | Gépelj le legalább 3 teljes mondatsort |
| 🏆 | **Maratoni Író** | Gépelj le legalább 12 teljes mondatsort |

---

## ⌨️ Ujjrendi Kiosztás (Finger Mapping)

| Ujj | Színkód | Példa Billentyűk |
| :--- | :--- | :--- |
| **Bal kisujj** | Rózsaszín/Piros | `1`, `Q`, `A`, `Y`, `Í` |
| **Bal gyűrűsujj** | Narancssárga | `2`, `W`, `S`, `X` |
| **Bal középső ujj** | Sárga | `3`, `E`, `D`, `C` |
| **Bal mutatóujj** | Zöld | `4`, `5`, `R`, `T`, `F`, `G`, `V`, `B` |
| **Jobb mutatóujj** | Ciánkék | `6`, `7`, `Z`, `U`, `H`, `J`, `N`, `M` |
| **Jobb középső ujj** | Kék | `8`, `I`, `K`, `,` |
| **Jobb gyűrűsujj** | Lila | `9`, `O`, `L`, `.` |
| **Jobb kisujj** | Rózsaszín | `0`, `Ö`, `Ü`, `Ó`, `P`, `Ő`, `Ú`, `É`, `Á`, `Ű`, `-` |
| **Hüvelykujjak** | Szürke | `Szóköz` (Space) |

---

## 🛠️ Technológiai Háttér

- **HTML5 & Vanilla JavaScript (ES6+)**: Külső JS keretrendszerek nélkül.
- **Tailwind CSS (CDN)**: Modern, sötét tónusú, üveghatású (glassmorphism) felület.
- **Google Fonts**: *Plus Jakarta Sans* (felület) és *JetBrains Mono* (gépelési szöveg).
- **Web Audio API**: Belső szintetizált hangeffektek audio fájlok letöltése nélkül.

---

## 🚀 Használat és Indítás

1. Töltsd le vagy másold ki az `index.html` fájlt.
2. Nyisd meg a fájlt tetszőleges modern böngészőben (Chrome, Firefox, Edge, Safari).
3. Válaszd ki a kívánt játékmódot, és kezdd el a gépelést!

---

*ChillTyper &bull; Magyar QWERTZ Vakírás Oktató Program*