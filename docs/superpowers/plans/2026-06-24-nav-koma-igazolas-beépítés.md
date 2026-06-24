# NAV KOMA igazolás beépítése Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Frissíteni a projekt dokumentumait a KOMA igazolás (KOMA - Pohánka Kft.pdf, kelte: 2026. 06. 23.) beérkezése alapján, majd beküldeni a módosításokat git-be.

**Architecture:** Manuális szerkesztések a projektleíró és teendőlistás Markdown fájlokban a KOMA igazolás státuszának frissítésére, majd a változások ellenőrzése és verziókezelése.

**Tech Stack:** Markdown, Git

---

### Task 1: DIMOP Mellékletek Checklist Frissítése

**Files:**
- Modify: `Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md:23-27`

- [ ] **Step 1: Módosítsd a 7. sorban található NAV KOMA státuszt**

Cseréld a következő sort:
```markdown
| 7. | NAV Nullás igazolás / KOMA státusz       | DIMOP       | NAV KOMA  köztartozásmentes adózói adatbázis             | [ ]     |
```
Erre a sorra:
```markdown
| 7. | NAV Nullás igazolás / KOMA státusz       | DIMOP       | KOMA - Pohánka Kft.pdf (NAV KOMA igazolás, 2026. 06. 23.) | [x]     |
```

- [ ] **Step 2: Ellenőrizd a táblázat formátumát**
Győződj meg róla, hogy a Markdown táblázat nem esett szét, a cellák elrendezése helyes maradt.

---

### Task 2: KELL.md emberi teendők frissítése

**Files:**
- Modify: `KELL.md:1-8`

- [ ] **Step 1: Frissítsd a NAV igazolás lekérésére vonatkozó pontot**

Cseréld a következő sort:
```markdown
1) NAV: köztartozás‑mentesség ("nullás") igazolás lekérése
```
Erre a sorra:
```markdown
1) [x] NAV: köztartozás‑mentesség ("nullás") igazolás lekérése (KOMA - Pohánka Kft.pdf elmentve, aktuális igazolás rendelkezésre áll)
```

---

### Task 3: TARTALOM.md dokumentumtérkép frissítése

**Files:**
- Modify: `TARTALOM.md:19-23`

- [ ] **Step 1: Egészítsd ki a docs mappa tartalmát a KOMA igazolással**

Cseréld ki a következő részt:
```markdown
- docs/
  - 2025-06-19_IG32095-2025_DII.pdf — DI igazolás és kapcsolódó vizsgálatok.
  - (további pdf/docx anyagok: ha vannak, itt találhatók)
```
Erre a részre:
```markdown
- docs/
  - 2025-06-19_IG32095-2025_DII.pdf — DI igazolás és kapcsolódó vizsgálatok.
  - KOMA - Pohánka Kft.pdf — NAV KOMA igazolás (köztartozásmentes adózói státusz igazolása a DIMOP és Széchenyi hitelhez, lekérdezve: 2026. 06. 23.)
  - (további pdf/docx anyagok: ha vannak, itt találhatók)
```

---

### Task 4: mesterdoc.md és mesterdoc-5.md frissítése

**Files:**
- Modify: `mesterdoc.md:84-88`
- Modify: `mesterdoc-5.md:84-88`

- [ ] **Step 1: Jelöld be a NAV Nullás igazolás meglétét a mesterdoc.md fájlban**

Cseréld ki a következő sort:
```markdown
*   [ ] NAV "Nullás" igazolás (vagy képernyőkép a köztartozásmentes adózói adatbázisról).
```
Erre a sorra:
```markdown
*   [x] NAV "Nullás" igazolás (vagy képernyőkép a köztartozásmentes adózói adatbázisról). Csatolva: KOMA - Pohánka Kft.pdf, érvényes a pályázat benyújtásakor (lekérdezve: 2026. 06. 23.).
```

- [ ] **Step 2: Jelöld be a NAV Nullás igazolás meglétét a mesterdoc-5.md fájlban**

Cseréld ki a következő sort:
```markdown
*   [ ] NAV "Nullás" igazolás (vagy képernyőkép a köztartozásmentes adózói adatbázisról).
```
Erre a sorra:
```markdown
*   [x] NAV "Nullás" igazolás (vagy képernyőkép a köztartozásmentes adózói adatbázisról). Csatolva: KOMA - Pohánka Kft.pdf, érvényes a pályázat benyújtásakor (lekérdezve: 2026. 06. 23.).
```

---

### Task 5: Git commit + push

**Files:**
- Git repository

- [ ] **Step 1: Ellenőrizd az állapotot és a módosításokat**
Futtasd: `git status`

- [ ] **Step 2: Add hozzá az összes módosított fájlt**
Futtasd: `git add .`

- [ ] **Step 3: Készíts egy commitot a változtatásokról**
Futtasd: `git commit -m "NAV KOMA igazolás (KOMA - Pohánka Kft.pdf) beépítve a DIMOP melléklet-listába és dokumentációba"`

- [ ] **Step 4: Pushold a változásokat a távoli repóba**
Futtasd: `git push origin main`
(Megjegyzés: Ha az ág neve nem main, hanem master, akkor arra az ágra pusholj.)
