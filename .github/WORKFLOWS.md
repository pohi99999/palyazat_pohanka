# GitHub Actions Munkafolyamatok — Pályázati Projekt

## Opcionális Automatizálás (Javasolt)

### 1. **Melléklet-validálás előtti PR**
Automatikusan ellenőrzi, hogy az összes szükséges melléklet dokumentálva van-e a `dimop_126b_mellekletek_checklist.md` fájlban.

```yaml
name: Melléklet Checklist Validáció
on: [pull_request, push]
jobs:
  validate:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: PowerShell melléklet-ellenőrzés
        run: |
          $ErrorActionPreference = "Stop"
          & ".\scripts\check_mellekletek.ps1"
```

### 2. **EPTK-verzió blokk integritása**
Ellenőrzi, hogy minden pályázati dokumentumban megtalálható az "## Rövid EPTK-verzió" szekció.

```yaml
name: EPTK-verzió Integritás
on: [pull_request, push]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: EPTK szekció validáció
        run: |
          grep -l "## Rövid EPTK-verzió" Palyazatok/DIMOP_*/*.md || {
            echo "HIBA: EPTK-verzió blokk hiányzik!"
            exit 1
          }
```

### 3. **Mesterdokumentum Frissítési Emlékeztetõ**
PR lezárásakor emlékeztetõ, hogy az `mesterdoc.md` frissítve lett-e.

```yaml
name: Mesterdokumentum Emlékeztetõ
on: [pull_request]
jobs:
  remind:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Mesterdoc módosítás ellenőrzés
        run: |
          git diff main...HEAD --name-only | grep -q "mesterdoc.md" || {
            echo "⚠️ FIGYELEM: mesterdoc.md nem módosult!"
            exit 0
          }
```

### 4. **Git Commit Linter (Opcionális)**
Ellenőrzi, hogy a commit üzenet felmarad-e az "Co-authored-by: Copilot" trailernek.

```yaml
name: Commit Üzenet Validáció
on: [pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Copilot trailer ellenőrzés
        run: |
          git log main...HEAD --pretty=format:%B | grep -q "Co-authored-by: Copilot" || echo "⚠️ Javasolt: Co-authored-by trailer hiányzik"
```

## Beállítás

1. Hozz létre egy `.github/workflows/` könyvtárat:
   ```bash
   mkdir -p .github/workflows
   ```

2. Másold a fenti `.yml` fájlokat a workflows könyvtárba.

3. Push-olj a main-re — a GitHub automatikusan aktiválja az Actions-okat.

## Letiltás/Módosítás

- Az egyes workflow-kat könnyedén letilthatod a GitHub Actions fülön.
- Csak az abszolút szükséges validációkat add hozzá — ez nem szoftver projekt.

## Kapcsolódó Dokumentumok

- [Melléklet checklist](../Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md)
- [Operatív Akciótev](../akcio_terv.md)
- [PowerShell validáció](../scripts/check_mellekletek.ps1)
