

\## DIMOP Plusz-1.2.6/B – adatlap szöveg (vázlat)



\### Projekt indokoltsága, kiinduló helyzet



A Pohánka és Társa Kft. mikrovállalkozás Zalaegerszegen, főként számviteli és könyvelési szolgáltatásokat nyújt, 16+ éves működési múlttal, stabil, pozitív saját tőkével és megbízható adózói minősítéssel. A vállalkozás digitális intenzitása a Modern Vállalkozások Programja keretében lefolytatott audit alapján 10 pontos, azaz “alacsony” szintű, ami indokolja a célzott digitalizációs beavatkozást. 



A könyvelési és adminisztratív folyamatok jelenleg nagyrészt manuálisak: a beérkező számlák jelentős részét kézzel rögzítik, a bankszámla- és pénztártételek egyeztetése időigényes, a dokumentumkezelés és riportolás több, részben nem integrált rendszerben történik. Ez a működés a növekvő ügyfélszám mellett kapacitáskorlátot, hibakockázatot és profitabilitási plafont eredményez. 



A pályázó célja, hogy a Brunella Agent System (BAS) hibrid, multi‑agent AI rendszer bevezetésével átfogó digitális transzformációt hajtson végre, és a manuális adminisztrációt nagy arányban automatizált, intelligens folyamatokra cserélje.



\*\*\*



\### Projekt célja



A projekt célja egy olyan integrált, AI‑alapú digitális infrastruktúra kiépítése, amely a Pohánka és Társa Kft. teljes könyvelési és adminisztratív értékláncát lefedi a számlabefogadástól a banki egyeztetésen át a NAV‑szinkronig. A Brunella Agent System bevezetésével a vállalkozás legalább 50%-kal kívánja csökkenteni az egy ügyfélre jutó manuális adatbevitelre fordított időt, miközben javítja a szolgáltatás minőségét és növeli a digitalizációs érettséget. 



Konkrét cél, hogy a beérkező számlák legalább 80%-a automatikusan, Gmail‑figyelés, OCR és AI alapú adatkinyerés segítségével kerüljön a könyvelési rendszerbe, a bankszámla- és pénztártételek minimum 70%-a pedig automatikus reconciliation folyamatokon fusson keresztül. A vállalkozás DI‑pontszáma a projekt lezárásáig az “alacsony” kategóriából a “közepes” szintre emelkedjen.



\*\*\*



\### A projekt szakmai tartalma, tevékenységek



A projekt keretében a vállalkozás a következő fejlesztési elemeket valósítja meg:  



1\. \*\*Hardver és hálózati infrastruktúra fejlesztése\*\*  

&#x20;  - GPU‑képes munkaállomás és korszerű irodai számítógépek beszerzése a BAS lokális futtatásához és fejlesztéséhez. 

&#x20;  - NAS és hálózati eszközök telepítése a vektoradatbázis és biztonságos adatmentés kiszolgálására.



2\. \*\*Brunella Agent System (BAS) bevezetése\*\*  

&#x20;  - Node.js alapú orkesztrációs mag, Python/FastAPI alrendszer és Playwright alapú “Robotkéz” modul bevezetése a könyvelői szoftverek és webes felületek automatizált kezelésére. 

&#x20;  - LanceDB vektoradatbázisra épülő RAG‑megoldás kialakítása, amely a számlák, bankkivonatok és korábbi döntések alapján támogatja az AI‑asszisztensek tanulását.

&#x20;  - Phoenix Protocol v2 önjavító mechanizmus élesítése folyamatos heartbeat‑monitoringgal és automatikus újraindítással.



3\. \*\*Felhőszolgáltatások és üzemeltetés\*\*  

&#x20;  - Felhőalapú erőforrások (pl. Google Cloud) igénybevétele a rendszer skálázható és biztonságos futtatásához, backup‑ és monitoringszolgáltatásokkal kiegészítve.



4\. \*\*Tanácsadás és képzés\*\*  

&#x20;  - Külső IT tanácsadó bevonása a rendszertervezéshez, biztonsági hardeninghez és folyamatoptimalizáláshoz. 

&#x20;  - Belső képzések szervezése a BAS mindennapi használatára, AI‑asszisztált munkavégzésre és digitális munkafolyamatokra. 



\*\*\*



\### Várható eredmények, indikátorok



\- A manuális számlaadat‑rögzítéssel töltött idő legalább 50%-kal csökken a projekt előtti bázisidőszakhoz képest (belső időmérési kimutatás alapján). 

