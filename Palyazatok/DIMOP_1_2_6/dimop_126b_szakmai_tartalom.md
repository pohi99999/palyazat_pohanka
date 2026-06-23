# DIMOP Plusz-1.2.6/B-26  A fejlesztés szakmai tartalma

## Rövid EPTK-verzió
A projekt keretében a Pohánka és Társa Kft. bevezeti a Brunella Agent System (BAS) hibrid, multi-agent AI rendszert. A rendszer egy Node.js alapú orkesztrációs magból (Express.js, Socket.IO) és Python/FastAPI alapú adatfeldolgozó és automatizációs rétegből áll (Playwright robotkéz technológia, számlaadat- és bankkivonat-feldolgozás).
Fő szakmai/technológiai elemek:
1. Specializált autonóm ágensek együttműködő csapata (MAS), amelyek Vision-Language-Action képességgel közvetlenül kezelik az irodai szoftverek felületeit (Robotkéz).
2. LanceDB vektoradatbázisra épülő RAG (Retrieval-Augmented Generation) memória, amely a korábbi számlák és könyvelési döntések alapján javaslatot tesz a tételek kezelésére.
3. Phoenix Protocol v2 önjavító mechanizmus 5 másodperces heartbeat monitoringgal az üzemzavarok és adatvesztés elkerülésére.
4. Bifrost Gateway hibrid elérés a helyi (Ollama, qwen2.5-coder:7b) és felhős (Gemini, GPT-4o) modellek intelligens és költséghatékony kombinálására.
Beszerzendő infrastruktúra: 1 db GPU-val szerelt munkaállomás a helyi MI modellek futtatásához, 2 db irodai laptop/PC a kliensoldali használathoz, 1 db NAS és hálózati eszközök a biztonsági mentések és az adatbázis kiszolgálására. A szoftverlicencek és felhőszolgáltatások bevezetését külső IT tanácsadás és a 3 fős munkatársi gárda AI-asszisztált képzése támogatja.

---

## A fejlesztés rövid szakmai összefoglalása

A projekt keretében a Pohánka és Társa Kft. bevezeti a Brunella Agent System (BAS) nevű, hibrid, multiagent MIalapú rendszert, amely a könyvelési és adminisztratív munkafolyamatok digitalizálását és részleges automatizálását szolgálja. A megoldás egy modern, két rétegből álló architektúrán alapul:

- **Orkesztrációs réteg**: Node.js (TypeScript) alapú központi mag, amely Express.js és Socket.IO segítségével koordinálja az egyes munkafolyamatokat és autonóm ágenseket.
- **Adatfeldolgozó és automatizációs réteg**: Python/FastAPI alapú komponensek, amelyek Playwright segítségével automatizálják a webes felületek (pl. számlaküldő portálok, banki felületek) kezelését, valamint nagy mennyiségű adatot dolgoznak fel (számlaadatok, bankkivonatok, pénztármozgások).

## Fő technológiai komponensek

1. **MultiAgent rendszer (MAS)**  
   A BAS több, specializált, autonóm ügynökből áll (pl. Orchestrator, Developer, Evaluator, RobotkezV2), amelyek együttműködve végzik a könyvelési és adminisztratív feladatok előkészítését. A Robotkéz technológia VisionLanguageAction képességekkel rendelkezik, így képes a szoftverek grafikus felületét látni és emberhez hasonló módon kezelni (kattintások, mezőkitöltések, fájlfeltöltés).

2. **RAG és vektoros memória (LanceDB)**  
   A rendszer a LanceDB vektoradatbázist használja a korábbi számlák, bizonylatok és könyvelési döntések lekérdezésére. A RAG (RetrievalAugmented Generation) architektúra révén az MImodell a releváns múltbeli minták alapján javaslatot tud tenni a tételek könyvelési kezelésére (főkönyvi számlaszám, ÁFAkulcs, partnerhozzárendelés), így tanul a cég saját gyakorlatából.

3. **Phoenix Protocol v2  önjavító architektúra**  
   A Phoenix Protocol v2 a rendszer üzembiztosságát biztosító mechanizmus: folyamatos 5 másodperces livenessmonitoringot végez, és hiba esetén automatikusan újraindítja az érintett alrendszereket vagy visszaállítja az utolsó stabil állapotot. Ez különösen fontos a könyvelési folyamatoknál, ahol adatvesztés vagy hosszabb leállás nem megengedhető.

4. **Bifrost Gateway  hibrid MI modellelérés**  
   A Bifrost Gateway lehetővé teszi, hogy a rendszer intelligensen kombinálja a helyben futó (pl. Ollama, qwen2.5coder:7b) és a felhőben elérhető (Google Gemini, GPT4o) MImodelleket. Így a nagy adatvédelmi érzékenységű műveletek lokálisan, alacsony költséggel, míg a komplexebb feladatok felhőben futnak, optimalizálva az üzemeltetési költségeket.

## Folyamatok, amelyeket a BAS érint

- Bejövő számlák automatikus letöltése (Gmailmonitoring, csatolmányok mentése).  
- Számlaadatok kinyerése OCR + MI segítségével, strukturált adatformátummá alakítva.  
- NAV Online Számla adatok lekérdezése és egyeztetése.  
- Bankszámla- és pénztártételek automatikus párosítása a számlákhoz (reconciliation).  
- Könyvelési tételek előkészítése a használt könyvelőprogram számára (export fájl vagy API alapján).

## Hardver és infrastruktúra

A projekt során a következő infrastruktúra elemek kerülnek beszerzésre és üzembe állításra:

- 1 db GPUval szerelt munkaállomás a lokális MI modellek futtatásához.  
- 23 db korszerű irodai PC/laptop a BAS kliensoldali használatához.  
- NAS és hálózati eszközök (router, switch) a vektoradatbázis és biztonsági mentések kiszolgálására.  

Ezen felül felhőszolgáltatások (pl. Google Cloud) biztosítják a rendszer skálázhatóságát, a redundáns adatmentést és a monitorozási funkciókat.

A fenti szakmai tartalom megfelel a DIMOP Plusz-1.2.6/B-26 felhívás digitális infrastruktúra és transzformáció célrendszerének: hardver és szoftverfejlesztés, felhőalapú megoldások bevezetése, valamint digitális folyamatok kialakítása és automatizálása.
