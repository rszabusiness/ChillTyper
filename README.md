# ⌨️ ChillTyper - Magyar QWERTZ Vakírás Tanuló & Gyakorló Program

A **ChillTyper** egy modern, interaktív és letisztult magyar vakírás-oktató webes alkalmazás. Segítségével lépésről lépésre, izommemóriára építve tanulhatsz meg tíz ujjal gépelni a standard magyar QWERTZ billentyűzetkiosztáson.

---

## ✨ Főbb Jellemzők

* **🇭🇺 Eredeti Magyar ISO QWERTZ Kiosztás**: Helyes ujjrend-hozzárendelésekkel és az összes magyar ékezetes billentyűvel (`é`, `á`, `í`, `ö`, `ü`, `ó`, `ő`, `ú`, `ű`).

* **🧩 47 Lépcsőfokos Tanösvény (1 új betű / szint)**:
  * **1. Szint**: Alappozíció (`F`, `J`, `Szóköz`).
  * **2–47. Szint**: Minden egyes szint pontosan **1 új karaktert** nyit fel és gyakoroltat be fokozatosan.

* **🎯 Izommemória-alapú Leütési Célok**: Kezdő szinten fix leütésszám (pl. 128 leütés) összegyűjtése a cél, ami a magasabb szinteken fokozatosan skálázódik.

* **📏 Szigorú ≥90%-os Pontossági Szabály**: A következő szintre kizárólag legalább **90%-os gépelési pontossággal** lehet továbblépni.

* **⌨️ Sorfolytonos Befejezés**: A leütési cél elérésekor nem szakad meg hirtelen a gépelés; a megkezdett sor végigírható, és a sor legvégén történik meg az ellenőrzés.

* **🔤 3 Betűs Blokkok**: A gyakorlósorok kizárólag szabályos, 3 karakteres csoportokból és szóköztörésekből állnak (pl. `fjf jff fff jfj`).

* **↵ Gyors Továbbhaladás Enterrel**: A szintválasztó és újrapróbálkozási ablakokban elég az `Enter` billentyűt megnyomni a következő szint azonnali indításához.

* **🎮 Új Játék Gomb**: Bármikor újraindíthatod az aktuális kört tiszta statisztikákkal és friss gyakorlósorokkal anélkül, hogy elveszítenéd a feloldott szintjeidet.

* **🎨 Responsive UI & Beépített SVG Favicon**: Kijelzőmérethez igazodó, megnövelt billentyűzet és szövegméretek, beépített dinamikus böngészőikonnal.

---

## 💬 Játékmódok

### 1. 🌱 Kezdő Mód (Dinamikus Cél)
* Szintről szintre nyitja fel a karaktereket.
* Élő haladási sáv és valós idejű pontosságkijelzés.
* Megadott leütési célok teljesítése szükséges a tovablépéshez.

### 2. ⚡ Haladó Mód (Mért Idő)
* Nyomon követi a percenkénti leütésszámot (**CPM**), a percenkénti szószámot (**WPM**), a pontosságot és az eltelt időt.

### 3. 💬 Mondat Mód (Kötetlen Gyakorlás)
* **Összes gomb feloldva**: Nem igényel szinteket, a teljes magyar billentyűzet azonnal elérhető (a szintválasztó automatikusan elrejtődik).
* Háromsoros elrendezésben generál értelmes magyar mondatokat.
* **🎨 Gépelési Animáció & Betűtípus Választó**: A keret jobb felső sarkában 4-féle vizuális effekttel és hozzájuk illő egyedi betűtípussal teheted látványossá a mondatokat:
  * ⚡ **Villám Pulzus**: *Space Grotesk* betűtípus, pulzáló fénnyel.
  * ✨ **Neon Cyber**: *Orbitron* sci-fi betűtípus, neon fénnyel és magenta/cián effekttel.
  * 🎈 **Pop & Ugrás**: *Fredoka* játékos, lekerekített betűtípus, ugráló animációval.
  * 📟 **Terminál**: *VT323* retró mátrix/terminál pixeles betűtípus, villogó kurzorral.

---

## 🏆 Kitüntetések (Badges System)

A **Mondat Mód** teljesítményeit a rendszer automatikusan kitüntetésekkel jutalmazza:

| İkon | Kitüntetés Neve | Feltétel / Leírás |
| :---: | :--- | :--- |
| 🐢 | **Kezdő Tempó** | Érj el 15 WPM (75 CPM) sebességet |
| 🏃 | **Mágus Író** | Érj el 30 WPM (150 CPM) sebességet |
| ⚡ | **Villám Gépíró** | Érj el 50 WPM (250 CPM) sebességet |
| 🚀 | **Hangsebesség** | Érj el 70 WPM (350 CPM) sebességet |
| 🎯 | **Pontos Szem** | Minimum 95%-os pontosság egy körben |
| 💎 | **Tökéletes Kéz** | 100%-os hibátlan gépelés egy körben |
| 💬 | **Mondat Mester** | Legalább 3 teljes mondat teljesítése |
| 🏆 | **Maratoni Író** | Legalább 12 teljes mondat teljesítése |

---

## ⌨️ Ujjrendi Kiosztás (Finger Mapping)

| Ujj | Színkód | Példa Billentyűk |
| :--- | :--- | :--- |
| **Bal kisujj** | Rózsaszín / Piros | `1`, `Q`, `A`, `Y`, `Í` |
| **Bal gyűrűsujj** | Narancssárga | `2`, `W`, `S`, `X` |
| **Bal középső ujj** | Sárga | `3`, `E`, `D`, `C` |
| **Bal mutatóujj** | Zöld | `4`, `5`, `R`, `T`, `F`, `G`, `V`, `B` |
| **Jobb mutatóujj** | Ciánkék | `6`, `7`, `Z`, `U`, `H`, `J`, `N`, `M` |
| **Jobb középső ujj** | Kék | `8`, `I`, `K`, `,` |
| **Jobb gyűrűsujj** | Lila | `9`, `O`, `L`, `.` |
| **Jobb kisujj** | Rózsaszín | `0`, `Ö`, `Ü`, `Ó`, `P`, `Ő`, `Ú`, `É`, `Á`, `Ű`, `-` |
| **Hüvelykujjak** | Szürke | `Szóköz` (Space) |

---

## 🛠️ Használt Technológiák

* **HTML5 / ES6+ Vanilla JavaScript**: Keretrendszer-független, gyors és önálló kód.
* **Tailwind CSS**: Modern, üveghatású (glassmorphism) és reszponzív felület.
* **Google Fonts**: *Plus Jakarta Sans*, *JetBrains Mono*, *Space Grotesk*, *Orbitron*, *Fredoka*, *VT323*.
* **Web Audio API**: Szintetizált gépelési és siker-hangeffektek audio fájlok letöltése nélkül.
* **LocalStorage**: Automatikus helyi mentés a feloldott szintekről, beállításokról és kitüntetésekről.

---

## 💻 Használat és Indítás

1. Mentsd el az `index.html` fájlt a számítógépedre.
2. Nyisd meg dupla kattintással tetszőleges böngészőben (Chrome, Edge, Firefox, Safari).
3. Helyezd az ujjaidat az **F** és **J** alapbillentyűkre, nyomd meg az **Új játék** gombot, és kezdd el a gépelést!

---
*ChillTyper • Magyar QWERTZ Vakírás Oktató Program*