\- A beérkező számlák minimum 80%-a automatikus Gmail‑figyelés + OCR + AI alapú folyamatokon keresztül kerül be a könyvelési rendszerbe. 

\- A bankszámla- és házipénztár tranzakciók legalább 70%-a automatikus egyeztető folyamatokon fut át. 

\- A rendszer éves rendelkezésre állása eléri a 99%-ot a Phoenix Protocol v2 önjavító mechanizmusnak köszönhetően. 

\- A DI‑pontszám az új audit során az “alacsony” szintről legalább “közepes” kategóriára javul. 



\*\*\*



\## Projekt szakmai összefoglaló (1–2 oldalra szánt narratíva – vázlat)



\### Kiinduló helyzet és probléma



A Pohánka és Társa Kft. több mint másfél évtizede működő, zalaegerszegi mikrovállalkozás, amely számviteli és adótanácsadási szolgáltatásokat nyújt mikro- és kisvállalkozások számára. A cég pénzügyi helyzete stabil, saját tőkéje pozitív, nincsen lejárt köztartozása, és “Megbízható adózó” minősítéssel rendelkezik. 



A Modern Vállalkozások Programja keretében elvégzett digitális intenzitásmérés azonban rámutatott, hogy a vállalkozás digitális érettsége alacsony: több kulcsfontosságú folyamat (számlabefogadás, banki egyeztetés, dokumentumkezelés) manuális, részben papíralapú, illetve több, egymással nem integrált rendszerben zajlik. Ez a működés a növekedés és a hatékonyság elsődleges korlátja.



\*\*\*



\### A Brunella Agent System szerepe



A pályázat középpontjában álló Brunella Agent System (BAS) egy hibrid, multi‑agent MI ökoszisztéma, amely kifejezetten a könyvelési és adminisztratív munkafolyamatok automatizálására készült. A rendszer orkesztrációja Node.js alapú, míg a nagy mennyiségű adatfeldolgozást Python/FastAPI komponensek végzik, Playwright alapú “Robotkéz” modulokkal kiegészítve, amelyek képesek emberhez hasonló módon kezelni a szoftverek grafikus felületeit.



A BAS több kulcstechnológiát egyesít: a LanceDB vektoradatbázisra épülő RAG architektúra lehetővé teszi, hogy a rendszer a korábbi számlák és könyvelési döntések alapján egyre intelligensebben támogassa az munkatársakat, míg a Phoenix Protocol v2 önjavító mechanizmus biztosítja a 24/7 üzembiztosságot. A Bifrost Gateway a lokális (Ollama) és a felhős (Gemini, GPT‑4o) MI modellek intelligens kombinációját valósítja meg, optimalizálva a költség–pontosság arányt. 



\*\*\*



\### Fejlesztési elemek és fejlesztési logika



A projekt első pillére a digitális infrastruktúra megerősítése: GPU‑s munkaállomás, korszerű irodai PC‑k, NAS és hálózati eszközök biztosítják azt a hardveres hátteret, amelyre a BAS hosszú távon stabilan építhető. Ezt egészíti ki a felhőalapú infrastruktúra (pl. Google Cloud), amely a skálázhatóságot, biztonságos távoli elérést és professzionális backup‑megoldásokat nyújt. 



A második pillér a BAS szoftveres bevezetése: az orkesztrációs mag, az adatfeldolgozó és automatizáló modulok, valamint a vektoradatbázisra épülő tudásbázis integrációja a meglévő könyvelési folyamatokba. Ennek eredményeként a beérkező számlák nagy része automatikus Gmail‑figyelés, OCR és AI‑alapú adatkinyerés révén kerül a könyvelő rendszerbe, míg a banki és pénztári tranzakciók automatizált egyeztető folyamatokon mennek keresztül. 



A harmadik pillér a tudásátadás és szervezetfejlesztés: a munkatársak célzott képzése biztosítja, hogy a BAS ne “fekete dobozként”, hanem átlátható, a mindennapi munkát támogató eszközként jelenjen meg, és a változás elfogadottsága magas legyen.



\*\*\*



\### Várható hatások és fenntarthatóság



A projekt révén a Pohánka és Társa Kft. egységnyi idő alatt több ügyfelet tud kiszolgálni, miközben csökken a hibakockázat és javul a szolgáltatás átláthatósága. A manuális adminisztráció visszaszorításával felszabaduló kapacitás magasabb hozzáadott értékű szakmai tevékenységre (tanácsadás, elemzés) fordítható, ami hozzájárul az árbevétel és a profitabilitás növekedéséhez.



