from paytmpg.pg.request.ExtraParameterMap import ExtraParameterMap
from paytmpg.pg.response.FeeRateFactors import FeeRateFactors
from paytmpg.pg.utils.stringUtil import make_string, equals


class BaseResponseBodyfeerate(ExtraParameterMap):

    def __init__(self):
        self.feeRateFactors = FeeRateFactors()
        super(BaseResponseBodyfeerate, self).__init__()


    def get_fee_rate_factor(self):
        return self.feeRateFactors

    def set_fee_rate_factor(self, feeRateFactors):
        self.feeRateFactors = feeRateFactors

    def __str__(self):
        return make_string(self)

    def __eq__(self, other):
        return equals(self, other)
