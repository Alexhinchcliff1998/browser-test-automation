import pytest
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    result=yield;report=result.get_result();setattr(item,'rep_'+report.when,report)
