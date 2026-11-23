# CHALIS cousin-pair discriminators

Each TSV lists frequent words (top 1500 of one language's 10k list) that do **not** occur anywhere in the other language's 10k list. These are high-precision cues for telling cousin languages apart. `*_nodiac` compares diacritic-stripped forms; `*_roman` compares English-style romanizations of Cyrillic languages.

Caveat: vocabularies come from different corpora (wordfreq vs. OpenSubtitles for gl/sr), so a few 'markers' reflect corpus differences rather than the language.

## ces_Latn vs slk_Latn  -> `discriminators/ces-slk.tsv`

- **ces_Latn markers:** jsem, jako, jsou, když, mě, byl, jsme, které, který, není, bylo, ještě, byla, být, pak, při, která, před, bych, protože, první, podle, pokud, něco, další
- **slk_Latn markers:** ako, som, čo, bol, pre, sú, ak, alebo, nie, ich, len, vo, keď, ktorý, ktoré, pri, bola, ktorá, veľmi, bolo, ešte, zo, podľa, viac, boli
- **Shared top-200 words (not diagnostic):** a, v, na, je, to, že, s, z, si, do, ale, o, i, tak, za, k, po, by, už, od, mi, bude, u, má, jeho, až, aby, ani, tam, toho, ten, kde, mám, ho, tu, tom, nás, vám, vás, bez

## ces_Latn vs slk_Latn (nodiac)  -> `discriminators/ces-slk_nodiac.tsv`

- **ces_Latn markers:** jsem, jako, jsou, kdyz, byl, jsme, ktere, ktery, bylo, jeste, byla, pak, ktera, bych, protoze, prvni, podle, pokud, neco, ted, mezi, jste, proc, sve, jejich
- **slk_Latn markers:** ako, som, bol, pre, ak, alebo, nie, ich, len, vo, ked, ktory, ktore, bola, ktora, bolo, este, zo, podla, viac, medzi, moze, tiez, pozri, pocas
- **Shared top-200 words (not diagnostic):** a, v, na, je, to, ze, s, z, si, do, ale, o, i, tak, za, co, k, po, by, uz, od, mi, bude, ja, u, ma, jeho, az, aby, byt, ani, pri, tam, toho, ten, kde, mam, ho, pred, tu

## spa_Latn vs cat_Latn  -> `discriminators/spa-cat.tsv`

- **spa_Latn markers:** sus, todo, cuando, fue, muy, también, tiene, porque, así, años, bien, puede, hasta, hacer, ahora, esto, vez, hace, nada, donde, parte, tiempo, uno, mejor, mucho
- **cat_Latn markers:** els, amb, és, més, dels, hi, aquest, però, tot, fer, seu, aquesta, molt, als, seva, també, ens, són, anys, això, estat, quan, ara, fins, què
- **Shared top-200 words (not diagnostic):** de, la, que, el, en, a, no, un, se, es, del, una, lo, al, si, o, ha, ser, sobre, nos, dos, entre, era, ni, tan, vida, han, cada, va, les, gran, contra, país, casa, forma, he, aquí, sí, tres, poder

## por_Latn vs glg_Latn  -> `discriminators/por-glg.tsv`

- **por_Latn markers:** em, não, uma, com, mas, você, tem, são, ele, muito, isso, já, também, quando, pela, bem, pessoas, tudo, fazer, minha, quem, sem, assim, depois, estão
- **glg_Latn markers:** unha, máis, pero, aquí, xa, hai, cando, súa, miña, así, moi, ten, facer, teño, quen, lle, xente, señor, tamén, sen, podo, estaba, día, aínda, che
- **Shared top-200 words (not diagnostic):** de, a, o, que, e, do, da, é, para, no, se, na, por, os, eu, como, as, mais, dos, foi, ao, me, ser, seu, das, ou, nos, está, meu, ela, vai, só, sobre, mesmo, pode, te, ter, anos, todos, agora

## spa_Latn vs glg_Latn  -> `discriminators/spa-glg.tsv`

- **spa_Latn markers:** sus, ya, yo, hay, fue, muy, también, tiene, puede, hasta, hacer, hace, ni, donde, mejor, mucho, mismo, siempre, tengo, después, estoy, mas, otro, otros, otra
- **glg_Latn markers:** unha, máis, ao, iso, meu, xa, hai, cando, ou, só, súa, miña, seu, agora, moi, onde, facer, foi, teño, isto, quen, vai, estou, lle, pode
- **Shared top-200 words (not diagnostic):** de, que, el, en, a, no, un, se, por, es, con, para, como, me, si, pero, te, o, este, esta, todo, ser, son, está, sobre, todos, nos, porque, así, dos, entre, era, vez, nada, parte, algo, día, tan, ver, vida

## spa_Latn vs por_Latn  -> `discriminators/spa-por.tsv`

- **spa_Latn markers:** pero, cuando, hay, fue, muy, también, eso, tiene, qué, así, años, bien, puede, hasta, hacer, ahora, esto, hace, donde, tiempo, día, uno, mejor, mucho, tan
- **por_Latn markers:** não, um, uma, mais, foi, ao, você, seu, sua, tem, ou, ele, muito, isso, já, também, quando, meu, ela, vai, só, pela, bem, até, mesmo
- **Shared top-200 words (not diagnostic):** de, la, que, a, no, se, por, para, como, me, te, o, este, esta, todo, ser, está, sobre, todos, nos, porque, dos, entre, desde, era, vez, nada, parte, ver, vida, e, cada, estado, mundo, mas, menos, nunca, antes, durante, contra

## dan_Latn vs nob_Latn  -> `discriminators/dan-nob.tsv`

- **dan_Latn markers:** sig, efter, mig, hvad, noget, dig, lige, blev, bliver, havde, lidt, vores, ind, gør, blive, igen, fik, nogle, gøre, måske, siger, altid, anden, uden, andet
- **nob_Latn markers:** seg, noe, noen, ble, etter, hadde, deg, opp, gjør, litt, bli, enn, gjøre, mye, igjen, mot, fikk, oss, uten, dere, sier, kanskje, bra, vet, annet
- **Shared top-200 words (not diagnostic):** i, og, er, det, at, en, til, på, jeg, har, for, ikke, med, den, der, de, du, kan, som, så, et, var, vi, om, han, fra, men, skal, ved, vil, også, være, hvor, man, hvis, eller, her, alle, godt, da

## nld_Latn vs dan_Latn  -> `discriminators/nld-dan.tsv`

- **nld_Latn markers:** het, dat, voor, je, met, niet, zijn, maar, aan, hij, ook, ze, door, uit, bij, was, wat, heeft, nog, deze, hebben, meer, zo, geen, mijn
- **dan_Latn markers:** og, det, til, på, jeg, har, ikke, med, så, fra, skal, ved, vil, også, være, hvor, hvis, sig, efter, mig, eller, hvad, ud, godt, meget
- **Shared top-200 words (not diagnostic):** de, en, op, er, om, dit, over, kan, nu, hun, dag, alle, ja, man, af, hele

## bul_Cyrl vs mkd_Cyrl  -> `discriminators/bul-mkd.tsv`

- **bul_Cyrl markers:** ще, това, като, много, най, към, съм, няма, след, през, аз, които, как, той, трябва, всички, който, във, което, един, още, със, когато, този, българия
- **mkd_Cyrl markers:** од, ќе, што, дека, како, ја, тоа, кој, многу, сите, тој, која, ова, јас, еден, нема, сум, биде, треба, македонија, повеќе, уште, тие, каде, луѓе
- **Shared top-200 words (not diagnostic):** на, и, да, е, за, се, не, си, по, а, ми, но, до, го, има, му, ако, може, ти, ли, само, г, при, ви, или, ни, те, така, време, ги, години, една, ме, сега, без, беше, им, година, едно, ден

## rus_Cyrl vs ukr_Cyrl  -> `discriminators/rus-ukr.tsv`

- **rus_Cyrl markers:** была, году, себя, тебя, области, жизни, всегда, между, этой, здесь, однако, её, несколько, своей, сказал, тогда, место, хорошо, которых, является, вместе, времени, лишь, свои, человека
- **ukr_Cyrl markers:** що, це, як, від, україни, але, він, його, ви, ще, які, під, вже, коли, якщо, або, року, було, вони, із, мене, щоб, мені, чи, який
- **Shared top-200 words (not diagnostic):** в, и, на, не, с, я, по, а, за, для, о, к, то, у, от, все, так, же, до, при, вас, того, просто, ну, без, нас, там, м, раз, один, через, них, сша, день, себе, тебе, два, людей, люди, тут

## rus_Cyrl vs bul_Cyrl  -> `discriminators/rus-bul.tsv`

- **rus_Cyrl markers:** что, это, для, его, он, же, мы, ты, только, был, если, когда, было, мне, меня, уже, еще, бы, их, они, будет, время, кто, года, чтобы
- **bul_Cyrl markers:** ще, са, това, като, най, има, ако, към, може, съм, няма, през, аз, които, ви, какво, трябва, всички, който, във, което, един, още, така, със
- **Shared top-200 words (not diagnostic):** в, и, на, не, с, я, по, а, как, за, но, то, у, от, все, до, или, при, под, вас, да, просто, г, без, нас, ни, там, ли, им, между, себе, два, него, много, над, три, около

## srp_Cyrl vs mkd_Cyrl  -> `discriminators/srp-mkd.tsv`

- **srp_Cyrl markers:** шта, није, ово, га, смо, ће, тако, нисам, могу, био, још, реду, бити, који, кад, ћу, хвала, из, мислим, знаш, можда, их, више, онда, сада
- **mkd_Cyrl markers:** во, ќе, дека, ги, тоа, кои, многу, сите, така, јас, еден, сум, биде, македонија, повеќе, уште, тие, една, сега, каде, луѓе, оваа, таа, кај, додека
- **Shared top-200 words (not diagnostic):** да, не, се, и, на, ти, ми, за, си, ли, што, ја, само, ме, те, од, а, би, како, добро, ако, знам, сте, па, нешто, било, има, или, до, треба, му, била, нема, нас, мене, она, тебе, сад, ни, може

## rus_Cyrl vs ukr_Cyrl (roman)  -> `discriminators/rus-ukr_roman.tsv`

- **rus_Cyrl markers:** ego, esli, kogda, ili, oni, goda, byli, byla, gde, rossii, togo, etogo, godu, sebya, odin, tebya, vsego, segodnya, nikh, eti, zhizni, vsegda, mezhdu, etoy, zdes
- **ukr_Cyrl markers:** shcho, tse, yak, ukrayiny, ale, vin, yoho, ye, shche, yaki, pid, vzhe, koly, yakshcho, abo, roku, bulo, vony, mene, shchob, meni, chy, yakyy, buv, bude
- **Shared top-200 words (not diagnostic):** v, i, na, ne, s, ya, po, a, iz, za, dlya, o, k, to, u, ot, vse, tak, zhe, my, do, ty, uzhe, by, vy, vas, prosto, nu, bez, nas, ni, tam, m, raz, teper, cherez, ssha, oblasti, den, sebe

## rus_Cyrl vs bul_Cyrl (roman)  -> `discriminators/rus-bul_roman.tsv`

- **rus_Cyrl markers:** chto, dlya, ego, zhe, ty, tolko, byl, esli, kogda, bylo, mne, menya, uzhe, eshche, ikh, oni, budet, vremya, kto, goda, chtoby, est, ona, vy, mozhet
- **bul_Cyrl markers:** shte, sa, tova, kato, nay, ima, ako, kam, mozhe, nyama, prez, az, koito, kakvo, tryabva, vsichki, koyto, vav, koeto, edin, oshte, taka, sas, vreme, kogato
- **Shared top-200 words (not diagnostic):** v, i, na, ne, s, ya, po, a, kak, eto, za, no, to, u, ot, vse, do, ili, pri, pod, vas, da, prosto, g, bez, nas, ni, tam, li, den, im, mezhdu, sebe, dva, nego, mnogo, nad, tri, sam, okolo

## bul_Cyrl vs mkd_Cyrl (roman)  -> `discriminators/bul-mkd_roman.tsv`

- **bul_Cyrl markers:** shte, tova, kato, mnogo, nay, kam, nyama, sled, prez, az, koito, kak, toy, tryabva, vsichki, koyto, vav, koeto, edin, oshte, sas, kogato, tozi, ya, balgariya
- **mkd_Cyrl markers:** od, kje, deka, kako, ja, toa, koj, mnogu, site, toj, koja, ova, jas, eden, nema, sum, bide, treba, makedonija, povekje, ushte, tie, lugje, ovoj, ovaa
- **Shared top-200 words (not diagnostic):** na, i, da, e, za, se, ne, si, po, a, mi, no, do, go, ima, mu, ako, mozhe, ti, li, samo, g, pri, vi, ili, ni, te, taka, vreme, gi, godini, edna, neshto, me, sega, bez, beshe, im, godina, edno

## srp_Cyrl vs mkd_Cyrl (roman)  -> `discriminators/srp-mkd_roman.tsv`

- **srp_Cyrl markers:** sta, nije, ovo, ga, smo, ce, tako, nisam, mogu, bio, zasto, jos, nesto, redu, biti, koji, kad, cu, hvala, iz, mislim, znas, mozda, ih, vise
- **mkd_Cyrl markers:** vo, kje, shto, deka, gi, toa, koi, mnogu, beshe, site, taka, mozhe, jas, eden, sum, bide, makedonija, povekje, ushte, tie, edna, sega, kade, lugje, ovaa
- **Shared top-200 words (not diagnostic):** da, ne, se, i, na, ti, mi, za, si, li, ja, samo, me, te, od, a, bi, kako, dobro, ako, znam, ste, pa, bilo, ima, ili, do, treba, mu, bila, nema, nas, mene, ona, tebe, sad, ni, imam, vi, po

## rus_Cyrl vs srp_Cyrl (roman)  -> `discriminators/rus-srp_roman.tsv`

- **rus_Cyrl markers:** chto, ya, kak, dlya, ot, vse, tak, zhe, ty, tolko, byl, kogda, bylo, mne, menya, uzhe, eshche, ikh, budet, vremya, kto, goda, chtoby, est, vo
- **srp_Cyrl markers:** je, ja, sa, nije, ovo, od, kako, ako, sve, smo, kao, ce, tako, znam, nisam, ste, ovde, bio, zasto, jos, nesto, bilo, redu, biti, koji
- **Shared top-200 words (not diagnostic):** i, na, ne, s, po, a, iz, za, o, to, u, on, do, ili, oni, ona, gde, vas, da, bez, nas, ni, li, im, tebe, dva, nego, mnogo, nam, vam, sam

