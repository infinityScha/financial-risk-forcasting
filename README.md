# Financial Risk Forecasting — Learning in Python

This is my personal learning project based on Jon Danielsson’s book *Financial Risk Forecasting*.
The book doesn’t come with exercises, so I decided to create my own small coding tasks while reading it - 
to understand the ideas better and get some hands-on practice with risk modeling in Python.

## 🧭 Goal
I’m using this project to:
- learn how to apply statistical and risk modeling concepts from the book,
- write simple, clean Python code for each method,
- and slowly build a small portfolio of quantitative finance work.

I’m not trying to reproduce everything in the book - just exploring the main techniques and seeing how they work in practice.

## 🧩 Topics I Plan to Cover
- Returns and basic statistics  
- Volatility models (historical, EWMA, GARCH)  
- Value-at-Risk (parametric, historical, Monte Carlo)  
- Backtesting VaR models  
- Correlations and multivariate models  
- Extreme Value Theory basics  

(These will grow as I go through the chapters.)

## ⚙️ Setup
I’m using Python and conda for environment management.

```bash
conda create -n risk python=3.11 numpy pandas matplotlib scipy statsmodels yfinance
conda activate risk
```

or with pip:

```bash
pip install numpy pandas matplotlib scipy statsmodels yfinance
```

## 📁 Structure
```
financial-risk-forecasting/
│
├── notebooks/            # Jupyter notebooks per chapter
├── src/                  # small helper functions
└── README.md
```

## 🧮 Example
```python
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath("../"))
from src.utils import ewma_volatility

returns = pd.Series([...])  # daily returns
vol = ewma_volatility(returns, lambda_=0.94)
print(vol.tail())
```

## 💬 Notes
This is a **learning project**, not a production-grade repo.  
It’s meant to help me get comfortable with risk modeling concepts, code some math, and maybe build up to more advanced quant topics later on.

---

*Based on the book “Financial Risk Forecasting” by Jon Danielsson. This repo is not affiliated with the author or publisher.*
