# Mellékletek Sablon — VNT Pályázat

> **Útmutató:** Ez a checklist a tipikus VNT pályázati mellékleteket tartalmazza táblázatos formában. A `docs/` mappában a jelölt dokumentumok **mintafájlként rendelkezésre állnak** Pohánka és Társa Kft. adataival. Minden új pályázatnál ellenőrizd és frissítsd a **dátumot, érvényességet és az aktuális fájlnevet** a `<!-- FIXME -->` jelölések mentén. Az automatizált validáláshoz futtasd: `powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1`

---

## 1. Cég- és Jogi Dokumentumok

| # | Dokumentum | Aktuális mintafájl (`docs/`) | Érvényesség / Megjegyzés | Státusz |
|:---:|:---|:---|:---|:---:|
| 1 | Friss cégkivonat | `Cegkivonat-7.pdf` | <!-- FIXME: Max. 30 napnál nem régebbi benyújtáskor --> | [ ] |
| 2 | Aláírási címpéldány / aláírás-minta | `Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf` | — | [ ] |
| 3 | Átláthatósági nyilatkozat | `Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf` (részét képezi) | — | [ ] |
| 4 | KKV-minősítési nyilatkozat | `Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf` (részét képezi) | Ellenőrizd: Pohánka = mikrovállalkozás | [ ] |
| 5 | Társasági szerződés / alapító okirat | Cégkapu / cégbíróság | <!-- FIXME: Beszerezni, ha a pályázat kötelezővé teszi --> | [ ] |

---

## 2. Pénzügyi Dokumentumok (Utolsó 3 Lezárt Év)

| # | Dokumentum | Aktuális mintafájl (`docs/`) | Érintett év | Státusz |
|:---:|:---|:---|:---:|:---:|
| 6 | 2023. évi beszámoló (mérleg + eredménykimutatás) | `2023.-beszamolo-10.pdf` | 2023 | [ ] |
| 7 | 2024. évi beszámoló | `2024.-beszamolo-2.pdf` | 2024 | [ ] |
| 8 | 2025. évi mérleg / beszámoló | `2025-evi-merleg-4.pdf` | 2025 | [ ] |
| 9 | 2023. évi főkönyvi kivonat | `2023.-fokonyv.pdf` | 2023 | [ ] |
| 10 | 2024. évi főkönyvi kivonat | `2024.-fokonyv-3.pdf` | 2024 | [ ] |
| 11 | 2025. évi főkönyvi kivonat | `2025.-fokonyv-5.pdf` | 2025 | [ ] |
| 12 | Aktuális törtidőszaki főkönyvi kivonat | <!-- FIXME: Ha rendelkezésre áll --> | Folyó év | [ ] |

> **FIXME:** Ha a pályázat benyújtásakor a legutóbbi lezárt év már más (pl. 2026), frissítsd a táblázatot a legfrissebb 3 évvel és adj hozzá új PDF fájlnevet.

---

## 3. Adó- és Megbízhatósági Igazolások

