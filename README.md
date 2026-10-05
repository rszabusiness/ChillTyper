# ⌨ ChillTyper v5.3.3 - Magyar QWERTZ Vakírás Tanuló & Gyakorló

**ChillTyper** egy modern, böngészőben futó, interaktív tízujjas gépírás-oktató és -fejlesztő webalkalmazás, amely a **magyar QWERTZ billentyűzetkiosztás** alapjaira épül[cite: 3].

## ✨ Főbb Funkciók & Jellemzők

* **🇭🇺 Eredeti Magyar ISO QWERTZ Kiosztás**:
  * Teljes ékezetes támogatás (`é`, `á`, `í`, `ö`, `ü`, `ó`, `ő`, `ú`, `ű`)[cite: 3].
  * Színkódolt, ujjrend alapú billentyűzet-kiemelések[cite: 3].
  * Zárolt billentyűk fekete-fehér / szürke árnyalatos megjelenítése a kezdő szinten[cite: 3].

* **🖐️ Megnövelt Méretű & Kétformájú Kéz-Megjelenítő (ÚJ)**:
  * **28%-kal nagyobb méret**: Mindkét oldalon könnyen áttekinthető, nagy SVG kézfej segít a helyes ujjrend követésében.
  * **2 Választható Kézforma**:
    * **1. Realisztikus Kézfej (Kontúr)**: Elegáns anatómiai kézfej kontúr világító ujjhegyekkel.
    * **2. Minimalista Ujj-sávok (Színes)**: A billentyűzet ujj-színeivel harmonizáló sávos korong-jelölők.
  * **🖐️ Kéz Forma Váltó Gomb**: A felső menüsorban egyetlen kattintással azonnal váltani lehet a 2 vizuális stílus között.

* **⚙️ 25 Egyedi Téma & Állítható Betűméret**:
  * Választható témák: *Serika Dark*, *Cyberpunk*, *Matrix*, *Dracula*, *Nord*, *Catppuccin*, *Retro*, *Vaporwave*, *Paper*, *Monokai*, *Coffee*, *Botanical*, *Gruvbox*, *Tokyo Night*, *Sunset*, *Ocean*, *Rosé Pine*, *Stealth*, *Solarized Dark*, *Emerald*, *Miami Vice*, *Lavender*, *Cheesecake*, *Matcha*, *Crimson*[cite: 3].
  * **🔠 Betűméret-választó**: Kicsi, Közepes (alapértelmezett), Nagy és Extra Nagy nézet dinamikusan igazodó sormagassággal[cite: 3].

* **🔤 Intelligens Szövegmegjelenítés**:
  * **Soha sincs elvágott szó**: A szavak törhetetlen blokkként (`whitespace-nowrap`) jelennek meg, így a böngésző a teljes szót hiánytalanul helyezi át a következő sorba[cite: 3].
  * **Visszatörlés (Backspace) támogatás**: Elgépelés esetén a `Backspace` gombbal visszaléphetsz és javíthatod az adott karaktert[cite: 3].
  * **Élő kurzor és hiba-visszajelzés**: Piros felvillanó animáció és virtuális billentyűzet-kiemelés hibás leütéskor[cite: 3].

* **📊 Részletes Eredmény- és Statisztikai Elemzés**:
  * **WPM** (Szó / perc) és **CPM** (Karakter / perc) nyers és tiszta értékek[cite: 3].
  * **Pontosság (%)** és egyenletességi mutató (**Consistency %**)[cite: 3].
  * **Leggyakrabban hibázott billentyűk** részletes kimutatása[cite: 3].

* **⌨️ Billentyűzet Navigáció**:
  * `Tab` - A teszt vagy kör azonnali újraindítása[cite: 3].
  * `Enter` - Továbbhaladás a szintteljesítési és statisztikai ablakokból[cite: 3].
  * A `Space` gomb kizárólag szóköz beírására szolgál, nem lépteti vissza a játékot és nem nyomja meg a fókuszban lévő gombokat[cite: 3].

## 🎮 Játékmódok

### 1. 🌱 Kezdő Szintek (47 Feloldható Szint)[cite: 3]
* **Izommemória építés**: Lépésről lépésre tanítja meg a billentyűket kezdve az `F`, `J` és `Szóköz` gomboktól[cite: 3].
* **Pontossági feltétel**: Legalább **90%-os pontosság** szükséges a következő szint feloldásához[cite: 3].
* **Cél-leütésszám**: A szint zárásához megadott számú helyes leütést kell összegyűjteni (pl. `60 / 60`)[cite: 3]. Hibás leütés esetén a számláló nem változik[cite: 3].
* **Új billentyű kijelzés**: Minden szint elején kiemelve látható az újonnan feloldott karakter és a hozzá tartozó ujj (pl. `D - Bal középső ujj`)[cite: 3].

### 2. ⚡ Haladó Mód (Mért Teszt)[cite: 3]
* **Stopper alapú mérés**: Az első billentyűleütésre indul a stopper[cite: 3].
* **Választható szöveghossz**: `10`, `25`, `50` vagy `100` szavas tesztek[cite: 3].
* **Részletes záró kiértékelés**: Statisztikai ablak WPM, CPM, pontosság és ritmus-stabilitás mutatókkal[cite: 3].

### 3. 💬 Mondatok Mód[cite: 3]
Három különálló al-mód a sokoldalú gyakorláshoz[cite: 3]:
1. **📝 Szavak**: Meghatározott szószámú szövegek (`10`, `25`, `50`, `100` szó)[cite: 3].
2. **💬 Idézetek**: Közismert magyar idézetek és közmondások három hosszúságban[cite: 3]:
   * 🐣 **Rövid**[cite: 3]
   * 🐥 **Közepes**[cite: 3]
   * 🦅 **Hosszú**[cite: 3]
3. **⏱️ Időmérés**: Klasszikus visszaszámláló teszt választható időtartammal: `15s`, `30s`, `60s`, `120s`[cite: 3].

## 🛠 Technikai Részletek

* **Egyszerű asztali alkalmazás**: A Python-indító az önálló HTML-felületet asztali ablakban futtatja, és önálló EXE-vé csomagolható[cite: 3].
* **Külső Függőségek**: Tailwind CSS (CDN), Google Fonts (Plus Jakarta Sans, JetBrains Mono, Orbitron, VT323, Space Grotesk, Courier Prime, Fredoka)[cite: 3].
* **Adattárolás**: A témát, a betűméretet, a feloldott legmagasabb szintet és az aktuális kezdőszint részfeladatait tartósan elmenti[cite: 3]. Bezárás után az utolsó gépelt karaktertől folytatható[cite: 3]. Windows alatt az adatok a `%LOCALAPPDATA%\ChillTyper\webview` mappába kerülnek[cite: 3].

*ChillTyper v5.3.3 • Magyar QWERTZ Vakírás Oktató Program © 2026*[cite: 3]