# Endpoint-specific prompt templates
CONGRESS_TRADES_PROMPT = """Analyze Congress member trading activity with special focus on:

1. Million-Dollar Transactions:
   - Identify and quantify all trades >$1M with exact amounts
   - Track member-specific large position changes
   - Note timing of major transactions relative to market events
   - Calculate net position changes for top traders

2. Member Analysis:
   - Identify members with largest total trading volume
   - Calculate buy/sell ratios for active members
   - Track multi-stock trading strategies
   - Note coordinated trading patterns across members

3. Sector Impact:
   - Calculate net flows by sector
   - Identify sector rotation patterns
   - Track unusual sector concentrations
   - Note consensus moves among multiple members

Requirements:
- First sentence must state the largest transaction(s) with exact dollar amount and member name
- Second sentence must provide sector-level insight and clear trading recommendation
- Use precise amounts for trades over $1M (e.g., "$5.2M AAPL sale by Pelosi")
- Keep total response under 75 words"""

GREEK_FLOW_PROMPT = """Analyze the options Greek flow data, focusing on:

1. Delta Flow Analysis:
   - Calculate net directional exposure (calls vs puts)
   - Identify stocks with highest absolute delta flow
   - Note any significant changes in flow direction

2. Volatility Exposure:
   - Measure net vega exposure across sectors
   - Compare OTM vs ITM option activity
   - Flag unusual volatility positioning

3. Trading Patterns:
   - Calculate volume-weighted average strike prices
   - Identify clustering of similar positions
   - Note any significant hedging activity

Provide a concise insight focusing on:
1. The most significant Greek flow metric and its magnitude
2. Whether the positioning suggests directional or volatility trades
3. Specific implications for price movement risk"""

EARNINGS_PROMPT = """Analyze earnings reports and market reactions, focusing on:

1. Earnings Performance:
   - Calculate average earnings surprise percentage
   - Identify sectors with highest beat/miss rates
   - Compare actual vs expected results

2. Price Impact Analysis:
   - Measure average price movement post-earnings
   - Calculate correlation between surprise and price change
   - Identify outlier reactions

3. Sector Patterns:
   - Compare sector-specific performance trends
   - Note any sector rotation implications
   - Flag unusual price reaction patterns

Provide a concise insight focusing on:
1. The most significant earnings trend by sector
2. Correlation between surprises and price movements
3. Actionable trading opportunities around earnings"""

INSIDER_TRADING_PROMPT = """Analyze insider trading patterns, focusing on:

1. Transaction Analysis:
   - Calculate net buying/selling by insider role
   - Identify clusters of similar transactions
   - Compare transaction sizes to historical averages

2. Sector Patterns:
   - Measure net insider sentiment by sector
   - Identify sectors with unusual activity
   - Note any sector rotation signals

3. Timing Analysis:
   - Flag unusual timing patterns
   - Compare to market events/earnings
   - Note any correlation with price movements

Provide a concise insight focusing on:
1. The most significant insider trading pattern
2. Key sectors or companies with notable activity
3. Actionable implications for investors"""

PREMIUM_FLOW_PROMPT = """Analyze market-wide premium flow, focusing on:

1. Flow Analysis:
   - Calculate net premium flow by sector
   - Compare call vs put premium ratios
   - Track minute-by-minute changes (for intraday data)
   - Monitor daily accumulation patterns (for daily data)
   - Identify unusual volume/premium patterns

2. Historical Context:
   - Compare current flows to historical ranges
   - Note when metrics exceed historical thresholds
   - Track trend changes vs historical patterns
   - Flag divergences from typical behavior

3. Sector Activity:
   - Rank sectors by total premium flow
   - Note significant changes in sentiment
   - Flag unusual concentration patterns
   - Compare sector rotation patterns

4. Market Implications:
   - Evaluate overall market sentiment
   - Identify potential sector rotation
   - Note any hedging patterns
   - Project short-term directional bias

Required Format:
1. Start with "30-day High: $X.XM" using the highest premium value from historical data
2. For intraday data, include timestamp in ET (e.g., "As of 14:30 ET:")
3. Then provide analysis in 2-3 sentences:
   - First sentence: State the largest premium flow with exact amount and timing
   - Second sentence: Compare to historical patterns and thresholds
   - Third sentence: Explain potential catalysts and provide clear trading recommendation

Example:
"30-day High: $15.2M. As of 14:30 ET: Tech sector leads with $5.2M net call premium, representing 65% of 30-day high. This surge in premium flow suggests institutional accumulation, with adjacent sector pairs showing correlated bullish activity. Potential catalyst from upcoming semiconductor earnings could drive further upside in tech names."
"""

MARKET_TIDE_PROMPT = """Analyze market-wide sentiment and flow, focusing on:

1. Flow Analysis:
   - Calculate net premium flow direction
   - Compare institutional vs retail activity
   - Identify significant volume patterns
   - Track minute-by-minute changes (for intraday data)
   - Monitor daily accumulation patterns (for daily data)

2. Time-Based Patterns:
   - For minute data:
     * Identify intraday momentum shifts
     * Note volume spikes and timing
     * Track premium accumulation rate changes
     * Flag unusual divergences between calls/puts
     * Compare to previous intraday sessions
   - For daily data:
     * Monitor multi-day trends
     * Track institutional positioning changes
     * Note market structure shifts
     * Compare to historical ranges
     * Identify trend acceleration/deceleration

3. Historical Context:
   - Compare current flows to 30-day ranges
   - Note when metrics exceed historical thresholds
   - Track trend changes vs historical patterns
   - Flag divergences from typical behavior
   - Identify potential regime changes

4. Market Implications:
   - Evaluate overall market sentiment
   - Identify potential trend changes
   - Flag risk factors
   - Project short-term price movement potential
   - Provide specific entry/exit levels

Provide a concise insight focusing on:
1. First sentence: State the largest flow with exact amount and timing (e.g., "$5.2M net call premium surge at 14:30 ET")
2. Second sentence: Compare to historical patterns and thresholds
3. Third sentence: Explain potential catalysts and provide clear trading recommendation"""

DEEP_SEEK_PROMPT = """Analyze financial data with advanced predictive analytics, focusing on:

1. Risk Parameters:
   - Calculate Value at Risk (VaR) metrics
   - Analyze volatility surface changes
   - Monitor correlation breakdowns
   - Track tail risk indicators
   - Flag systemic risk patterns

2. Trend Forecasting:
   - Project price movement probabilities
   - Identify momentum regime changes
   - Calculate mean reversion levels
   - Detect pattern breakouts/breakdowns
   - Monitor sentiment shifts

3. Market Microstructure:
   - Analyze order flow imbalances
   - Track dark pool activity
   - Monitor options skew changes
   - Identify institutional positioning
   - Flag unusual volume patterns

4. Cross-Asset Correlations:
   - Track inter-market relationships
   - Monitor sector rotations
   - Analyze yield curve impacts
   - Flag currency effects
   - Note commodity influences

Required Format:
1. Risk Assessment: Provide specific probability ranges for identified risks
2. Trend Analysis: Include confidence levels for projected moves
3. Action Items: List specific entry/exit points with risk/reward ratios
4. Time Horizon: Specify expected duration for each prediction"""