| # | Dokumentum | Aktuális mintafájl (`docs/`) | Kiállító | Érvényesség | Státusz |
|:---:|:---|:---|:---|:---|:---:|
| 13 | NAV köztartozásmentes igazolás (KOMA / „nullás") | `KOMA-Pohanka-Kft-8.pdf` | NAV | <!-- FIXME: Frissítsd benyújtás előtt (max. 30 nap) --> | [ ] |
| 14 | Helyi iparűzési adó igazolás (HIPA) | `SKM_4050260625124300-9.pdf` | Zalaegerszeg Önkormányzata | <!-- FIXME: Frissítsd benyújtás előtt --> | [ ] |
| 15 | NAV megbízható adózói státusz | NAV törzsfelületről (KOMA-ba foglalva) | NAV | — | [ ] |

> **FIXME:** Az igazolások tipikusan 30–90 napig érvényesek. Mindig ellenőrizd a kiállítás dátumát a benyújtás napjához képest.

---

## 4. Digitális Intenzitás és DFK Dokumentumok

| # | Dokumentum | Aktuális mintafájl (`docs/`) | Azonosító | Megjegyzés | Státusz |
|:---:|:---|:---|:---|:---|:---:|
| 16 | Vállalati DI igazolás (alacsony szint) | `2025-06-19_IG32095-2025_DII.pdf` | IG32095-2025 | 10 pont — digitális lemaradás igazolása | [ ] |
| 17 | Közösségi DI igazolás (magas szint) | `2025-06-19_IG32096-2025_RCR13-2.pdf` | IG32096-2025 | 8 pont — szektoros referencia | [ ] |
| 18 | GINOP DFK Támogatói Okirat | `palyazat_ginop_1-3.pdf` | D127/23-505/2025 | In-kind DFK szakértői támogatás (100%, önerő nélkül) | [ ] |
| 19 | Digitális Fejlesztési Koncepció (DFK) | <!-- FIXME: `DFK.pdf` a docs/ mappában, ha elkészült --> | — | DFK szolgáltató által kiállított végleges dokumentum | [ ] |

> **FIXME:** A DFK dokumentum csak a DFK folyamat lezárása után érhető el. Benyújtás előtt ellenőrizd, hogy `docs/DFK.pdf` fájl létezik-e.

---

## 5. Projekt-Specifikus Mellékletek

| # | Dokumentum | Forrás | Megjegyzés | Státusz |
|:---:|:---|:---|:---|:---:|
| 20 | Projekt indokoltsága | `Palyazatok/[FIXME: PÁLYÁZAT]/..._projekt_indokoltsag.md` | Az EPTK-verzió blokkot másold be az online felületre | [ ] |
| 21 | Projekt céljai és eredményei | `Palyazatok/[FIXME: PÁLYÁZAT]/..._celok_es_eredmenyek.md` | — | [ ] |
| 22 | Szakmai tartalom | `Palyazatok/[FIXME: PÁLYÁZAT]/..._szakmai_tartalom.md` | Technikai architektúra leírás (BAS) | [ ] |
| 23 | Részletes költségvetés | `Palyazatok/[FIXME: PÁLYÁZAT]/..._koltsegvetes_es_indikatorok.md` | <!-- FIXME: Ellenőrizd az összeget --> | [ ] |

---

## 6. Árajánlatok

| # | Dokumentum | Min. darabszám | Megjegyzés | Státusz |
|:---:|:---|:---:|:---|:---:|
| 24 | Hardver árajánlat (workstation, PC, NAS) | 2–3 ajánlat | <!-- FIXME: Bekérni IT beszállítóktól --> | [ ] |
| 25 | Szoftver / BAS bevezetési árajánlat | 1–2 ajánlat | <!-- FIXME: Fejlesztői ajánlat --> | [ ] |
| 26 | Képzési szolgáltatás árajánlat | 1–2 ajánlat | <!-- FIXME: Tréning szolgáltató --> | [ ] |
| 27 | Felhőszolgáltatás árajánlat (opcionális) | 1 ajánlat | Google Cloud / Azure | [ ] |

> **FIXME:** Az árajánlatoknak a benyújtás napján érvényesnek kell lenniük. Tárold őket a `docs/` könyvtárban egységes névvel (pl. `arajanlat_hardver_1.pdf`).

---

## 7. Egyéb / Opcionális Mellékletek

| # | Dokumentum | Megjegyzés | Státusz |
|:---:|:---|:---|:---:|
| 28 | Megbízási szerződés (ha tanácsadót alkalmazol) | <!-- FIXME: Ha releváns --> | [ ] |
| 29 | Adatvédelmi szabályzat / DPIA | <!-- FIXME: Ha az AI rendszer személyes adatot kezel --> | [ ] |
| 30 | Referencia / esettanulmány | <!-- FIXME: Ha a pályázat pontot ad rá --> | [ ] |

---

## Melléklet Ellenőrzési Összesítő (Benyújtás Előtt)

```
KÖTELEZŐ ELLENŐRZÉSI PONTOK:
[ ] Futtasd: powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1
[ ] KOMA igazolás dátuma: max. 30 napnál nem régebbi
[ ] HIPA igazolás dátuma: max. 30 napnál nem régebbi
[ ] Cégkivonat dátuma: max. 30 napnál nem régebbi
[ ] DFK.pdf létezik-e a docs/ mappában?
[ ] Árajánlatok érvényesek-e (aktuális dátum)?
[ ] Minden fájl PDF formátumban van?
[ ] EPTK-verzió szövegek bemásolva az online felületre?
```

---

*Sablon alapja: `Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md` és `KELL.md`, 2026. június 26-i állapot.*
