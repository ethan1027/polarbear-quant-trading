from Selection.QC500UniverseSelectionModel import QC500UniverseSelectionModel
from Alphas.MacdAlphaModel import MacdAlphaModel
from Alphas.RsiAlphaModel import RsiAlphaModel
from Portfolio.BlackLittermanOptimizationPortfolioConstructionModel import BlackLittermanOptimizationPortfolioConstructionModel
from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel
from Portfolio.MeanVarianceOptimizationPortfolioConstructionModel import MeanVarianceOptimizationPortfolioConstructionModel
from Execution.ImmediateExecutionModel import ImmediateExecutionModel
from Risk.MaximumDrawdownPercentPerSecurity import MaximumDrawdownPercentPerSecurity
from SlothSelectionModel import SlothSelectionModel
from TigerAlphaModel import TigerAlphaModel
from CopiedMaxDrawdownPercentPerSecurity import CopiedMaxDrawdownPercentPerSecurity

class SimpleProject(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 4, 10)
        # self.SetEndDate(2020, 8, 12)
        self.SetCash(5000)
        resolution = Resolution.Daily
        self.UniverseSettings.Resolution = resolution
        symbols = self.CreateUSEquities(["AAPL", "MSFT", "VICI", "AMD", "PTON", "NIO", "PENN"])
        self.SetAlpha(TigerAlphaModel(resolution))
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.03))

    def OnData(self, data):
        pass
    
    def CreateUSEquities(self, symbols):
        return [Symbol.Create(s, SecurityType.Equity, Market.USA) for s in symbols]