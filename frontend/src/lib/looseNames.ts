// Loose dataset-name matching for LLM sentences that paraphrase a title
// ("서울시 따릉이 대여소별 대여량 데이터" for "서울시 공공자전거 대여소별 이용정보(월별)").

const JOSA = /(으로|에서|로|를|을|는|은|이|가|와|과|의|에|도)$/;
const DATA_NOUN = /(데이터셋|데이터|정보|현황|이력|목록|통계|자료)$/;

const stem = (word: string) => word.replace(/[.,!?·"'“”()[\]]/g, "").replace(JOSA, "");

/** A title's distinctive words: no parenthetical, no bare data nouns like "데이터". */
function titleTokens(title: string) {
  return title.replace(/\(.*?\)|\[.*?\]/g, " ").split(/[\s/_·,-]+/)
    .filter((t) => t.length >= 2 && !/^(데이터셋|데이터|정보|자료)$/.test(t));
}

function matches(word: string, tokens: string[]) {
  const s = stem(word);
  return s.length < 2 ? undefined : tokens.find((t) => t.includes(s) || s.includes(t));
}

/** Character ranges [start, end) of loose mentions; each range covers at least two of a title's words. */
export function looseMentions(text: string, titles: string[]): [number, number][] {
  const words = [...text.matchAll(/\S+/g)].map((m) => ({ word: m[0], start: m.index!, end: m.index! + m[0].length }));
  const found: [number, number][] = [];
  for (let i = 0; i < words.length; i++) {
    for (const title of titles) {
      const tokens = titleTokens(title);
      if (tokens.length < 2 || !matches(words[i].word, tokens)) continue;
      const hit = new Set<string>();
      let last = i;
      // Extend over matching words, allowing one unmatched word in between (e.g. "따릉이" for "공공자전거").
      for (let j = i; j < words.length && j - last <= 2; j++) {
        const token = matches(words[j].word, tokens);
        if (token) { hit.add(token); last = j; }
      }
      if (hit.size < 2) continue;
      // Take in a trailing data noun such as "대여량 데이터로", so the whole name is coloured.
      for (let j = last + 1; j <= last + 2 && j < words.length; j++) {
        if (DATA_NOUN.test(stem(words[j].word))) { last = j; break; }
      }
      const tail = words[last].word.length - stem(words[last].word).length;
      found.push([words[i].start, words[last].end - tail]);
      i = last;
      break;
    }
  }
  return found;
}
