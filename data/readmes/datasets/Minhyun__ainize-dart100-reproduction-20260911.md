---
language:
- ko
tags:
- dart
- ainize
- question-answering
configs:
- config_name: dart-001-company_ceo_nm
  data_files:
  - split: train
    path: data/dart-001-company_ceo_nm.parquet
- config_name: dart-002-company_adres
  data_files:
  - split: train
    path: data/dart-002-company_adres.parquet
- config_name: dart-003-company_phn_no
  data_files:
  - split: train
    path: data/dart-003-company_phn_no.parquet
- config_name: dart-004-company_est_dt
  data_files:
  - split: train
    path: data/dart-004-company_est_dt.parquet
- config_name: dart-005-company_acc_mt
  data_files:
  - split: train
    path: data/dart-005-company_acc_mt.parquet
- config_name: dart-006-company_jurir_no
  data_files:
  - split: train
    path: data/dart-006-company_jurir_no.parquet
- config_name: dart-007-company_bizr_no
  data_files:
  - split: train
    path: data/dart-007-company_bizr_no.parquet
- config_name: dart-008-company_hm_url
  data_files:
  - split: train
    path: data/dart-008-company_hm_url.parquet
- config_name: dart-009-company_induty_code
  data_files:
  - split: train
    path: data/dart-009-company_induty_code.parquet
- config_name: dart-010-company_corp_name_eng
  data_files:
  - split: train
    path: data/dart-010-company_corp_name_eng.parquet
- config_name: dart-011-corpcode
  data_files:
  - split: train
    path: data/dart-011-corpcode.parquet
- config_name: dart-012-disclosure_annual_rcept
  data_files:
  - split: train
    path: data/dart-012-disclosure_annual_rcept.parquet
- config_name: dart-013-stock_total
  data_files:
  - split: train
    path: data/dart-013-stock_total.parquet
- config_name: dart-014-treasury_stock
  data_files:
  - split: train
    path: data/dart-014-treasury_stock.parquet
- config_name: dart-015-dividend_cash_per_share
  data_files:
  - split: train
    path: data/dart-015-dividend_cash_per_share.parquet
- config_name: dart-016-dividend_payout
  data_files:
  - split: train
    path: data/dart-016-dividend_payout.parquet
- config_name: dart-017-capital_change
  data_files:
  - split: train
    path: data/dart-017-capital_change.parquet
- config_name: dart-018-debt_issue
  data_files:
  - split: train
    path: data/dart-018-debt_issue.parquet
- config_name: dart-019-cp_balance
  data_files:
  - split: train
    path: data/dart-019-cp_balance.parquet
- config_name: dart-020-stb_balance
  data_files:
  - split: train
    path: data/dart-020-stb_balance.parquet
- config_name: dart-021-bond_balance
  data_files:
  - split: train
    path: data/dart-021-bond_balance.parquet
- config_name: dart-022-hybrid_balance
  data_files:
  - split: train
    path: data/dart-022-hybrid_balance.parquet
- config_name: dart-023-coco_balance
  data_files:
  - split: train
    path: data/dart-023-coco_balance.parquet
- config_name: dart-024-public_fund_use
  data_files:
  - split: train
    path: data/dart-024-public_fund_use.parquet
- config_name: dart-025-private_fund_use
  data_files:
  - split: train
    path: data/dart-025-private_fund_use.parquet
- config_name: dart-026-auditor
  data_files:
  - split: train
    path: data/dart-026-auditor.parquet
- config_name: dart-027-audit_opinion
  data_files:
  - split: train
    path: data/dart-027-audit_opinion.parquet
- config_name: dart-028-audit_fee
  data_files:
  - split: train
    path: data/dart-028-audit_fee.parquet
- config_name: dart-029-non_audit_service
  data_files:
  - split: train
    path: data/dart-029-non_audit_service.parquet
- config_name: dart-030-outside_directors
  data_files:
  - split: train
    path: data/dart-030-outside_directors.parquet
- config_name: dart-031-largest_shareholder
  data_files:
  - split: train
    path: data/dart-031-largest_shareholder.parquet
- config_name: dart-032-largest_shareholder_ratio
  data_files:
  - split: train
    path: data/dart-032-largest_shareholder_ratio.parquet
- config_name: dart-033-largest_shareholder_change
  data_files:
  - split: train
    path: data/dart-033-largest_shareholder_change.parquet
- config_name: dart-034-minority_shareholders
  data_files:
  - split: train
    path: data/dart-034-minority_shareholders.parquet
- config_name: dart-035-executives
  data_files:
  - split: train
    path: data/dart-035-executives.parquet
- config_name: dart-036-employees
  data_files:
  - split: train
    path: data/dart-036-employees.parquet
- config_name: dart-037-employee_avg_salary
  data_files:
  - split: train
    path: data/dart-037-employee_avg_salary.parquet
