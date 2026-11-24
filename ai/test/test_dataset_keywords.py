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
