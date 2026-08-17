class LBWRuleEngine:
    @staticmethod
    def evaluate(pitching_inline, impact_inline, projected_hits_wickets):
        results = {
            "Pitching": "IN-LINE" if pitching_inline else "OUTSIDE",
            "Impact": "IN-LINE" if impact_inline else "OUTSIDE",
            "Wickets": "HITTING" if projected_hits_wickets else "MISSING"
        }
        
        is_out = pitching_inline and impact_inline and projected_hits_wickets
        results["Decision"] = "OUT" if is_out else "NOT OUT"
        return results