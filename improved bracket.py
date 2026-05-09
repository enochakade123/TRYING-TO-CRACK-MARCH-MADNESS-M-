import random

# ==========================================================
#   2026 MARCH MADNESS ELITE EIGHT PREDICTOR
# ==========================================================

# --- MOMENTUM RULE ---
def get_momentum_boost(seed, last_margin):
    if seed >= 6 and last_margin >= 10:
        return 1.15
    return 1.0

# --- DATASET ---
teams_2026 = {
    "Arizona": {
        "seed": 1, "adjem": 37.5,
        "win_prob": 0.63,
        "last_margin": 21
    },
    "Purdue": {
        "seed": 2, "adjem": 29.8,
        "win_prob": 0.37,
        "last_margin": 2
    },
    "Illinois": {
        "seed": 3, "adjem": 28.9,
        "win_prob": 0.73,
        "last_margin": 10
    },
    "Iowa": {
        "seed": 9, "adjem": 18.2,
        "win_prob": 0.27,
        "last_margin": 6
    },
    "Duke": {
        "seed": 1, "adjem": 37.68,
        "win_prob": 0.62,
        "last_margin": 5
    },
    "UConn": {
        "seed": 2, "adjem": 28.41,
        "win_prob": 0.38,
        "last_margin": 4
    },
    "Michigan": {
        "seed": 1, "adjem": 39.1,
        "win_prob": 0.78,
        "last_margin": 13
    },
    "Tennessee": {
        "seed": 6, "adjem": 22.1,
        "win_prob": 0.22,
        "last_margin": 14
    },
}

def simulate_game(t1, t2, simulations=10000):
    s1, s2 = teams_2026[t1], teams_2026[t2]

    m1 = get_momentum_boost(s1['seed'], s1['last_margin'])
    m2 = get_momentum_boost(s2['seed'], s2['last_margin'])

    p1 = ((s1['adjem'] * 0.60) + (s1['win_prob'] * 100 * 0.40)) * m1
    p2 = ((s2['adjem'] * 0.60) + (s2['win_prob'] * 100 * 0.40)) * m2

    model_prob_t1 = p1 / (p1 + p2)
    model_prob_t2 = p2 / (p1 + p2)

    results = {t1: 0, t2: 0}
    for _ in range(simulations):
        winner = random.choices([t1, t2], weights=[p1, p2])[0]
        results[winner] += 1

    sim_winner = t1 if results[t1] > results[t2] else t2
    sim_pct_t1 = results[t1] / simulations
    sim_pct_t2 = results[t2] / simulations

    print(f"{'='*50}")
    print(f"  {t1} (#{s1['seed']}) vs {t2} (#{s2['seed']})")
    print(f"{'='*50}")
    print(f"  Momentum       : {t1} {m1}x  |  {t2} {m2}x")
    print(f"  Model Win Prob : {t1} {model_prob_t1:.1%}  |  {t2} {model_prob_t2:.1%}")
    print(f"  Simulations    : {t1} {sim_pct_t1:.1%}  |  {t2} {sim_pct_t2:.1%}")
    print(f"  PREDICTED WIN  : {sim_winner}")
    print()

    return sim_winner

# --- RUN ---
print()
print("  2026 NCAA MARCH MADNESS — ELITE EIGHT PREDICTOR")
print()

winners = []
winners.append(simulate_game("Arizona",  "Purdue"))
winners.append(simulate_game("Illinois", "Iowa"))
winners.append(simulate_game("Duke",     "UConn"))
winners.append(simulate_game("Michigan", "Tennessee"))

print(f"{'='*50}")
print(f"  PROJECTED FINAL FOUR")
print(f"{'='*50}")
for w in winners:
    print(f"  → {w}")
print(f"{'='*50}")
