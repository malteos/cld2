#!/usr/bin/env python3
"""Per-language catalogue of **non-benchmark** source websites.

Every entry lists websites that (a) serve text in the target language and
(b) are not LID / MT evaluation corpora. We pull examples from these to
avoid training–testing leakage against CommonLID, FLORES+, and similar.

Source types:
    gov      — government / state / public-sector
    news     — news publishers in the language
    cultural — cultural institutions, literature, academic, encyclopaedic
    civil    — NGO / international organisations publishing in the language
    religious — religious publications (often translated into rare languages)

This file is deliberately light on hard-coded URLs; the `fetch_web_examples.py`
script treats the list as *candidates* and falls back gracefully when a site
is unreachable, blocks scrapers, or doesn't yield extractable paragraph text.
"""
from __future__ import annotations

from typing import Any

# UDHR is available in ~500 languages on ohchr.org via two-letter-ish codes.
# Mapping our ISO-639-3 codes to the UDHR identifier where we know it.
# Many entries are intentionally absent; a missing entry means "no UDHR here".
UDHR_BASE = "https://www.ohchr.org/en/human-rights/universal-declaration/translations/"

# Per-language catalogue. Each entry has:
#   wikipedia   — Wikipedia subdomain, or None if no edition exists
#   sources     — list of {url, type, description}
SOURCES: dict[str, dict[str, Any]] = {
    "ace": {"wikipedia": "ace", "sources": [
        {"url": "https://ace.wikipedia.org/", "type": "cultural", "description": "Acehnese Wikipedia"},
        {"url": "https://acehkita.com/", "type": "news", "description": "Acehkita — regional news in Aceh (mixed Acehnese/Indonesian)"},
    ]},
    "acf": {"wikipedia": None, "sources": [
        {"url": "https://www.stlucianewsonline.com/", "type": "news", "description": "St. Lucia News Online"},
        {"url": "https://www.govt.lc/", "type": "gov", "description": "Government of Saint Lucia"},
        {"url": "https://www.potomitan.info/", "type": "education", "description": "Potomitan — Caribbean-creole literature / education portal"},
        {"url": "https://www.potomitan.info/atelier/kweyol/index.php", "type": "education", "description": "Potomitan — Kwéyòl texts (Kreyol section)"},
        {"url": "https://www.potomitan.info/bible/", "type": "religious", "description": "Potomitan — Kwéyòl Bible translations"},
        {"url": "https://stluciatimes.com/", "type": "news", "description": "St. Lucia Times"},
        {"url": "https://www.visitsaintlucia.org/", "type": "commercial", "description": "Saint Lucia Tourism Authority"},
        {"url": "https://www.thevoiceslu.com/", "type": "news", "description": "The Voice St. Lucia"},
    ]},
    "aeb": {"wikipedia": None, "sources": [
        {"url": "https://www.babnet.net/", "type": "news", "description": "BabNet — Tunisian news"},
        {"url": "https://www.tunisienumerique.com/", "type": "news", "description": "Tunisie Numérique"},
        {"url": "https://www.turess.com/", "type": "news", "description": "Turess — Tunisian press aggregator"},
        {"url": "https://nawaat.org/", "type": "news", "description": "Nawaat — Tunisian independent news"},
        {"url": "https://www.leaders.com.tn/", "type": "news", "description": "Leaders — Tunisian magazine"},
        {"url": "https://www.kapitalis.com/tunisie/", "type": "news", "description": "Kapitalis — Tunisian economic news"},
        {"url": "https://www.tap.info.tn/", "type": "news", "description": "TAP — Tunisian news agency"},
        {"url": "https://www.shemsfm.net/", "type": "news", "description": "Shems FM — Tunisian radio"},
    ]},
    "afr": {"wikipedia": "af", "sources": [
        {"url": "https://af.wikipedia.org/", "type": "cultural", "description": "Afrikaans Wikipedia"},
        {"url": "https://www.netwerk24.com/", "type": "news", "description": "Netwerk24 — Afrikaans news portal"},
        {"url": "https://www.parliament.gov.za/", "type": "gov", "description": "Parliament of South Africa (Afrikaans press releases)"},
    ]},
    "amh": {"wikipedia": "am", "sources": [
        {"url": "https://am.wikipedia.org/", "type": "cultural", "description": "Amharic Wikipedia"},
        {"url": "https://www.press.et/", "type": "news", "description": "Ethiopian Press Agency (አፍሪካውያን ፕሬስ) — Amharic news"},
        {"url": "https://www.fanabc.com/amharic/", "type": "news", "description": "Fana Broadcasting (Amharic service)"},
    ]},
    "apd": {"wikipedia": None, "sources": [
        {"url": "https://www.alrakoba.net/", "type": "news", "description": "Al Rakoba — Sudanese news portal"},
        {"url": "https://www.altaghyeer.info/", "type": "news", "description": "Al Taghyeer — Sudanese news"},
        {"url": "https://www.sudaniaa.com/", "type": "news", "description": "Sudaniaa — Sudanese portal"},
        {"url": "https://www.aljareeda.com/", "type": "news", "description": "Al Jareeda — Sudanese daily"},
        {"url": "https://alayam.com/", "type": "news", "description": "Al Ayam newspaper"},
        {"url": "https://www.sudafax.com/", "type": "news", "description": "Sudafax news"},
        {"url": "https://darfur24.com/", "type": "news", "description": "Darfur 24 — Sudanese regional news"},
    ]},
    "ara": {"wikipedia": "ar", "sources": [
        {"url": "https://ar.wikipedia.org/", "type": "cultural", "description": "Arabic Wikipedia"},
        {"url": "https://www.aljazeera.net/", "type": "news", "description": "Al Jazeera Arabic"},
        {"url": "https://www.bbc.com/arabic", "type": "news", "description": "BBC Arabic"},
    ]},
    "arb": {"wikipedia": "ar", "sources": [
        {"url": "https://ar.wikipedia.org/", "type": "cultural", "description": "Arabic Wikipedia (MSA)"},
        {"url": "https://www.un.org/ar/", "type": "civil", "description": "UN in Arabic"},
    ]},
    "arg": {"wikipedia": "an", "sources": [
        {"url": "https://an.wikipedia.org/", "type": "cultural", "description": "Aragonese Wikipedia"},
        {"url": "https://www.academiadelaragones.org/", "type": "cultural", "description": "Academia de l'Aragonés"},
    ]},
    "ars": {"wikipedia": None, "sources": [
        {"url": "https://www.spa.gov.sa/?lang=ar", "type": "gov", "description": "Saudi Press Agency — Arabic edition"},
        {"url": "https://sabq.org/", "type": "news", "description": "Sabq — Saudi Arabic news"},
        {"url": "https://www.alyaum.com/", "type": "news", "description": "Al Yaum — Saudi daily"},
        {"url": "https://www.okaz.com.sa/", "type": "news", "description": "Okaz — Saudi news"},
        {"url": "https://www.alriyadh.com/", "type": "news", "description": "Al Riyadh — daily newspaper"},
        {"url": "https://www.al-madina.com/", "type": "news", "description": "Al Madina newspaper"},
        {"url": "https://www.al-jazirah.com/", "type": "news", "description": "Al Jazirah — Saudi daily"},
        {"url": "https://www.alwatan.com.sa/", "type": "news", "description": "Al Watan Saudi Arabia"},
        {"url": "https://ajel.sa/", "type": "news", "description": "Ajel — Saudi news portal"},
    ]},
    "ary": {"wikipedia": "ary", "sources": [
        {"url": "https://ary.wikipedia.org/", "type": "cultural", "description": "Moroccan Arabic Wikipedia (Wikipediya Dderja)"},
        {"url": "https://www.hespress.com/", "type": "news", "description": "Hespress — Moroccan news (frequent Darija)"},
        {"url": "https://goud.ma/", "type": "news", "description": "Goud.ma — Moroccan Darija-heavy news"},
    ]},
    "arz": {"wikipedia": "arz", "sources": [
        {"url": "https://arz.wikipedia.org/", "type": "cultural", "description": "Egyptian Arabic Wikipedia"},
        {"url": "https://www.youm7.com/", "type": "news", "description": "Youm7 — Egyptian news"},
    ]},
    "asm": {"wikipedia": "as", "sources": [
        {"url": "https://as.wikipedia.org/", "type": "cultural", "description": "Assamese Wikipedia"},
        {"url": "https://assam.gov.in/", "type": "gov", "description": "Government of Assam (Assamese publications)"},
        {"url": "https://www.asomiyapratidin.in/", "type": "news", "description": "Asomiya Pratidin — Assamese daily"},
    ]},
    "aze": {"wikipedia": "az", "sources": [
        {"url": "https://az.wikipedia.org/", "type": "cultural", "description": "Azerbaijani Wikipedia"},
        {"url": "https://www.president.az/az", "type": "gov", "description": "President.az (Azerbaijani)"},
    ]},
    "azj": {"wikipedia": "az", "sources": [
        {"url": "https://az.wikipedia.org/", "type": "cultural", "description": "Azerbaijani Wikipedia (North Azerbaijani)"},
        {"url": "https://report.az/", "type": "news", "description": "Report.az — Baku news agency"},
    ]},
    "bak": {"wikipedia": "ba", "sources": [
        {"url": "https://ba.wikipedia.org/", "type": "cultural", "description": "Bashkir Wikipedia"},
        {"url": "https://bashinform.ru/ba/", "type": "news", "description": "Bashinform (Bashkir-language service)"},
    ]},
    "bcl": {"wikipedia": "bcl", "sources": [
        {"url": "https://bcl.wikipedia.org/", "type": "cultural", "description": "Central Bikol Wikipedia"},
        {"url": "https://www.bicolstandard.com/", "type": "news", "description": "Bicol Standard (English/Bicol)"},
    ]},
    "ben": {"wikipedia": "bn", "sources": [
        {"url": "https://bn.wikipedia.org/", "type": "cultural", "description": "Bengali Wikipedia"},
        {"url": "https://www.prothomalo.com/", "type": "news", "description": "Prothom Alo — Bangladesh's largest Bengali daily"},
        {"url": "https://www.bbc.com/bengali", "type": "news", "description": "BBC Bengali"},
    ]},
    "bik": {"wikipedia": "bcl", "sources": [
        {"url": "https://bcl.wikipedia.org/", "type": "cultural", "description": "Central Bikol Wikipedia (proxy for macro)"},
        {"url": "https://www.pia.gov.ph/", "type": "gov", "description": "Philippine Information Agency regional releases"},
    ]},
    "bre": {"wikipedia": "br", "sources": [
        {"url": "https://br.wikipedia.org/", "type": "cultural", "description": "Breton Wikipedia"},
        {"url": "https://www.francebleu.fr/breizh-izel", "type": "news", "description": "France Bleu Breizh Izel — partial Breton content"},
        {"url": "https://opab.bzh/", "type": "cultural", "description": "Ofis Publik ar Brezhoneg"},
        {"url": "https://www.lepeuplebreton.bzh/", "type": "news", "description": "Le Peuple breton"},
        {"url": "https://www.skolanemsav.bzh/breman.html", "type": "news", "description": "Bremañ — Breton-language paper"},
        {"url": "https://bannouheol.com/", "type": "cultural", "description": "Bannoù-Heol — Breton publisher"},
    ]},
    "bul": {"wikipedia": "bg", "sources": [
        {"url": "https://bg.wikipedia.org/", "type": "cultural", "description": "Bulgarian Wikipedia"},
        {"url": "https://www.government.bg/", "type": "gov", "description": "Council of Ministers of Bulgaria"},
        {"url": "https://dariknews.bg/", "type": "news", "description": "Darik News"},
    ]},
    "cat": {"wikipedia": "ca", "sources": [
        {"url": "https://ca.wikipedia.org/", "type": "cultural", "description": "Catalan Wikipedia"},
        {"url": "https://www.ara.cat/", "type": "news", "description": "Ara — Catalan daily"},
        {"url": "https://web.gencat.cat/ca/inici/", "type": "gov", "description": "Generalitat de Catalunya"},
    ]},
    "ces": {"wikipedia": "cs", "sources": [
        {"url": "https://cs.wikipedia.org/", "type": "cultural", "description": "Czech Wikipedia"},
        {"url": "https://www.vlada.cz/cz/", "type": "gov", "description": "Government of the Czech Republic"},
        {"url": "https://www.idnes.cz/", "type": "news", "description": "iDnes — Czech news"},
    ]},
    "cmn": {"wikipedia": "zh", "sources": [
        {"url": "https://zh.wikipedia.org/", "type": "cultural", "description": "Chinese Wikipedia"},
        {"url": "https://www.gov.cn/", "type": "gov", "description": "中国政府网 — Central People's Government (PRC)"},
        {"url": "https://www.xinhuanet.com/", "type": "news", "description": "Xinhua (Simplified Chinese)"},
    ]},
    "crh": {"wikipedia": "crh", "sources": [
        {"url": "https://crh.wikipedia.org/", "type": "cultural", "description": "Crimean Tatar Wikipedia"},
        {"url": "https://ktat.org/", "type": "civil", "description": "Crimean Tatar cultural society"},
    ]},
    "deu": {"wikipedia": "de", "sources": [
        {"url": "https://de.wikipedia.org/", "type": "cultural", "description": "German Wikipedia"},
        {"url": "https://www.bundesregierung.de/", "type": "gov", "description": "Bundesregierung (Federal Government of Germany)"},
        {"url": "https://www.tagesschau.de/", "type": "news", "description": "Tagesschau"},
    ]},
    "ell": {"wikipedia": "el", "sources": [
        {"url": "https://el.wikipedia.org/", "type": "cultural", "description": "Greek Wikipedia"},
        {"url": "https://www.kathimerini.gr/", "type": "news", "description": "Kathimerini"},
        {"url": "https://www.primeminister.gr/", "type": "gov", "description": "Office of the Prime Minister of Greece"},
    ]},
    "eng": {"wikipedia": "en", "sources": [
        {"url": "https://en.wikipedia.org/", "type": "cultural", "description": "English Wikipedia"},
        {"url": "https://www.gov.uk/", "type": "gov", "description": "GOV.UK"},
        {"url": "https://www.bbc.com/news", "type": "news", "description": "BBC News"},
    ]},
    "est": {"wikipedia": "et", "sources": [
        {"url": "https://et.wikipedia.org/", "type": "cultural", "description": "Estonian Wikipedia"},
        {"url": "https://www.valitsus.ee/", "type": "gov", "description": "Estonian Government"},
        {"url": "https://err.ee/", "type": "news", "description": "ERR — Estonian Public Broadcasting"},
    ]},
    "ext": {"wikipedia": "ext", "sources": [
        {"url": "https://ext.wikipedia.org/", "type": "cultural", "description": "Extremaduran Wikipedia"},
        {"url": "https://elhabrahla.wordpress.com/", "type": "cultural", "description": "El Habrahla — Extremaduran blog"},
    ]},
    "fas": {"wikipedia": "fa", "sources": [
        {"url": "https://fa.wikipedia.org/", "type": "cultural", "description": "Persian Wikipedia"},
        {"url": "https://president.ir/fa", "type": "gov", "description": "Office of the President (Iran)"},
        {"url": "https://www.bbc.com/persian", "type": "news", "description": "BBC Persian"},
    ]},
    "fil": {"wikipedia": "tl", "sources": [
        {"url": "https://tl.wikipedia.org/", "type": "cultural", "description": "Tagalog/Filipino Wikipedia"},
        {"url": "https://www.officialgazette.gov.ph/", "type": "gov", "description": "Official Gazette of the Philippines"},
        {"url": "https://www.abs-cbn.com/news", "type": "news", "description": "ABS-CBN News (TL/ENG)"},
    ]},
    "fin": {"wikipedia": "fi", "sources": [
        {"url": "https://fi.wikipedia.org/", "type": "cultural", "description": "Finnish Wikipedia"},
        {"url": "https://valtioneuvosto.fi/etusivu", "type": "gov", "description": "Finnish Government"},
        {"url": "https://yle.fi/uutiset", "type": "news", "description": "Yle Uutiset"},
    ]},
    "fra": {"wikipedia": "fr", "sources": [
        {"url": "https://fr.wikipedia.org/", "type": "cultural", "description": "French Wikipedia"},
        {"url": "https://www.gouvernement.fr/", "type": "gov", "description": "Gouvernement de la République française"},
        {"url": "https://www.lemonde.fr/", "type": "news", "description": "Le Monde"},
    ]},
    "fro": {"wikipedia": None, "sources": [
        {"url": "https://www.arlima.net/", "type": "cultural", "description": "ARLIMA — Archives de littérature du Moyen Âge"},
        {"url": "https://micmap.org/dicfro/", "type": "education", "description": "Dictionnaire du Français Médiéval (DicFro)"},
        {"url": "https://txm.bfm-corpus.org/", "type": "education", "description": "Base de Français Médiéval — ENS Lyon corpus"},
        {"url": "https://ebooks.adelaide.edu.au/c/chanson/roland/", "type": "cultural", "description": "The Chanson de Roland — University of Adelaide ebook"},
        {"url": "https://www.gutenberg.org/browse/languages/fro", "type": "cultural", "description": "Project Gutenberg — Old French texts"},
    ]},
    "fry": {"wikipedia": "fy", "sources": [
        {"url": "https://fy.wikipedia.org/", "type": "cultural", "description": "Western Frisian Wikipedia"},
        {"url": "https://www.omropfryslan.nl/", "type": "news", "description": "Omrop Fryslân — regional broadcaster"},
    ]},
    "fuv": {"wikipedia": None, "sources": [
        {"url": "https://www.voafulfulde.com/", "type": "news", "description": "Voice of America Fulfulde"},
        {"url": "https://www.voafulfulde.com/p/5819.html", "type": "news", "description": "VOA Fulfulde — news section"},
        {"url": "https://www.dw.com/fuv/", "type": "news", "description": "Deutsche Welle Fulfulde (tentative)"},
        {"url": "https://pulaagu.com/", "type": "cultural", "description": "Pulaagu — Pulaar cultural portal"},
        {"url": "https://www.sil.org/resources/publications/fub", "type": "education", "description": "SIL Fulfulde publications"},
    ]},
    "gaz": {"wikipedia": "om", "sources": [
        {"url": "https://om.wikipedia.org/", "type": "cultural", "description": "Oromo Wikipedia (West-Central proxy)"},
        {"url": "https://www.oromiyaa.com/", "type": "news", "description": "Oromia Regional portal (Afaan Oromoo)"},
        {"url": "https://www.bbc.com/afaanoromoo", "type": "news", "description": "BBC Afaan Oromoo"},
    ]},
    "gcf": {"wikipedia": None, "sources": [
        {"url": "https://la1ere.francetvinfo.fr/guadeloupe/", "type": "news", "description": "Guadeloupe La 1ère"},
        {"url": "https://www.potomitan.info/", "type": "education", "description": "Potomitan — Caribbean-creole literature / education portal"},
        {"url": "https://www.potomitan.info/atelier/index.php", "type": "education", "description": "Potomitan — creole texts atelier"},
        {"url": "https://www.rci.fm/guadeloupe/", "type": "news", "description": "Radio Caraïbes Internationale Guadeloupe"},
        {"url": "https://www.guadeloupe.fr/", "type": "gov", "description": "Région Guadeloupe"},
        {"url": "https://www.france-antilles.fr/guadeloupe", "type": "news", "description": "France-Antilles Guadeloupe"},
        {"url": "https://www.antillesmultimedia.com/", "type": "commercial", "description": "Antilles Multimédia"},
        {"url": "https://www.karicom.org/", "type": "civil", "description": "CARICOM"},
    ]},
    "gcr": {"wikipedia": None, "sources": [
        {"url": "https://la1ere.francetvinfo.fr/guyane/", "type": "news", "description": "Guyane La 1ère"},
        {"url": "https://www.potomitan.info/", "type": "education", "description": "Potomitan — Caribbean-creole literature / education portal"},
        {"url": "https://www.guyaweb.com/", "type": "news", "description": "Guyaweb — French Guiana news"},
        {"url": "https://www.ctguyane.fr/", "type": "gov", "description": "Collectivité territoriale de Guyane"},
        {"url": "https://www.franceguyane.fr/", "type": "news", "description": "France-Guyane"},
        {"url": "https://www.guyane.cci.fr/", "type": "commercial", "description": "Chambre de Commerce et d'Industrie de Guyane"},
        {"url": "https://www.univ-guyane.fr/", "type": "education", "description": "Université de Guyane"},
        {"url": "https://www.radiopeyi.com/", "type": "news", "description": "Radio Peyi — Kreyol Guyanè radio"},
    ]},
    "gla": {"wikipedia": "gd", "sources": [
        {"url": "https://gd.wikipedia.org/", "type": "cultural", "description": "Scottish Gaelic Wikipedia"},
        {"url": "https://www.bbc.co.uk/naidheachdan", "type": "news", "description": "BBC Naidheachdan (Scottish Gaelic news)"},
        {"url": "https://www.gaidhlig.scot/", "type": "gov", "description": "Bòrd na Gàidhlig"},
    ]},
    "gle": {"wikipedia": "ga", "sources": [
        {"url": "https://ga.wikipedia.org/", "type": "cultural", "description": "Irish Wikipedia"},
        {"url": "https://www.rte.ie/news/nuacht/", "type": "news", "description": "Nuacht RTÉ (Irish)"},
        {"url": "https://www.gov.ie/ga/", "type": "gov", "description": "Gov.ie — Irish-language portal"},
        {"url": "https://tuairisc.ie/", "type": "news", "description": "Tuairisc.ie — Irish-language news"},
        {"url": "https://comhar.ie/", "type": "cultural", "description": "Comhar — Irish-language literary magazine"},
        {"url": "https://www.nuacht24.com/", "type": "news", "description": "Nuacht24 — 24-hour Irish news"},
    ]},
    "gom": {"wikipedia": "gom", "sources": [
        {"url": "https://gom.wikipedia.org/", "type": "cultural", "description": "Goan Konkani Wikipedia"},
        {"url": "https://www.bhaangar.com/", "type": "news", "description": "Bhaangar Bhuim — Konkani periodical"},
    ]},
    "grc": {"wikipedia": None, "sources": [
        {"url": "https://www.perseus.tufts.edu/hopper/", "type": "cultural", "description": "Perseus Digital Library"},
        {"url": "https://www.hs-augsburg.de/~harsch/graeca/grae_ind.html", "type": "education", "description": "Bibliotheca Augustana — Greek corpus"},
        {"url": "https://el.wikisource.org/wiki/Κύρια_Σελίδα", "type": "cultural", "description": "Greek Wikisource (polytonic classical texts)"},
        {"url": "https://www.sacred-texts.com/cla/", "type": "cultural", "description": "Sacred Texts — Classical archive"},
        {"url": "https://stephanus.tlg.uci.edu/", "type": "education", "description": "Thesaurus Linguae Graecae (open pages)"},
        {"url": "https://dcc.dickinson.edu/", "type": "education", "description": "Dickinson College Commentaries"},
    ]},
    "gug": {"wikipedia": "gn", "sources": [
        {"url": "https://gn.wikipedia.org/", "type": "cultural", "description": "Guarani Wikipedia"},
        {"url": "https://www.presidencia.gov.py/", "type": "gov", "description": "Presidencia de la República del Paraguay (some Guarani)"},
    ]},
    "guj": {"wikipedia": "gu", "sources": [
        {"url": "https://gu.wikipedia.org/", "type": "cultural", "description": "Gujarati Wikipedia"},
        {"url": "https://gujaratsamachar.com/", "type": "news", "description": "Gujarat Samachar"},
        {"url": "https://gujaratinformation.gujarat.gov.in/", "type": "gov", "description": "Government of Gujarat — Information Dept."},
    ]},
    "guw": {"wikipedia": None, "sources": [
        {"url": "https://www.24haubenin.info/", "type": "news", "description": "24 Heures au Bénin"},
        {"url": "https://beninrevele.bj/", "type": "gov", "description": "Bénin Révélé — Government of Benin"},
        {"url": "https://www.benindiaspora.com/", "type": "education", "description": "Béninoise cultural / education portal"},
        {"url": "https://www.sonangnon.com/", "type": "news", "description": "Sonangnon — Béninoise news"},
        {"url": "https://lanation.bj/", "type": "news", "description": "La Nation — Bénin official daily"},
        {"url": "https://www.banouto.info/", "type": "news", "description": "Banouto — Béninoise news portal"},
        {"url": "https://fr.allafrica.com/benin/", "type": "news", "description": "AllAfrica — Bénin section"},
    ]},
    "hau": {"wikipedia": "ha", "sources": [
        {"url": "https://ha.wikipedia.org/", "type": "cultural", "description": "Hausa Wikipedia"},
        {"url": "https://www.bbc.com/hausa", "type": "news", "description": "BBC Hausa"},
        {"url": "https://www.voahausa.com/", "type": "news", "description": "VOA Hausa"},
    ]},
    "hbo": {"wikipedia": None, "sources": [
        {"url": "https://www.sefaria.org/texts/Tanakh", "type": "cultural", "description": "Sefaria — Tanakh (biblical Hebrew)"},
        {"url": "https://mechon-mamre.org/p/pt/pt0.htm", "type": "education", "description": "Mechon Mamre — Hebrew Bible"},
        {"url": "https://he.wikisource.org/wiki/", "type": "cultural", "description": "Hebrew Wikisource (Biblical texts)"},
        {"url": "https://www.sefaria.org/texts/Mishnah", "type": "cultural", "description": "Sefaria — Mishnah"},
        {"url": "https://www.biblehub.com/hebrew/", "type": "education", "description": "Bible Hub — Hebrew texts"},
        {"url": "https://biblehub.com/interlinear/genesis/1.htm", "type": "education", "description": "Bible Hub Interlinear Hebrew"},
    ]},
    "heb": {"wikipedia": "he", "sources": [
        {"url": "https://he.wikipedia.org/", "type": "cultural", "description": "Hebrew Wikipedia"},
        {"url": "https://www.gov.il/he", "type": "gov", "description": "gov.il (Israel)"},
        {"url": "https://www.haaretz.co.il/", "type": "news", "description": "Haaretz Hebrew"},
    ]},
    "hin": {"wikipedia": "hi", "sources": [
        {"url": "https://hi.wikipedia.org/", "type": "cultural", "description": "Hindi Wikipedia"},
        {"url": "https://www.bbc.com/hindi", "type": "news", "description": "BBC Hindi"},
        {"url": "https://www.india.gov.in/hi", "type": "gov", "description": "India.gov.in Hindi portal"},
    ]},
    "ibo": {"wikipedia": "ig", "sources": [
        {"url": "https://ig.wikipedia.org/", "type": "cultural", "description": "Igbo Wikipedia"},
        {"url": "https://www.bbc.com/igbo", "type": "news", "description": "BBC Igbo"},
    ]},
    "ind": {"wikipedia": "id", "sources": [
        {"url": "https://id.wikipedia.org/", "type": "cultural", "description": "Indonesian Wikipedia"},
        {"url": "https://www.setneg.go.id/", "type": "gov", "description": "Sekretariat Negara RI"},
        {"url": "https://www.kompas.com/", "type": "news", "description": "Kompas"},
    ]},
    "ita": {"wikipedia": "it", "sources": [
        {"url": "https://it.wikipedia.org/", "type": "cultural", "description": "Italian Wikipedia"},
        {"url": "https://www.governo.it/", "type": "gov", "description": "Governo Italiano"},
        {"url": "https://www.ansa.it/", "type": "news", "description": "ANSA"},
    ]},
    "jav": {"wikipedia": "jv", "sources": [
        {"url": "https://jv.wikipedia.org/", "type": "cultural", "description": "Javanese Wikipedia"},
        {"url": "https://www.panjebarsemangat.co.id/", "type": "news", "description": "Panjebar Semangat — Javanese magazine"},
    ]},
    "jpn": {"wikipedia": "ja", "sources": [
        {"url": "https://ja.wikipedia.org/", "type": "cultural", "description": "Japanese Wikipedia"},
        {"url": "https://www.kantei.go.jp/", "type": "gov", "description": "Prime Minister's Office of Japan"},
        {"url": "https://www.asahi.com/", "type": "news", "description": "Asahi Shimbun"},
    ]},
    "kab": {"wikipedia": "kab", "sources": [
        {"url": "https://kab.wikipedia.org/", "type": "cultural", "description": "Kabyle Wikipedia"},
        {"url": "https://www.tamurt.info/", "type": "news", "description": "Tamurt — Kabyle news portal"},
    ]},
    "kan": {"wikipedia": "kn", "sources": [
        {"url": "https://kn.wikipedia.org/", "type": "cultural", "description": "Kannada Wikipedia"},
        {"url": "https://www.prajavani.net/", "type": "news", "description": "Prajavani — Kannada daily"},
        {"url": "https://www.karnataka.gov.in/", "type": "gov", "description": "Government of Karnataka"},
    ]},
    "kik": {"wikipedia": "ki", "sources": [
        {"url": "https://ki.wikipedia.org/", "type": "cultural", "description": "Kikuyu Wikipedia"},
        {"url": "https://www.jw.org/ki/", "type": "religious", "description": "jw.org Kikuyu edition"},
    ]},
    "kor": {"wikipedia": "ko", "sources": [
        {"url": "https://ko.wikipedia.org/", "type": "cultural", "description": "Korean Wikipedia"},
        {"url": "https://www.korea.kr/", "type": "gov", "description": "Government of Korea"},
        {"url": "https://www.hani.co.kr/", "type": "news", "description": "The Hankyoreh"},
    ]},
    "lat": {"wikipedia": "la", "sources": [
        {"url": "https://la.wikipedia.org/", "type": "cultural", "description": "Latin Wikipedia"},
        {"url": "https://www.thelatinlibrary.com/", "type": "cultural", "description": "The Latin Library"},
        {"url": "https://www.vatican.va/archive/hist_councils/index_lt.htm", "type": "religious", "description": "Vatican Latin archives"},
    ]},
    "lav": {"wikipedia": "lv", "sources": [
        {"url": "https://lv.wikipedia.org/", "type": "cultural", "description": "Latvian Wikipedia"},
        {"url": "https://www.mk.gov.lv/lv", "type": "gov", "description": "Cabinet of Ministers of Latvia"},
        {"url": "https://www.lsm.lv/", "type": "news", "description": "LSM — Latvian Public Broadcasting"},
    ]},
    "lij": {"wikipedia": "lij", "sources": [
        {"url": "https://lij.wikipedia.org/", "type": "cultural", "description": "Ligurian Wikipedia"},
        {"url": "https://www.gazzettinodellaliguria.it/", "type": "news", "description": "Ligurian regional news"},
    ]},
    "lin": {"wikipedia": "ln", "sources": [
        {"url": "https://ln.wikipedia.org/", "type": "cultural", "description": "Lingala Wikipedia"},
        {"url": "https://www.voalingala.com/", "type": "news", "description": "Voice of America Lingala"},
    ]},
    "ltg": {"wikipedia": "ltg", "sources": [
        {"url": "https://ltg.wikipedia.org/", "type": "cultural", "description": "Latgalian Wikipedia"},
        {"url": "https://lakuga.lv/", "type": "cultural", "description": "LaKuGa — Latgalian culture portal"},
    ]},
    "lug": {"wikipedia": "lg", "sources": [
        {"url": "https://lg.wikipedia.org/", "type": "cultural", "description": "Luganda Wikipedia"},
        {"url": "https://www.bukedde.co.ug/", "type": "news", "description": "Bukedde — Luganda daily"},
    ]},
    "lvs": {"wikipedia": "lv", "sources": [
        {"url": "https://lv.wikipedia.org/", "type": "cultural", "description": "Latvian Wikipedia (Standard Latvian)"},
        {"url": "https://www.delfi.lv/", "type": "news", "description": "Delfi.lv"},
    ]},
    "mal": {"wikipedia": "ml", "sources": [
        {"url": "https://ml.wikipedia.org/", "type": "cultural", "description": "Malayalam Wikipedia"},
        {"url": "https://www.mathrubhumi.com/", "type": "news", "description": "Mathrubhumi"},
        {"url": "https://www.kerala.gov.in/malayalam", "type": "gov", "description": "Government of Kerala"},
    ]},
    "mar": {"wikipedia": "mr", "sources": [
        {"url": "https://mr.wikipedia.org/", "type": "cultural", "description": "Marathi Wikipedia"},
        {"url": "https://www.loksatta.com/", "type": "news", "description": "Loksatta"},
        {"url": "https://www.maharashtra.gov.in/", "type": "gov", "description": "Government of Maharashtra"},
    ]},
    "mlg": {"wikipedia": "mg", "sources": [
        {"url": "https://mg.wikipedia.org/", "type": "cultural", "description": "Malagasy Wikipedia"},
        {"url": "https://www.lexpressmada.com/", "type": "news", "description": "L'Express de Madagascar (includes Malagasy content)"},
    ]},
    "msa": {"wikipedia": "ms", "sources": [
        {"url": "https://ms.wikipedia.org/", "type": "cultural", "description": "Malay Wikipedia"},
        {"url": "https://www.bharian.com.my/", "type": "news", "description": "Berita Harian"},
        {"url": "https://www.malaysia.gov.my/portal/index", "type": "gov", "description": "MyGovernment portal (Malay)"},
    ]},
    "nld": {"wikipedia": "nl", "sources": [
        {"url": "https://nl.wikipedia.org/", "type": "cultural", "description": "Dutch Wikipedia"},
        {"url": "https://www.rijksoverheid.nl/", "type": "gov", "description": "Rijksoverheid — Dutch government"},
        {"url": "https://www.nrc.nl/", "type": "news", "description": "NRC Handelsblad"},
    ]},
    "nso": {"wikipedia": None, "sources": [
        {"url": "https://www.capricornfm.co.za/", "type": "news", "description": "Capricorn FM (Sepedi / English)"},
        {"url": "https://www.sabc.co.za/sabc/thobela-fm/", "type": "news", "description": "SABC Thobela FM — Sepedi radio"},
        {"url": "https://www.jw.org/nso/", "type": "religious", "description": "jw.org Northern Sotho"},
        {"url": "https://www.gov.za/", "type": "gov", "description": "South African Government (multi-language)"},
        {"url": "https://www.limpopo.gov.za/", "type": "gov", "description": "Limpopo Provincial Government (Sepedi-speaking region)"},
        {"url": "https://www.pedilanguage.co.za/", "type": "education", "description": "Pedi Language — Sepedi resources"},
        {"url": "https://www.iol.co.za/", "type": "news", "description": "IOL — South African news (mixed languages)"},
    ]},
    "nyn": {"wikipedia": None, "sources": [
        {"url": "https://www.newvision.co.ug/", "type": "news", "description": "New Vision — Uganda news"},
        {"url": "https://orumuri.co.ug/", "type": "news", "description": "Orumuri — Runyankore/Rukiga newspaper"},
        {"url": "https://www.mak.ac.ug/", "type": "education", "description": "Makerere University"},
        {"url": "https://www.jw.org/nyn/", "type": "religious", "description": "jw.org Runyankore"},
        {"url": "https://ugandaradionetwork.net/", "type": "news", "description": "Uganda Radio Network"},
        {"url": "https://www.monitor.co.ug/", "type": "news", "description": "Daily Monitor — Uganda"},
        {"url": "https://www.kanguka.org/", "type": "education", "description": "Kanguka — Runyankore language resources"},
    ]},
    "oci": {"wikipedia": "oc", "sources": [
        {"url": "https://oc.wikipedia.org/", "type": "cultural", "description": "Occitan Wikipedia"},
        {"url": "https://www.jornalet.com/", "type": "news", "description": "Jornalet — Occitan news"},
    ]},
    "orm": {"wikipedia": "om", "sources": [
        {"url": "https://om.wikipedia.org/", "type": "cultural", "description": "Oromo Wikipedia"},
        {"url": "https://www.bbc.com/afaanoromoo", "type": "news", "description": "BBC Afaan Oromoo"},
    ]},
    "ory": {"wikipedia": "or", "sources": [
        {"url": "https://or.wikipedia.org/", "type": "cultural", "description": "Odia Wikipedia"},
        {"url": "https://sambadodisha.com/", "type": "news", "description": "Sambad — Odia daily"},
        {"url": "https://www.odisha.gov.in/", "type": "gov", "description": "Government of Odisha"},
    ]},
    "pan": {"wikipedia": "pa", "sources": [
        {"url": "https://pa.wikipedia.org/", "type": "cultural", "description": "Punjabi Wikipedia"},
        {"url": "https://www.ajitjalandhar.com/", "type": "news", "description": "Ajit Jalandhar — Punjabi daily"},
        {"url": "https://punjab.gov.in/", "type": "gov", "description": "Government of Punjab"},
    ]},
    "pcm": {"wikipedia": "pcm", "sources": [
        {"url": "https://pcm.wikipedia.org/", "type": "cultural", "description": "Nigerian Pidgin Wikipedia"},
        {"url": "https://www.bbc.com/pidgin", "type": "news", "description": "BBC Pidgin"},
    ]},
    "pol": {"wikipedia": "pl", "sources": [
        {"url": "https://pl.wikipedia.org/", "type": "cultural", "description": "Polish Wikipedia"},
        {"url": "https://www.gov.pl/", "type": "gov", "description": "Gov.pl"},
        {"url": "https://www.rp.pl/", "type": "news", "description": "Rzeczpospolita"},
    ]},
    "por": {"wikipedia": "pt", "sources": [
        {"url": "https://pt.wikipedia.org/", "type": "cultural", "description": "Portuguese Wikipedia"},
        {"url": "https://www.gov.br/pt-br", "type": "gov", "description": "Gov.br — Brazilian government"},
        {"url": "https://www.publico.pt/", "type": "news", "description": "Público"},
    ]},
    "rcf": {"wikipedia": None, "sources": [
        {"url": "https://la1ere.francetvinfo.fr/reunion/", "type": "news", "description": "Réunion La 1ère"},
        {"url": "https://www.zinfos974.com/", "type": "news", "description": "Zinfos 974 — Réunion news"},
        {"url": "https://www.clicanoo.re/", "type": "news", "description": "Clicanoo / JIR"},
        {"url": "https://www.ipreunion.com/", "type": "news", "description": "IP Réunion"},
        {"url": "https://www.temoignages.re/", "type": "news", "description": "Témoignages — quotidien (PCR)"},
        {"url": "https://www.runweb.re/", "type": "news", "description": "Runweb — Réunion news"},
        {"url": "https://www.regionreunion.com/", "type": "gov", "description": "Région Réunion"},
        {"url": "https://www.cg974.fr/", "type": "gov", "description": "Conseil Départemental de La Réunion"},
        {"url": "https://www.linfo.re/", "type": "news", "description": "L'Info — Réunion news portal"},
    ]},
    "rus": {"wikipedia": "ru", "sources": [
        {"url": "https://ru.wikipedia.org/", "type": "cultural", "description": "Russian Wikipedia"},
        {"url": "https://government.ru/", "type": "gov", "description": "Government of the Russian Federation"},
        {"url": "https://meduza.io/", "type": "news", "description": "Meduza"},
    ]},
    "san": {"wikipedia": "sa", "sources": [
        {"url": "https://sa.wikipedia.org/", "type": "cultural", "description": "Sanskrit Wikipedia"},
        {"url": "https://www.sanskritdocuments.org/", "type": "cultural", "description": "Sanskrit Documents"},
        {"url": "https://www.sudharma.in/", "type": "news", "description": "Sudharma — Sanskrit daily"},
    ]},
    "sna": {"wikipedia": "sn", "sources": [
        {"url": "https://sn.wikipedia.org/", "type": "cultural", "description": "Shona Wikipedia"},
        {"url": "https://www.kwayedza.co.zw/", "type": "news", "description": "Kwayedza — Shona-language newspaper"},
    ]},
    "sot": {"wikipedia": "st", "sources": [
        {"url": "https://st.wikipedia.org/", "type": "cultural", "description": "Southern Sotho Wikipedia"},
        {"url": "https://www.jw.org/st/", "type": "religious", "description": "jw.org Southern Sotho edition"},
    ]},
    "spa": {"wikipedia": "es", "sources": [
        {"url": "https://es.wikipedia.org/", "type": "cultural", "description": "Spanish Wikipedia"},
        {"url": "https://www.lamoncloa.gob.es/", "type": "gov", "description": "La Moncloa — Spanish government"},
        {"url": "https://elpais.com/", "type": "news", "description": "El País"},
    ]},
    "swa": {"wikipedia": "sw", "sources": [
        {"url": "https://sw.wikipedia.org/", "type": "cultural", "description": "Swahili Wikipedia"},
        {"url": "https://www.bbc.com/swahili", "type": "news", "description": "BBC Swahili"},
        {"url": "https://www.mwananchi.co.tz/", "type": "news", "description": "Mwananchi — Tanzanian Swahili daily"},
    ]},
    "swh": {"wikipedia": "sw", "sources": [
        {"url": "https://sw.wikipedia.org/", "type": "cultural", "description": "Swahili Wikipedia (Coastal Swahili)"},
        {"url": "https://www.dw.com/sw/", "type": "news", "description": "Deutsche Welle Kiswahili"},
    ]},
    "tam": {"wikipedia": "ta", "sources": [
        {"url": "https://ta.wikipedia.org/", "type": "cultural", "description": "Tamil Wikipedia"},
        {"url": "https://www.dinamani.com/", "type": "news", "description": "Dinamani"},
        {"url": "https://www.tn.gov.in/tamil", "type": "gov", "description": "Government of Tamil Nadu"},
    ]},
    "tat": {"wikipedia": "tt", "sources": [
        {"url": "https://tt.wikipedia.org/", "type": "cultural", "description": "Tatar Wikipedia"},
        {"url": "https://intertat.tatar/", "type": "news", "description": "Intertat — Tatar-language news"},
    ]},
    "tel": {"wikipedia": "te", "sources": [
        {"url": "https://te.wikipedia.org/", "type": "cultural", "description": "Telugu Wikipedia"},
        {"url": "https://www.eenadu.net/", "type": "news", "description": "Eenadu — Telugu daily"},
        {"url": "https://www.ap.gov.in/", "type": "gov", "description": "Government of Andhra Pradesh"},
    ]},
    "tgl": {"wikipedia": "tl", "sources": [
        {"url": "https://tl.wikipedia.org/", "type": "cultural", "description": "Tagalog Wikipedia"},
        {"url": "https://www.philstar.com/", "type": "news", "description": "The Philippine Star (partial Tagalog)"},
    ]},
    "tha": {"wikipedia": "th", "sources": [
        {"url": "https://th.wikipedia.org/", "type": "cultural", "description": "Thai Wikipedia"},
        {"url": "https://www.thaigov.go.th/", "type": "gov", "description": "Government House of Thailand"},
        {"url": "https://www.thairath.co.th/", "type": "news", "description": "Thairath"},
    ]},
    "tuk": {"wikipedia": "tk", "sources": [
        {"url": "https://tk.wikipedia.org/", "type": "cultural", "description": "Turkmen Wikipedia"},
        {"url": "https://turkmenistan.gov.tm/", "type": "gov", "description": "Government of Turkmenistan"},
    ]},
    "tur": {"wikipedia": "tr", "sources": [
        {"url": "https://tr.wikipedia.org/", "type": "cultural", "description": "Turkish Wikipedia"},
        {"url": "https://www.tccb.gov.tr/", "type": "gov", "description": "Turkish Presidency"},
        {"url": "https://www.hurriyet.com.tr/", "type": "news", "description": "Hürriyet"},
    ]},
    "ukr": {"wikipedia": "uk", "sources": [
        {"url": "https://uk.wikipedia.org/", "type": "cultural", "description": "Ukrainian Wikipedia"},
        {"url": "https://www.kmu.gov.ua/", "type": "gov", "description": "Cabinet of Ministers of Ukraine"},
        {"url": "https://www.pravda.com.ua/", "type": "news", "description": "Ukrayinska Pravda"},
    ]},
    "urd": {"wikipedia": "ur", "sources": [
        {"url": "https://ur.wikipedia.org/", "type": "cultural", "description": "Urdu Wikipedia"},
        {"url": "https://www.jang.com.pk/", "type": "news", "description": "Jang — Urdu daily"},
        {"url": "https://www.bbc.com/urdu", "type": "news", "description": "BBC Urdu"},
    ]},
    "uzb": {"wikipedia": "uz", "sources": [
        {"url": "https://uz.wikipedia.org/", "type": "cultural", "description": "Uzbek Wikipedia (Latin)"},
        {"url": "https://www.gov.uz/uz", "type": "gov", "description": "Government of Uzbekistan"},
    ]},
    "uzs": {"wikipedia": None, "sources": [
        {"url": "https://www.pajhwok.com/", "type": "news", "description": "Pajhwok Afghan News"},
        {"url": "https://da.azadiradio.com/", "type": "news", "description": "Radio Azadi (Afghanistan)"},
        {"url": "https://www.bbc.com/uzbek", "type": "news", "description": "BBC Uzbek (Latin + Cyrillic; occasional Arabic-script)"},
        {"url": "https://www.voanews.com/", "type": "news", "description": "Voice of America (Uzbek service)"},
        {"url": "https://kabulnow.com/", "type": "news", "description": "Kabul Now — Afghan news"},
        {"url": "https://8am.media/", "type": "news", "description": "Hasht-e Subh — Afghan daily (multi-lang)"},
    ]},
    "vec": {"wikipedia": "vec", "sources": [
        {"url": "https://vec.wikipedia.org/", "type": "cultural", "description": "Venetian Wikipedia"},
        {"url": "https://www.raixevenete.com/", "type": "cultural", "description": "Raixe Venete — Venetian portal"},
    ]},
    "vie": {"wikipedia": "vi", "sources": [
        {"url": "https://vi.wikipedia.org/", "type": "cultural", "description": "Vietnamese Wikipedia"},
        {"url": "https://www.chinhphu.vn/", "type": "gov", "description": "Vietnamese Government Portal"},
        {"url": "https://tuoitre.vn/", "type": "news", "description": "Tuổi Trẻ"},
    ]},
    "wuu": {"wikipedia": "wuu", "sources": [
        {"url": "https://wuu.wikipedia.org/", "type": "cultural", "description": "Wu Chinese Wikipedia"},
    ]},
    "xho": {"wikipedia": "xh", "sources": [
        {"url": "https://xh.wikipedia.org/", "type": "cultural", "description": "Xhosa Wikipedia"},
        {"url": "https://www.jw.org/xh/", "type": "religious", "description": "jw.org Xhosa edition"},
    ]},
    "yor": {"wikipedia": "yo", "sources": [
        {"url": "https://yo.wikipedia.org/", "type": "cultural", "description": "Yoruba Wikipedia"},
        {"url": "https://www.bbc.com/yoruba", "type": "news", "description": "BBC Yoruba"},
    ]},
    "yue": {"wikipedia": "zh-yue", "sources": [
        {"url": "https://zh-yue.wikipedia.org/", "type": "cultural", "description": "Cantonese Wikipedia"},
        {"url": "https://www.rthk.hk/", "type": "news", "description": "RTHK — Hong Kong public broadcaster"},
    ]},
    "zho": {"wikipedia": "zh", "sources": [
        {"url": "https://zh.wikipedia.org/", "type": "cultural", "description": "Chinese Wikipedia"},
        {"url": "https://www.people.com.cn/", "type": "news", "description": "People's Daily Online"},
    ]},
    "zsm": {"wikipedia": "ms", "sources": [
        {"url": "https://ms.wikipedia.org/", "type": "cultural", "description": "Malay Wikipedia (Standard Malay)"},
        {"url": "https://www.utusan.com.my/", "type": "news", "description": "Utusan Malaysia"},
    ]},
    "zul": {"wikipedia": "zu", "sources": [
        {"url": "https://zu.wikipedia.org/", "type": "cultural", "description": "Zulu Wikipedia"},
        {"url": "https://www.isolezwe.co.za/", "type": "news", "description": "Isolezwe — Zulu daily"},
    ]},
}
