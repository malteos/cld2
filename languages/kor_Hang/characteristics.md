# Korean LID characteristics

## Script signals

- **Hangul syllable blocks** (U+AC00–U+D7A3). Any character in this range → Korean with extremely high precision.
- **Hangul jamo** (U+1100–U+11FF, U+3130–U+318F) appear in decomposed or IME states.
- Modern running text is essentially **all Hangul plus spaces and Western punctuation**; Han characters are rare and usually parenthetical.
- **Word spacing** (띄어쓰기) distinguishes Korean from Chinese and Japanese, which lack inter-word spaces.

## Top function words

은, 는, 이, 가, 을, 를, 의, 에, 에서, 으로, 로, 와, 과, 도, 만, 부터, 까지, 하고, 이다, 있다, 없다, 하다, 되다, 않다, 그리고, 하지만, 그러나, 그래서, 또한, 이, 그, 저, 이것, 그것, 저것, 나, 너, 우리, 저, 당신, 그, 그녀, 그들, 수, 것, 때, 등.

## N-gram / spelling patterns

- Verb/adjective endings: -습니다, -ㅂ니다, -어요, -아요, -었다, -았다, -는다, -다, -지요, -까.
- Sentence-final `습니다.` and `요.` are overwhelmingly Korean.
- Topic/subject particle collocations: `은 ` `는 ` `이 ` `가 ` at word boundaries.
- Common frames: `N + 은/는 N + 이다`, `N + 을/를 + V`, `N + 에서 + V`.

## Morphology hooks

- Particle allomorphy triggered by final consonant: 은/는, 이/가, 을/를, 과/와, 으로/로.
- Honorific infix -시-: 가시다, 하십니다, 드시다.
- Speech-level ending stacks: -었-습니다, -고 있-어요, -지 않-습니다.
- Pre-nominal participial relative endings -은 / -는 / -을 attaching to verbs.

## Punctuation / orthography quirks

- Uses Western-style full stops `.`, commas `,`, and question marks `?` (sometimes full-width).
- Ordinal/numerical markers often use Arabic digits plus Hangul counters (3명, 5개).
- North Korean orthography sometimes omits spaces within noun compounds and uses different Sino-Korean vocabulary; both styles still live in U+AC00–U+D7A3.
