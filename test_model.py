import pytest
from lgapi import price_predictor, ModelInput
def tester():
    sample_input = ModelInput(features = [8.32, 41.0, 6.9, 1.0, 322.0, 2.5, 37.8, -122.2])
    prediction = price_predictor(sample_input)
    assert isinstance(prediction, int)
    assert prediction > 0 
