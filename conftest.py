import pytest
@pytest.fixture(scope="module")
def myfixture():
    # print("执行我的fixture，里面的参数是：%s"%request.param)
    # yield request.param
    print("执行我的fixture")
# @pytest.fixture()
# def connectdb():
#     print("执行我的fixture--connectdb")