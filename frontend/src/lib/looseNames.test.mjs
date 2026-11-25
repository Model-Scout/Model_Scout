// Run: node src/lib/looseNames.test.mjs (Node 22.6+ strips the TypeScript types)
import assert from "node:assert/strict";
import { looseMentions } from "./looseNames.ts";

const titles = ["서울시 공공자전거 대여소별 이용정보(월별)", "전국 자전거도로 표준데이터"];
const pick = (text) => looseMentions(text, titles).map(([a, b]) => text.slice(a, b));

assert.deepEqual(pick("서울시 따릉이 대여소별 대여량 데이터로 시계열 예측 모델을 학습해요."), ["서울시 따릉이 대여소별 대여량 데이터"]);
assert.deepEqual(pick("서울시 공공자전거 이용정보를 넣어요."), ["서울시 공공자전거 이용정보"]);
assert.deepEqual(pick("전국 자전거도로 데이터는 근거로 써요."), ["전국 자전거도로 데이터"]);
// One shared word is not enough.
assert.deepEqual(pick("서울시 관광 코스를 추천해요."), []);
assert.deepEqual(pick("Qwen2.5-3B-Korean 생성 모델에 입력해요."), []);
console.log("looseNames ok");
