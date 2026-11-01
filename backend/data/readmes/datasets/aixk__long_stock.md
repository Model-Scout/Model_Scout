---
pretty_name: toss_stock_features
language:
- ko
configs:
- config_name: default
  data_files:
  - split: train
    path: train.csv
  - split: validation
    path: validation.csv
  - split: test
    path: test.csv
---

## Files

- all.csv / all.jsonl: 수집된 전체 bar와 계산 특징
- train.csv, validation.csv, test.csv: 20 bar 라벨이 완성된 시간 순서 분할
- supplemental/stocks.jsonl: 선택 종목 기본정보 원본
- supplemental/api_records.jsonl: 선택 종목과 시장 공통 API 응답 원본
- candidate_backtest.csv / candidate_backtest_metrics.json: 후보 규칙의 시간순 모의 체결 요약
- metadata.json: 수집 설정과 행 개수

## Method

- Interval: 1d
- Indicators: RSI(14), MACD(12,26,9), SMA(20/50/60), ATR(14), rolling volatility, Bollinger bands, volume MA/ratio/z-score, OBV, disparity, normalized MACD/ATR, price gaps and log turnover
- Signals: buy/sell candidate rules are heuristic features only. They are not guaranteed profitable signals.
- Candidate backtest: signals are observed after bar close, entry/exit use the next bar open, maximum holding is 20 bars, and trades do not cross dataset splits. Net return subtracts an illustrative 0.30% round-trip cost; replace it with actual fee, tax and slippage.
- Triple-barrier label: target_tp5_sl3_5bar is +1 if +5% is reached first, -1 if -3% is reached first, and 0 if neither is reached within five bars. If both barriers appear in one candle, stop loss is assumed first.
- Targets: forward returns at 1, 5 and 20 bars; target_up_5bar uses a zero-return threshold
- Splits use chronological timestamps and require a completed 20-bar forward label. Labels crossing train/validation boundaries are omitted.
- Per-stock investor flow fields are net buying volume, not monetary amount. Market index investor-trading responses in supplemental data contain buy/sell amounts.
- Historical investor data can have provider update times after the trading date. Check investor_updated_at before using flow fields in point-in-time backtests.
- Toss does not expose S&P 500, Nasdaq, VIX, US Treasury 10Y, fundamentals, earnings consensus, news sentiment, or search trends in this dataset. Add separately licensed providers for those features.

This dataset is for research and educational use. It is not financial advice. Past patterns do not guarantee future results.
