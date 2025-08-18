# Phishing Awareness Study🔍

**Academic Research Project | [Download Full Paper](phishing_awareness_paper.pdf)**


*Evaluating Phishing Email Awareness Among Non-IT Professionals in Hospitality Sector*


## Research Overview 📄

This repository contains both the **scientific paper** and **experimental toolkit** for my study on phishing susceptibility among hotel reception staff in Bosnia and Herzegovina. Key findings:

- 66.7% click-through rate on simulated phishing emails
- 0% of participants verified sender addresses
- Significant correlation between work experience and detection rates

**Study Design**: Controlled field experiment with 6 participants at a 4-star hotel

## Research Components 🧩

### 1. Core Scientific Paper
  - Final manuscript (PDF)


### 2. Experimental Toolkit
```bash
├── data/                   # Email templates used in study
│   └── booking_phish.html  # Authentic Booking.com replica
├── scripts/
│   ├── send_phishing.py    # Study replication script
│   └── analyze_results.py  # Statistical analysis tools
├── results/                # Study findings
│   ├── responses.csv       # Raw experimental data
│   └── visualizations/     # Generated charts
```
# Replicating the Study 🔬

## Prerequisites
- Python 3.8+  
- Institutional Review Board approval (for human subjects research)

---

## Step-by-Step Replication

### 1. Configure Environment
```bash
pip install -r requirements.txt
```

### 2. Run the Experimental Protocol
```bash
# Send simulated emails (adjust targets as needed)
python scripts/send_phishing.py --target participant@example.com

# Analyze results (produces Figure 3 from paper)
python scripts/analyze_results.py
```

### 3. Generate New Visualizations
```bash
python scripts/visualize.py --output paper/figures/
```

## Key Scientific Findings 📊

| Metric                | Value   | Significance |
|------------------------|---------|--------------|
| Click-through Rate     | 66.7%   | p < 0.05     |
| Sender Verification    | 0%      | p < 0.01     |
| Experience Correlation | r = 0.82| p < 0.05     |

➡️ Full statistical analysis available in **Section IV** of the paper

## Ethical Considerations ⚖️

This study was conducted with:
- Written consent from all participants  
- Approval from the **hotel where the experiment was conducted**  
- Full debriefing procedures  

⚠️ Important: The provided tools should only be used:
- For academic research  
- With proper ethical approvals  
- On authorized systems

## Citation 📝

If using this research, please cite:

```bibtex
@article{mustafic2024phishing,
  title={Email Scam Detection in the Real World: Evaluating Phishing Email Awareness Outside the IT Sector},
  author={Mustafić, Lana},
  year={2024},
  institution={University of "Džemal Bijedić" Mostar}
}
```

## License 📜

- Research materials: **CC BY-NC 4.0**  
- Code: **MIT License**


