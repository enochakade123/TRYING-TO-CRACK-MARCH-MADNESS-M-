import random

# --- MOMENTUM RULE ---
def get_momentum_boost(seed, last_margin):
    # If it's a "Cinderella" (7+ seed) and they won big (10+ pts), give 15% boost
    if seed >= 7 and last_margin >= 10:
        return 1.15
    else:
        return 1.0

# --- THE OFFICIAL 2026 "SWEET 16" DATASET ---
# Data updated as of Friday Night, March 27, 2026
teams_2026 = {
    # EAST REGION
    "Duke": {"seed": 1, "adjem": 28.5, "vegas": 0.17, "last_margin": 5, "status": "Elite 8"},
    "UConn": {"seed": 2, "adjem": 26.1, "vegas": 0.03, "last_margin": 11, "status": "Live"},
    "Michigan State": {"seed": 3, "adjem": 21.2, "vegas": 0.02, "last_margin": 8, "status": "Live"},

    # WEST REGION
    "Arizona": {"seed": 1, "adjem": 27.2, "vegas": 0.17, "last_margin": 21, "status": "Elite 8"},
    "Purdue": {"seed": 2, "adjem": 25.4, "vegas": 0.06, "last_margin": 2, "status": "Elite 8"},

    # SOUTH REGION
    "Illinois": {"seed": 3, "adjem": 24.9, "vegas": 0.08, "last_margin": 10, "status": "Elite 8"},
    "Iowa": {"seed": 9, "adjem": 19.5, "vegas": 0.02, "last_margin": 6, "status": "Elite 8"},

    # MIDWEST REGION
    "Michigan": {"seed": 1, "adjem": 26.8, "vegas": 0.22, "last_margin": 13, "status": "Elite 8"},
    "Iowa State": {"seed": 2, "adjem": 24.8, "vegas": 0.05, "last_margin": 19, "status": "Live"},
    "Tennessee": {"seed": 6, "adjem": 22.1, "vegas": 0.04, "last_margin": 7, "status": "Live"}
}

def simulate_game(t1, t2):
    s1, s2 = teams_2026[t1], teams_2026[t2]
    
    # 1. Apply your custom Momentum Logic
    m1 = get_momentum_boost(s1['seed'], s1['last_margin'])
    m2 = get_momentum_boost(s2['seed'], s2['last_margin'])
    
    # 2. Calculate "Power Rating" (70% KenPom Efficiency, 30% Vegas Title Odds)
    # We multiply Vegas by 100 to put it on a similar scale to AdjEM
    p1 = ((s1['adjem'] * 0.7) + (s1['vegas'] * 100 * 0.3)) * m1
    p2 = ((s2['adjem'] * 0.7) + (s2['vegas'] * 100 * 0.3)) * m2
    
    # 3. Determine Win Probability
    win_prob = p1 / (p1 + p2)
    
    # 4. Run the random simulation
    winner = random.choices([t1, t2], weights=[p1, p2])[0]
    
    print(f" MATCHUP: {t1} ({s1['seed']}) vs {t2} ({s2['seed']})")
    print(f" Probability: {t1} {win_prob:.1%} | {t2} {1-win_prob:.1%}")
    print(f" MOMENTUM CHECK: {t1} ({m1}x) | {t2} ({m2}x)")
    print(f" PROJECTED WINNER: {winner}\n")
    return winner

# --- EXECUTION ---
print("="*50)
print("  2026 MARCH MADNESS ELITE EIGHT PREDICTOR   ")
print("="*50 + "\n")

# Predict the upcoming Elite Eight Matchups
simulate_game("Arizona", "Purdue")
simulate_game("Illinois", "Iowa")
simulate_game("Duke", "UConn")  # Assumes UConn wins Sweet 16
simulate_game("Michigan", "Iowa State") # Assumes ISU wins Sweet 16