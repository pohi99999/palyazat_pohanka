Az alábbi JSON-profilindexet használhatod közvetlenül Brunella ügynökökben: tartalmazza a cég-, pályázati- és hitelparamétereket, valamint a preferenciákat úgy strukturálva, hogy egy külső LLM-bázisú „hitel/pályázat kereső” ügynök ebből ki tudjon indulni.[^1](palyazat.md)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "profile\_version": "2026-06-30",
  "company": {
    "name": "Pohánka és Társa Kft.",
    "full\_name": "POHÁNKA ÉS TÁRSA KÖNYVELŐ IRODA KORLÁTOLT FELELŐSSÉGŰ TÁRSASÁG",
    "tax\_id": "14728864-2-20",
    "vat\_id": "HU14728864",
    "registration\_number": "20-09-069482",
    "founded": "2009-04-10",
    "legal\_form": "Kft",
    "seat": {
      "country": "HU",
      "region": "Nyugat-Dunántúl",
      "county": "Zala",
      "city": "Zalaegerszeg",
      "address": "Berek utca 38.",
      "is\_budapest": false
    },
    "headcount\_2025": 3,
    "sme\_class": "micro",
    "connected\_companies": false,
    "foreign\_owners": false,
    "main\_bank": {
      "name": "OTP Bank",
      "branch": "Zalaegerszeg",
      "account\_prefix": "11749008-24920311"
    },
    "taxation": {
      "scheme": "KIVA",
      "since": "2020-01-01",
      "reliable\_taxpayer": true,
      "reliable\_since": "2026-05-01",
      "public\_debt\_free": true
    },
    "tevor\_codes": \[
      { "code": "6920", "label": "Számviteli, könyvvizsgálói, adószakértői tevékenység", "main": true },
      { "code": "6201", "label": "Számítógépes programozás" },
      { "code": "6202", "label": "Információtechnológiai szaktanácsadás" },
      { "code": "6311", "label": "Adatfeldolgozás, web-hoszting szolgáltatás" },
      { "code": "6290", "label": "Egyéb információtechnológiai szolgáltatás" },
      { "code": "6310", "label": "Számítástechnikai infrastruktúra, adatfeldolgozás" }
    ]
  },
  "financials": {
    "years": \[
      {
        "year": 2023,
        "revenue\_net\_huf": 2844000,
        "ebitda\_huf": 1260000,
        "profit\_after\_tax\_huf": 1620000,
        "equity\_huf": 5344000,
        "balance\_sheet\_total\_huf": 5661000
      },
      {
        "year": 2024,
        "revenue\_net\_huf": 4204000,
        "ebitda\_huf": 346000,
        "profit\_after\_tax\_huf": 346000,
        "equity\_huf": 5681000,
        "balance\_sheet\_total\_huf": 6338000
      },
      {
        "year": 2025,
        "revenue\_net\_huf": 9158000,
        "ebitda\_huf": 517000,
        "profit\_after\_tax\_huf": 374000,
        "equity\_huf": 6065000,
        "balance\_sheet\_total\_huf": 6502000
      }
    ],
    "debt\_free": true,
    "previous\_grants": {
      "vnt\_used": false,
      "de\_minimis\_used": false,
      "de\_minimis\_remaining\_eur": 200000
    }
  },
  "digital\_profile": {
    "di\_company": {
      "score": 10,
      "level": "low",
      "id": "IG32095-2025",
      "date": "2025-06-19"
    },
    "di\_community": {
      "score": 8,
      "level": "high",
      "id": "IG32096-2025",
      "date": "2025-06-19"
    },
    "dfk": {
      "program": "Modern Vállalkozások Program 2.0",
      "supporting\_document\_id": "D127/23-505/2025",
      "project\_id": "DIMOP\_Plusz-1.2.7-23-2023-00001",
      "valid\_until": "2026-11-30"
    },
    "core\_project": {
      "name": "Brunella Agent System (BAS)",
      "description": "Multi-agent AI ökoszisztéma könyvelési és adminisztratív folyamatok automatizálására",
      "expected\_impacts": {
        "manual\_admin\_reduction\_pct": 50,
        "automatic\_invoice\_processing\_pct": 80,
        "bank\_reconciliation\_automation\_pct": 70
      }
    }
  },
  "investment\_plan": {
    "short\_term\_2026": {
      "dimop\_project": {
        "name": "BAS bevezetés és digitális infrastruktúra",
        "total\_value\_huf": 9000000,
        "grant\_expected\_huf": 8100000,
        "own\_contribution\_huf": 900000,
        "eligible\_items": \[
          "BAS szoftver és licencek",
          "Felhőszolgáltatás (IaaS/PaaS)",
          "OCR, LanceDB, AI modulok",
          "Tanácsadás és integráció",
          "Képzés (3 fő)",
          "IT hardver (GPU, NAS, hálózat) dimop-kereten belül"
        ]
      },
      "szechenyi\_credit": {
        "program": "Széchenyi Mikrohitel MAX+",
        "planned\_amount\_huf": 6000000,
        "purpose": \[
          "GPU AI munkaállomás (1 db)",
          "Irodai PC/laptop (3 db)",
          "NAS + hálózati eszközök",
          "Használt cégautó"
        ],
        "desired\_interest\_pct": 3,
        "desired\_term\_months": 60,
        "preferred\_grace\_period\_years": 1
      }
    },
    "mid\_term\_2027\_2028": {
      "potential\_credit\_range\_huf": \[10000000, 20000000],
      "use\_cases": \[
        "Szerverinfrastruktúra BAS SaaS szolgáltatáshoz",
        "Kiegészítő járművek (terepjáró, kosaras emelő) ha tevékenység bővül"
      ]
    },
    "long\_term\_2029\_plus": {
      "potential\_credit\_range\_huf": \[20000000, 30000000],
      "use\_case": "BAS SaaS skálázás országos / regionális szinten"
    }
  },
  "preferences": {
    "grant\_programs": {
      "preferred\_types": \[
        "KKV digitalizáció (IT, AI, automatizálás)",
        "Innovációs támogatás (AI termék)",
        "Vállalati képzés (digitális kompetencia)",
        "Vidéki mikrovállalkozásoknak szóló felhívás",
        "Kombinált 0%-os hitel + VNT konstrukciók"
      ],
      "preferred\_intensity\_pct": {
        "ideal": 90,
        "acceptable\_min": 70
      },
      "amount\_ranges\_huf": {
        "short\_term": \[3000000, 12000000],
        "mid\_term": \[12000000, 30000000]
      }
    },
    "credit\_programs": {
      "priority\_order": \[
        "State\_supported 0% investment loan (GINOP Plusz-1.4.3-24 KKV Technológia Plusz)",
        "Széchenyi Mikrohitel MAX+",
        "Széchenyi Beruházási Hitel MAX+",
        "DIMOP Plusz-1.2.3/A-24 kombinált 0% hitel + VNT",
        "MFB Pont kamattámogatott konstrukciók"
      ],
      "interest\_preference\_pct": {
        "ideal": 0,
        "acceptable\_max": 3
      },
      "amount\_preference\_huf": {
        "short\_term": \[5000000, 10000000],
        "mid\_term": \[10000000, 20000000],
        "long\_term": \[20000000, 30000000]
      },
      "grace\_period": {
        "ideal\_years": 2,
        "acceptable\_full\_annuity\_from\_start\_if\_dscr\_ge": 1.5
      }
    },
    "collateral": {
      "assets": \[
        "IT berendezések",
        "Cégautó"
      ],
      "real\_estate": {
        "seat\_property\_available": true,
        "prefer\_not\_to\_use": true
      },
      "preferred\_guarantee": \[
        "Garantiqa garancia",
        "AVHGA garancia"
      ]
    },
    "exclusions": {
      "exclude\_credit": \[
        "Piaci kamatozású >4%/év hitelek",
        "Forgóeszköz-hitelek (Széchenyi Likviditási / munkakapital)",
        "Extrém ingatlanfedezetet igénylő konstrukciók",
        "Rövid távon >25M Ft hitel"
      ],
      "exclude\_grants": \[
        "Kizárólag budapesti székhelyű cégeknek szóló felhívások",
        "Nagyvállalati (>250 fő) felhívások",
        "Mezőgazdasági, ipari vagy gyártási szektorra célzott pályázatok",
        "Export-fókuszú pályázatok",
        "Magas önerő (>30%) pályázatok",
        ">50M Ft tisztán K+F pályázatok jelenlegi árbevétel mellett"
      ]
    }
  },
  "eligibility\_checks": {
    "company\_params\_for\_agent": {
      "region": "Zala Vármegye",
      "is\_budapest": false,
      "headcount": 3,
      "revenue\_2025\_huf": 9158000,
      "sme\_size": "micro",
      "tax\_scheme": "KIVA",
      "di\_low": true,
      "dfk\_available": true
    },
    "agent\_must\_check\_each\_program": \[
      "Jogosultság mikro/kis KKV-ra (<=10 fő, <=2M EUR árbevétel)",
      "Területi hatókör: országos vagy Nyugat-Dunántúl, Budapest kizárása",
      "Ingatlanfedezet kötelező-e; ha igen, jelölés külön",
      "Garantiqa/AVHGA garancia bevonható-e ingatlan kiváltására",
      "Kettős finanszírozási tilalom: DIMOP VNT + hitel kombinációk összehangolása",
      "Van-e KIVA-specifikus kizárás",
      "Elszámolható-e IT hardver, szoftver, felhő, tanácsadás, képzés a BAS projektre",
      "Támogatási intenzitás és összegsáv illeszkedik-e a preferenciákhoz"
    ],
    "ranking\_criteria": {
      "order": \[
        "Kamat mértéke (0% > 1–2% > 3%)",
        "Ismerős programok (Széchenyi / KAVOSZ / GINOP Tech)",
        "Türelmi idő lehetősége",
        "Összeg illeszkedése (elsősorban 5–10M Ft sáv)",
        "Garantiqa/AVHGA elérhetősége"
      ]
    }
  }
}
```

Használat Brunellában:

* Ezt a JSON-t elmentheted pl. `pohanka\_credit\_profile.json` néven, és minden hitel/pályázat-kereső ügynök promptjában hivatkozhatsz rá mint „company\_profile”.
* A kereső ügynök feladata: a `preferences`, `eligibility\_checks` és az `investment\_plan` alapján szűrni a nyitott DIMOP/GNIOP/Széchenyi programokat, majd rangsorolni őket az itt megadott szabályok szerint.[^3](palyazat.md)
<span style="display:none">[^10](https://arxiv.org/abs/2405.17681)[^12](https://github.com/json-schema-org/json-schema-spec/wiki/Profiles-and-Sets)\[^14][^15](https://pages.nist.gov/OSCAL-Reference/models/v1.0.0/profile/json-outline/)[^17](https://www.wipo.int/edocs/mdocs/classifications/zh/cws_7/cws_7_5-annex1.docx)[^19](https://ieeexplore.ieee.org/document/11273215/)[^5](https://arxiv.org/abs/2503.02770)[^7](https://dl.acm.org/doi/10.1145/3735106.3736532)[^9](https://arxiv.org/abs/2407.03286)</span>

<div align="center">⁂</div>

\[^15]: https://cimug.ucaiug.org/WG19/IEC 62361-104 CIM Profiles to JSON schema Mapping - DRAFT/57-62361-104-IS-CIM Profiles to JSON Schema Mapping\_rev01v20.pdf