- config_name: dart-038-unregistered_exec_pay
  data_files:
  - split: train
    path: data/dart-038-unregistered_exec_pay.parquet
- config_name: dart-039-director_pay_approved
  data_files:
  - split: train
    path: data/dart-039-director_pay_approved.parquet
- config_name: dart-040-director_pay_total
  data_files:
  - split: train
    path: data/dart-040-director_pay_total.parquet
- config_name: dart-041-director_pay_by_type
  data_files:
  - split: train
    path: data/dart-041-director_pay_by_type.parquet
- config_name: dart-042-exec_pay_individual
  data_files:
  - split: train
    path: data/dart-042-exec_pay_individual.parquet
- config_name: dart-043-exec_pay_individual_v2
  data_files:
  - split: train
    path: data/dart-043-exec_pay_individual_v2.parquet
- config_name: dart-044-top5_pay
  data_files:
  - split: train
    path: data/dart-044-top5_pay.parquet
- config_name: dart-045-top5_pay_v2
  data_files:
  - split: train
    path: data/dart-045-top5_pay_v2.parquet
- config_name: dart-046-investments_other
  data_files:
  - split: train
    path: data/dart-046-investments_other.parquet
- config_name: dart-047-fs_revenue
  data_files:
  - split: train
    path: data/dart-047-fs_revenue.parquet
- config_name: dart-048-fs_operating_income
  data_files:
  - split: train
    path: data/dart-048-fs_operating_income.parquet
- config_name: dart-049-fs_net_income
  data_files:
  - split: train
    path: data/dart-049-fs_net_income.parquet
- config_name: dart-050-fs_total_assets
  data_files:
  - split: train
    path: data/dart-050-fs_total_assets.parquet
- config_name: dart-051-fs_total_liabilities
  data_files:
  - split: train
    path: data/dart-051-fs_total_liabilities.parquet
- config_name: dart-052-fs_total_equity
  data_files:
  - split: train
    path: data/dart-052-fs_total_equity.parquet
- config_name: dart-053-fs_current_assets
  data_files:
  - split: train
    path: data/dart-053-fs_current_assets.parquet
- config_name: dart-054-fs_current_liabilities
  data_files:
  - split: train
    path: data/dart-054-fs_current_liabilities.parquet
- config_name: dart-055-fs_noncurrent_assets
  data_files:
  - split: train
    path: data/dart-055-fs_noncurrent_assets.parquet
- config_name: dart-056-fs_capital_stock
  data_files:
  - split: train
    path: data/dart-056-fs_capital_stock.parquet
- config_name: dart-057-fs_multi_revenue
  data_files:
  - split: train
    path: data/dart-057-fs_multi_revenue.parquet
- config_name: dart-058-fs_all_cashflow
  data_files:
  - split: train
    path: data/dart-058-fs_all_cashflow.parquet
- config_name: dart-059-xbrl_taxonomy
  data_files:
  - split: train
    path: data/dart-059-xbrl_taxonomy.parquet
- config_name: dart-060-idx_net_margin
  data_files:
  - split: train
    path: data/dart-060-idx_net_margin.parquet
- config_name: dart-061-idx_debt_ratio
  data_files:
  - split: train
    path: data/dart-061-idx_debt_ratio.parquet
- config_name: dart-062-idx_revenue_growth
  data_files:
  - split: train
    path: data/dart-062-idx_revenue_growth.parquet
- config_name: dart-063-idx_asset_turnover
  data_files:
  - split: train
    path: data/dart-063-idx_asset_turnover.parquet
- config_name: dart-064-idx_multi_roe
  data_files:
  - split: train
    path: data/dart-064-idx_multi_roe.parquet
- config_name: dart-065-major_holder
  data_files:
  - split: train
    path: data/dart-065-major_holder.parquet
- config_name: dart-066-insider_holding
  data_files:
  - split: train
    path: data/dart-066-insider_holding.parquet
- config_name: dart-067-asset_transfer_putback
  data_files:
  - split: train
    path: data/dart-067-asset_transfer_putback.parquet
- config_name: dart-068-default_occurrence
  data_files:
  - split: train
    path: data/dart-068-default_occurrence.parquet
- config_name: dart-069-business_suspension
  data_files:
  - split: train
    path: data/dart-069-business_suspension.parquet
- config_name: dart-070-rehabilitation
  data_files:
  - split: train
    path: data/dart-070-rehabilitation.parquet
- config_name: dart-071-dissolution
  data_files:
  - split: train
    path: data/dart-071-dissolution.parquet
- config_name: dart-072-paid_in_capital_increase
  data_files:
  - split: train
    path: data/dart-072-paid_in_capital_increase.parquet
- config_name: dart-073-bonus_issue
  data_files:
  - split: train
    path: data/dart-073-bonus_issue.parquet
