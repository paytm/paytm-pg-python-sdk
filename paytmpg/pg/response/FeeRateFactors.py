from paytmpg.pg.utils.stringUtil import make_string, equals


class FeeRateFactors:

    def __init__(self):
        self.corporateCard = None

    def set_corporateCard(self, corporateCard):
        self.corporateCard = corporateCard
        

    def get_corporateCard(self):
        #return self.feeRateFactors
        return self.corporateCard

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