A phoenix‑alapú önjavító architektúra, a felhőalapú backup és a rendszeres DI‑audit biztosítják a fejlesztés hosszú távú fenntarthatóságát és továbbfejleszthetőségét. A BAS bevezetése egyben új üzleti modellkapukat is megnyit (BAS‑alapú szolgáltatáscsomagok más vállalkozások számára), ami megalapozza a későbbi innovációs és skálázódási pályázatok (pl. GINOP Plusz 2.1.3‑24) sikeres elérését. 



\*\*\*



\## Akcióterv – teendők támogatásokra (pályázatok)



\### A. DIMOP Plusz-1.2.6/B-26 – azonnali prioritás



1\. \*\*Adatellenőrzés, jogosultsági check (1–2 nap)\*\*  

&#x20;  - DI‑igazolás, cégadatok, létszám, árbevétel, székhely/telephely ellenőrzése a mesterdoc és cégkivonat alapján. 



2\. \*\*Költségvetés véglegesítése (2–3 nap)\*\*  

&#x20;  - A 9 M Ft-os keret végleges bontása (hardver/szoftver/felhő/képzés) a fenti javaslat alapján, konkrét egységárakkal és szállítókkal. \[socialpro](https://www.socialpro.hu/dimop-plusz-126/)



3\. \*\*Árajánlatok beszerzése (5–7 nap)\*\*  

&#x20;  - Legalább 2–3 független árajánlat begyűjtése a fő tételekre (workstation, NAS, szoftverlicencek, fejlesztői szolgáltatás, felhőcsomag). \[onedrive.live](https://onedrive.live.com/personal/7042f804db147b6f/\_layouts/15/doc.aspx?resid=12040e83-f603-4478-93f4-7aa5e2f4a793\&cid=7042f804db147b6f)



4\. \*\*DFK és projektleírás finomhangolása (3–4 nap)\*\*  

&#x20;  - DFK aktualizálása a konkrét BAS‑projekt részleteivel, indikátorokkal, költségvetéssel és ütemtervvel. 



5\. \*\*Pályázati adatlap kitöltése (3–5 nap)\*\*  

&#x20;  - Online adatlapba beemelni a fenti adatlap‑szöveget (indokoltság, célok, szakmai tartalom, indikátorok), csatolni a szükséges mellékleteket (DFK, DI‑igazolás, árajánlatok).



6\. \*\*Belső ellenőrzés + beadás (1–2 nap)\*\*  

&#x20;  - Ellenőrző lista lefuttatása, hibák javítása, majd beadás jóval a június 30-i ablak vége előtt. 



\*\*\*



\### B. DIMOP Plusz-1.2.3/A-24 – “második kör” előkészítése



7\. \*\*Stratégiai döntés a második fejlesztési fázisról (1 nap)\*\*  

&#x20;  - Mi az, ami nem fér bele a 9 M Ft-ba (pl. extra cloud‑kapacitás, további modulok, hosszabb távú üzemeltetés), ezt külön “II. fázis” csomagba szervezni. 



8\. \*\*Jogosultsági kalkuláció (1–2 nap)\*\*  

&#x20;  - Árbevétel és üzemi eredmény alapján meghatározni, mekkora DIMOP 1.2.3/A támogatás + 0%-os hitel fér bele biztonságosan.



9\. \*\*Előminősítés / konzultáció (online vagy tanácsadóval, 1 nap)\*\*  

&#x20;  - Pályázatíró/tanácsadó egyeztetés, hogy a DIMOP 1.2.3/A-24 konstrukció melyik szakaszában érdemes majd indulni, és milyen dokumentáció szükséges. 



10\. \*\*Projektvázlat elkészítése DIMOP 1.2.3/A-ra (5–7 nap)\*\*  

&#x20;   - A DIMOP 1.2.6/B projekt tapasztalatai és eredményei alapján “felfelé” épített 3–12 M Ft-os második fejlesztési csomag kidolgozása (plusz modulok, további automatizálás, skálázás). 



\*\*\*



\### C. GINOP Plusz-2.1.3-24 és egyéb pályázatok – pipeline



11\. \*\*Innovációs dokumentáció csomag létrehozása (7–10 nap)\*\*  

