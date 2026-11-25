import hypergraph_search as hs


def entity(title, source="data_go_kr"):
    return {"title": title, "name": title, "source": source}


def test_generic_words_are_not_topic_words():
    assert hs.title_topic_words(entity("서울시 가로수 위치정보"), ["주유소", "위치"]) == []
    assert hs.title_topic_words(entity("전국주유소표준데이터"), ["주유소", "위치"]) == ["주유소"]
    assert "domain/location" not in hs.concepts_from_terms(["위치", "가격"])


def test_region_alone_earns_no_bonus():
    off_topic = entity("충청북도_지적통계")
    assert hs.keyword_score(off_topic, ["충청북도", "공중화장실"])[0] == 0.0
    # Topic fit from the title or from the dense match both earn the region bonus.
    assert hs.keyword_score(entity("충청북도_공중화장실 현황"), ["충청북도", "공중화장실"])[0] > hs.REGION_MATCH_BONUS
    assert hs.keyword_score(off_topic, ["충청북도", "공중화장실"], on_topic=True)[0] == hs.REGION_MATCH_BONUS


def test_region_words_with_a_suffix_are_regions():
    assert [hs.region_of(w) for w in ["서울시", "서울특별시", "경기도", "충청북도", "부산광역시", "도시", "버스"]] == [
        "서울", "서울", "경기", "충북", "부산", None, None]
    seoul = entity("서울시 버스도착정보", source="seoul_open_data")
    assert hs.keyword_score(seoul, ["서울시", "버스"])[0] == hs.KEYWORD_BONUS + hs.REGION_MATCH_BONUS


def test_letters_of_a_region_inside_another_word_are_not_a_region():
    titles = ["식육부산물전문판매업 현황", "환경기초시설 정보제공서비스", "소상공인 경기동향(BSI)",
              "전국기능경기대회 개최현황", "서울올림픽기념국민체육진흥공단_전국체육시설 정보"]
    assert [hs.dataset_regions({"title": t}) for t in titles] == [set()] * 5
    assert hs.dataset_regions({"title": "부산광역시_식육부산물 판매업"}) == {"부산"}
    assert hs.dataset_regions({"title": "인천국제공항공사_주차 정보"}) == {"인천"}
    assert hs.dataset_regions({"title": "경기도_환경기초시설"}) == {"경기"}


def test_a_stuck_embedding_call_fails_fast(monkeypatch):
    import openai

    seen = {}

    class Client:
        def __init__(self, **kwargs):
            seen.update(kwargs)
            raise TimeoutError

    monkeypatch.setattr(openai, "OpenAI", Client)
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    try:
        hs._embed_query("timeout test", "model")
    except TimeoutError:
        pass
    assert seen["timeout"] <= 30 and seen["max_retries"] <= 1
