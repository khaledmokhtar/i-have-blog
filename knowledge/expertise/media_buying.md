# Media Buying & Performance Marketing Frameworks

## The ROAS Illusion vs. Contribution Margin

Never judge performance on in-platform ROAS alone:
- Platforms claim 100% credit for conversions they touch.
- In-platform ROAS does not deduct COGS, fulfillment, payment fees, or platform slippage.
- True health is measured via Blended Marketing Efficiency Ratio:
  $$\text{MER} = \frac{\text{Total Net Revenue}}{\text{Total Paid Ad Spend}}$$

## Signal Quality & Server-Side Tracking
- Browser pixels lose 20–35% of events due to ad blockers, browser privacy, and Safari ITP.
- Conversions API (CAPI) is essential, but ONLY when deduplicated via unique `event_id`.
- Without deduplication, platforms optimize for artificial volume, skewing algorithmic bidding.