&#x20;   - BAS technológiai leírás K+F szempontrendszerben (TRL, újdonságtartalom, Phoenix Protocol, Innovation Bridge, Swarm logika) GINOP 2.1.3‑24 célrendszeréhez igazítva. 



12\. \*\*Pályázatfigyelés beállítása (folyamatos)\*\*  

&#x20;   - Rendszeres figyelés GINOP 2.1.3‑24 új szakaszaira, esetleges új vállalati képzési pályázatokra (GINOP 3.2.1 jellegűek).



13\. \*\*MVLSH / Demján jellegű programok monitorozása (folyamatos)\*\*  

&#x20;   - Ha újra nyílik “Minden vállalkozásnak legyen saját honlapja” vagy MI‑fókuszú voucher, gyors reagálás a már kész tartalommal (pohanka.vercel.app, esettanulmányok). 



\*\*\*



\## Akcióterv – teendők támogatott hitelekre



\### D. GINOP Plusz-1.4.3-24 – KKV Technológia Plusz (0% hitel)



1\. \*\*Hitelképességi előszűrés (1–2 nap)\*\*  

&#x20;  - Belső kalkuláció: mekkora 0%-os hitel illeszkedik a jelenlegi 2–3 M Ft körüli éves nyereséghez és cash‑flow‑hoz (pl. 10–20 M Ft célösszeg). 



2\. \*\*MFB Pont / közvetítő bank felkeresése (1 nap)\*\*  

&#x20;  - Időpont egyeztetés, előminősítésre alkalmas dokumentumok (mérleg, eredménykimutatás, NAV igazolás, mesterdoc) összekészítése. 



3\. \*\*Előminősítési tárgyalás (1 nap)\*\*  

&#x20;  - A finanszírozandó eszköz- és technológiai projekt rövid bemutatása (BAS + esetleges jármű/gép), hitelösszeg és futamidő egyeztetése.



4\. \*\*Döntés: GINOP 1.4.3-24 vs. Széchenyi hitel kombináció (1–2 nap)\*\*  

&#x20;  - Összehasonlítani a 0%-os GINOP-hitel feltételeit a Széchenyi Mikrohitel MAX+ és Széchenyi Beruházási Hitel MAX+ konstrukciókkal (fedezet, futamidő, admin). 



5\. \*\*Hitelkérelem összeállítása és benyújtása (5–10 nap)\*\*  

&#x20;  - Részletes beruházási terv, cash‑flow terv, fedezet dokumentációja, szükséges banki nyomtatványok kitöltése. 



\*\*\*



\### E. DIMOP Plusz-1.2.3/A-24 – hitelrész integrálása



6\. \*\*DIMOP 1.2.3/A hitel–támogatás arány tervezése (2–3 nap)\*\*  

&#x20;  - Meghatározni, hogy a 3–20 M Ft-os keretből mekkora arányban legyen VNT és mekkora a 0%-os hitel, úgy hogy a hitelterhelés biztonságos maradjon. 



7\. \*\*Hitelrész banki egyeztetése (1–2 nap)\*\*  

&#x20;  - A pályázatban vállalt hitelrész feltételeinek pontosítása a finanszírozó intézménnyel (futamidő, biztosíték, lehívás ütemezése).



\*\*\*



\### F. Széchenyi Mikrohitel MAX+ és Beruházási Hitel MAX+



8\. \*\*Széchenyi Programiroda konzultáció (1 nap)\*\*  

&#x20;  - Termékismertetés és előminősítés: Mikrohitel MAX+ vs. Beruházási Hitel MAX+, javasolt hitelösszeg és fedezet. 



9\. \*\*Banki ajánlatok bekérése 2–3 banktól (3–5 nap)\*\*  

&#x20;  - Kamat (3% / 1,5% zöld), díjak, fedezeti elvárások, futamidő és türelmi idők összehasonlítása. 



10\. \*\*Hitelstratégia véglegesítése (1–2 nap)\*\*  

&#x20;   - Eldönteni, hogy a DIMOP + GINOP 0%-os hiteleket milyen mértékben egészítitek ki Széchenyi‑hitelekkel (pl. nagyobb jármű/bizonyos eszközök finanszírozására). 



11\. \*\*Hitelkérelem(ek) beadása és nyomon követése (5–15 nap)\*\*  

&#x20;   - Teljes banki dokumentáció összeállítása, hiánypótlások kezelése, majd pozitív döntés esetén folyósítás és szerződéses kötelezettségek monitorozása.





