# ⌨ ChillTyper v4.9.9 - Magyar QWERTZ Vakírás Tanuló & Gyakorló

**ChillTyper** egy modern, böngészőben futó, interaktív tízujjas gépírás-oktató és -fejlesztő webalkalmazás, amely a **magyar QWERTZ billentyűzetkiosztás** alapjaira épül.

## ✨ Főbb Funkciók & Jellemzők

* **🇭🇺 Eredeti Magyar ISO QWERTZ Kiosztás**:

  * Teljes ékezetes támogatás (`é`, `á`, `í`, `ö`, `ü`, `ó`, `ő`, `ú`, `ű`).

  * Színkódolt, ujjrend alapú billentyűzet-kiemelések.

  * Zárolt billentyűk fekete-fehér / szürke árnyalatos megjelenítése a kezdő szinten.

* **⚙️ 25 Egyedi Téma & Állítható Betűméret**:

  * Választható témák: *Serika Dark*, *Cyberpunk*, *Matrix*, *Dracula*, *Nord*, *Catppuccin*, *Retro*, *Vaporwave*, *Paper*, *Monokai*, *Coffee*, *Botanical*, *Gruvbox*, *Tokyo Night*, *Sunset*, *Ocean*, *Rosé Pine*, *Stealth*, *Solarized Dark*, *Emerald*, *Miami Vice*, *Lavender*, *Cheesecake*, *Matcha*, *Crimson*.

  * **🔠 Betűméret-választó**: Kicsi, Közepes (alapértelmezett), Nagy és Extra Nagy nézet dinamikusan igazodó sormagassággal.

* **🔤 Intelligens Szövegmegjelenítés**:

  * **Soha sincs elvágott szó**: A szavak törhetetlen blokkként (`whitespace-nowrap`) jelennek meg, így a böngésző a teljes szót hiánytalanul helyezi át a következő sorba.

  * **Visszatörlés (Backspace) támogatás**: Elgépelés esetén a `Backspace` gombbal visszaléphetsz és javíthatod az adott karaktert.

  * **Élő kurzor és hiba-visszajelzés**: Piros felvillanó animáció és virtuális billentyűzet-kiemelés hibás leütéskor.

* **📊 Részletes Eredmény- és Statisztikai Elemzés**:

  * **WPM** (Szó / perc) és **CPM** (Karakter / perc) nyers és tiszta értékek.

  * **Pontosság (%)** és egyenletességi mutató (**Consistency %**).

  * **Leggyakrabban hibázott billentyűk** részletes kimutatása.

* **⌨️ Billentyűzet Navigáció**:

  * `Tab` - A teszt vagy kör azonnali újraindítása.

  * `Enter` - Továbbhaladás a szintteljesítési és statisztikai ablakokból.

  * A `Space` gomb kizárólag szóköz beírására szolgál, nem lépteti vissza a játékot és nem nyomja meg a fókuszban lévő gombokat.

## 🎮 Játékmódok

### 1. 🌱 Kezdő Szintek (47 Feloldható Szint)

* **Izommemória építés**: Lépésről lépésre tanítja meg a billentyűket kezdve az `F`, `J` és `Szóköz` gomboktól.

* **Pontossági feltétel**: Legalább **90%-os pontosság** szükséges a következő szint feloldásához.

* **Cél-leütésszám**: A szint zárásához megadott számú helyes leütést kell összegyűjteni (pl. `60 / 60`). Hibás leütés esetén a számláló nem változik.

* **Új billentyű kijelzés**: Minden szint elején kiemelve látható az újonnan feloldott karakter és a hozzá tartozó ujj (pl. `D - Bal középső ujj`).

### 2. ⚡ Haladó Mód (Mért Teszt)

* **Stopper alapú mérés**: Az első billentyűleütésre indul a stopper.

* **Választható szöveghossz**: `10`, `25`, `50` vagy `100` szavas tesztek.

* **Részletes záró kiértékelés**: Statisztikai ablak WPM, CPM, pontosság és ritmus-stabilitás mutatókkal.

### 3. 💬 Mondatok Mód

Három különálló al-mód a sokoldalú gyakorláshoz:

1. **📝 Szavak**: Meghatározott szószámú szövegek (`10`, `25`, `50`, `100` szó).

2. **💬 Idézetek**: Közismert magyar idézetek és közmondások három hosszúságban:

   * 🐣 **Rövid**

   * 🐥 **Közepes**

   * 🦅 **Hosszú**

3. **⏱️ Időmérés**: Klasszikus visszaszámláló teszt választható időtartammal: `15s`, `30s`, `60s`, `120s`.

## 🛠 Technikai Részletek

* **Egyszerű asztali alkalmazás**: A Python-indító az önálló HTML-felületet asztali ablakban futtatja, és önálló EXE-vé csomagolható.

* **Külső Függőségek**: Tailwind CSS (CDN), Google Fonts (Plus Jakarta Sans, JetBrains Mono, Orbitron, VT323, Space Grotesk, Courier Prime, Fredoka).

* **Adattárolás**: A témát, a betűméretet, a feloldott legmagasabb szintet és az aktuális kezdőszint részfeladatait tartósan elmenti. Bezárás után az utolsó gépelt karaktertől folytatható. Windows alatt az adatok a `%LOCALAPPDATA%\ChillTyper\webview` mappába kerülnek.

*ChillTyper v4.9.9 • Magyar QWERTZ Vakírás Oktató Program © 2026*