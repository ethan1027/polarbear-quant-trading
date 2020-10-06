from QuantConnect import *
from QuantConnect.Algorithm import *
from QuantConnect.Algorithm.Framework import *
from QuantConnect.Algorithm.Framework.Portfolio import PortfolioTarget
from QuantConnect.Algorithm.Framework.Risk import RiskManagementModel

class CopiedMaxDrawdownPercentPerSecurity(RiskManagementModel):
    def __init__(self, maximumDrawdownPercent = 0.03):
        self.maximumDrawdownPercent = -abs(maximumDrawdownPercent)

    def ManageRisk(self, algorithm, targets):
        targets = []
        for kvp in algorithm.Securities:
            security = kvp.Value
            if not security.Invested:
                continue
            algorithm.Log("risk check")
            pnl = security.Holdings.UnrealizedProfitPercent
            if pnl < self.maximumDrawdownPercent:
                targets.append(PortfolioTarget(security.Symbol, 0))

        return targets