- config_name: dart-074-paid_bonus_issue
  data_files:
  - split: train
    path: data/dart-074-paid_bonus_issue.parquet
- config_name: dart-075-capital_reduction
  data_files:
  - split: train
    path: data/dart-075-capital_reduction.parquet
- config_name: dart-076-bank_management_start
  data_files:
  - split: train
    path: data/dart-076-bank_management_start.parquet
- config_name: dart-077-lawsuit
  data_files:
  - split: train
    path: data/dart-077-lawsuit.parquet
- config_name: dart-078-overseas_listing_decision
  data_files:
  - split: train
    path: data/dart-078-overseas_listing_decision.parquet
- config_name: dart-079-overseas_delisting_decision
  data_files:
  - split: train
    path: data/dart-079-overseas_delisting_decision.parquet
- config_name: dart-080-overseas_listing
  data_files:
  - split: train
    path: data/dart-080-overseas_listing.parquet
- config_name: dart-081-overseas_delisting
  data_files:
  - split: train
    path: data/dart-081-overseas_delisting.parquet
- config_name: dart-082-convertible_bond
  data_files:
  - split: train
    path: data/dart-082-convertible_bond.parquet
- config_name: dart-083-bond_with_warrant
  data_files:
  - split: train
    path: data/dart-083-bond_with_warrant.parquet
- config_name: dart-084-exchangeable_bond
  data_files:
  - split: train
    path: data/dart-084-exchangeable_bond.parquet
- config_name: dart-085-bank_management_stop
  data_files:
  - split: train
    path: data/dart-085-bank_management_stop.parquet
- config_name: dart-086-writedown_coco
  data_files:
  - split: train
    path: data/dart-086-writedown_coco.parquet
- config_name: dart-087-treasury_acquisition
  data_files:
  - split: train
    path: data/dart-087-treasury_acquisition.parquet
- config_name: dart-088-treasury_disposal
  data_files:
  - split: train
    path: data/dart-088-treasury_disposal.parquet
- config_name: dart-089-treasury_trust_contract
  data_files:
  - split: train
    path: data/dart-089-treasury_trust_contract.parquet
- config_name: dart-090-treasury_trust_cancel
  data_files:
  - split: train
    path: data/dart-090-treasury_trust_cancel.parquet
- config_name: dart-091-business_acquisition
  data_files:
  - split: train
    path: data/dart-091-business_acquisition.parquet
- config_name: dart-092-business_transfer
  data_files:
  - split: train
    path: data/dart-092-business_transfer.parquet
- config_name: dart-093-tangible_asset_acquisition
  data_files:
  - split: train
    path: data/dart-093-tangible_asset_acquisition.parquet
- config_name: dart-094-tangible_asset_transfer
  data_files:
  - split: train
    path: data/dart-094-tangible_asset_transfer.parquet
- config_name: dart-095-other_stock_acquisition
  data_files:
  - split: train
    path: data/dart-095-other_stock_acquisition.parquet
- config_name: dart-096-other_stock_transfer
  data_files:
  - split: train
    path: data/dart-096-other_stock_transfer.parquet
- config_name: dart-097-stock_bond_acquisition
  data_files:
  - split: train
    path: data/dart-097-stock_bond_acquisition.parquet
- config_name: dart-098-stock_bond_transfer
  data_files:
  - split: train
    path: data/dart-098-stock_bond_transfer.parquet
- config_name: dart-099-merger
  data_files:
  - split: train
    path: data/dart-099-merger.parquet
- config_name: dart-100-spinoff
  data_files:
  - split: train
    path: data/dart-100-spinoff.parquet
---

# DART task datasets for Ainize reproduction

This bundle preserves 100 distinct task configurations from the existing DART-derived datasets. Each JSONL file is byte-identical to its authenticated Ainize canonical download. The manifest links configuration names, row counts, SHA256 values and Ainize dataset IDs.

Source: Financial Supervisory Service Open DART, https://opendart.fss.or.kr/. These are historical disclosure-derived answers, not a promise of current company information or financial advice. Source reuse terms and publisher rights must be confirmed before public upload; no new license is asserted by this packaging step.

The train split contains the question/answer records used by Ainize. alt_prompt, where present, is an alternate question for the same fact and is not an independent dataset. A dataset ID is not a trained model ID. Uploading this repository does not demonstrate 100 successful teach jobs, inference support, a model deployment or a public Ainize listing.

After upload, verify the Hub commit and every configuration by downloading at that exact revision. Do not treat this README or the local manifest as proof of remote publication.

Format reference: https://huggingface.co/docs/datasets/en/repository_structure

The HF configurations read typed Parquet files so date-like answers and leading zeros remain strings. The original canonical JSONL files are also retained byte-for-byte; the manifest binds both formats.
