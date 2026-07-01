"""Web-verified notable facts for specific coins.

Every sentence here is grounded in real sources (Royal Mint / Royal Mint
Museum, Wikipedia, NGC/PCGS, Change Checker, dealer records) — see the
`# src:` note on each block. These extra sentences give the corpus genuine
*semantic* content (history, errors, withdrawals) beyond the bare CSV fields,
so semantic retrieval and the LLM answer step have something real to work with.

Do not add unverified claims. Where a single primary figure doesn't exist,
the wording is deliberately qualified ("reported around", "estimates cite").
"""

from __future__ import annotations

# ---- facts appended to the prose of coins that DO exist in the CSV ----
# key = catalogue_ref
NOTABLE_FACTS: dict[str, list[str]] = {
    # src: Wikipedia 'Fifty pence (British coin)', Royal Mint
    "UK-50P-2009-KEW": [
        "With a circulation mintage of just 210,000 it is by far the lowest-"
        "mintage circulating 50p, which is why it is regarded as the rarest "
        "circulating fifty pence.",
        "The reverse by Christopher Le Brun shows the Great Pagoda at the Royal "
        "Botanic Gardens, Kew, encircled by a climbing plant, marking the "
        "gardens' 250th anniversary (dates 1759 and 2009).",
        "It was reissued in 2019 in the '50 Years of the 50p' set; those "
        "2019-dated coins are far more common than the 2009 circulation strike.",
    ],
    # src: NGC 'Counterfeit Detection: Lines Over Face Aquatics', RWB Auctions
    "UK-50P-2011-AQU": [
        "The Aquatics 50p is part of the 29-coin London 2012 Olympic and "
        "Paralympic series, each reverse showing a different sport.",
        "Jonathan Olliffe's original design showed water lines running across "
        "the swimmer's face; it was amended so the lines cleared the face.",
        "A limited number of early 'lines over face' coins reached circulation "
        "before the die change, making that variant the scarce, most valuable "
        "coin of the series (and heavily counterfeited).",
    ],
    # src: Wikipedia 'One pound coin', Cash4Coins / Royal Mint
    "UK-£1-1983-RA": [
        "This is the original round £1 coin, introduced in 1983 to replace the "
        "£1 note (the note was withdrawn in 1988).",
        "The round pound was demonetised and ceased to be legal tender on 15 "
        "October 2017, replaced by the 12-sided bimetallic £1 introduced on 28 "
        "March 2017.",
        "Counterfeiting drove the change: the Royal Mint estimated around 3% of "
        "round pounds in circulation were forgeries.",
    ],
    # src: Royal Mint 'The Royal Mint brings back Britannia', Numista
    "UK-£2-2015-BRI5": [
        "In 2015 the Royal Mint returned a standing Britannia design to the "
        "circulating £2, replacing Bruce Rushin's technology design.",
        "Antony Dufort's reverse shows a helmeted Britannia with shield and "
        "trident; the edge reads 'QUATUOR MARIA VINDICO' ('I will claim the "
        "four seas').",
        "The 2015 first-year Britannia £2 had a comparatively low circulation "
        "mintage (reported around 650,000).",
    ],
    # src: Wikipedia (Matthew Dent 2008 competition), Change Checker
    "UK-£1-2015-RS4": [
        "The Royal Shield definitive designs come from Matthew Dent's winning "
        "2008 competition entry: the 1p-50p each show a section of the Royal "
        "Shield that assemble together, while the £1 shows the whole shield.",
        "As demand for low-value coins fell, several years' 1p and 2p pieces "
        "were struck only for collector sets, not circulation, making those "
        "dates scarce outside sets.",
    ],
}

# ---- corpus overview document (id: "UK-OVERVIEW") ----
# src: Royal Mint Museum, Wikipedia 'Coins of the pound sterling'
OVERVIEW: list[str] = [
    "Decimalisation was announced in 1966 and took effect on Decimal Day, 15 "
    "February 1971, dividing one pound into 100 pence instead of the former 240.",
    "To strike the new decimal coinage the Royal Mint moved from London to "
    "Llantrisant, Wales, a site opened by Queen Elizabeth II in 1968; UK "
    "circulating coins are struck there today.",
    "Elizabeth II decimal coins carried successive obverse portraits: Arnold "
    "Machin (1968), Raphael Maklouf (1985), Ian Rank-Broadley (1998) and Jody "
    "Clark's fifth portrait (2015).",
    "For modern circulating coins the practical measure of rarity is the annual "
    "mintage: the fewer struck for circulation, the scarcer and more collectable.",
]

# ---- famous real coins that are NOT rows in the CSV, added as extra docs ----
# Each becomes its own Document in the corpus.
EXTRA_DOCS: list[dict] = [
    {
        # src: PCGS 'British Royal Mint Issues 2008 Mule Error Coins', Wikipedia
        "id": "UK-20P-2008-UNDATED",
        "meta": {"denomination": "20 Pence", "year": "2008", "rarity": "Rare",
                 "remarks": "Undated mule error", "section": "ELIZABETH II - TWENTY PENCE"},
        "text": (
            "The 2008 undated 20 pence is a famous British mule error. In 2008 "
            "the Royal Mint moved the date from the reverse to the obverse of "
            "the 20p as part of Matthew Dent's redesign, but a batch paired the "
            "new dateless reverse with an older obverse that also lacked a date, "
            "so the coins bear no year at all. It was the first undated British "
            "coin to enter circulation in more than 300 years. The Royal Mint "
            "published no definitive figure; numismatic estimates commonly cite "
            "roughly 50,000 to 250,000 affected coins. It is one of the most "
            "sought-after modern British error coins and trades well above face "
            "value."
        ),
    },
    {
        # src: Change Checker, RWB Auctions (1983 New Pence error)
        "id": "UK-2P-1983-NEWPENCE",
        "meta": {"denomination": "2 Pence", "year": "1983", "rarity": "Rare",
                 "remarks": "New Pence mule error", "section": "ELIZABETH II - TWO PENCE"},
        "text": (
            "The 1983 'New Pence' 2p is a scarce mule error. The 2p reverse "
            "wording had been changed from 'NEW PENCE' to 'TWO PENCE', but a "
            "small number of 1983 coins were struck using the old 'NEW PENCE' "
            "reverse die. These error coins were never released for general "
            "circulation; they appeared in Royal Mint souvenir sets, which is "
            "why they are scarce. Only the 1983-dated 'NEW PENCE' 2p carries a "
            "premium — earlier 'NEW PENCE' coins (up to 1981) are normal. "
            "Genuine examples sell for hundreds of pounds."
        ),
    },
]
