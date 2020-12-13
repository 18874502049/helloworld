import pytest
import yaml

from pythoncode.calculator import Calculator

def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas1"]
        add_ids = datas["myid"]
        sub_datas = datas["datas2"]
        mul_datas = datas["datas3"]
        mod_datas = datas["datas4"]
        return [add_datas,sub_datas,mul_datas,mod_datas,add_ids]
class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[0],
                             ids=get_datas()[4])
    def test_add(self,a,b,expect,myfixture):
        assert expect == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[1],
                             ids=get_datas()[4])
    @pytest.mark.run(order=1)
    def test_sub(self,a,b,expect,myfixture):
        assert expect == self.cal.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[2],
                             ids=get_datas()[4])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[3],
                             ids=get_datas()[4])
    def test_mod(self, a, b, expect):
        assert expect == self.cal.mod(a, b)