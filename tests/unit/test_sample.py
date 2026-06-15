###################################### LEARNING PYTEST


###################################### UNIT TEST IN PYTHON

import sys

import pytest
#defining another function  
def test_method1():
    print("test_method1")

def test_method2():
    print("test_method2")

######################################### 1.ASSERSION IN PYTEST

#defining a function with parameter x
def func(x):
    return x+5

def test_func():
    #check whether 3+5 = 8 or not by passing 3 as an argument in function x
    assert func(3) == 8

def test_func2():
    #check whether 3+5 = 8 or not by passing 3 as an argument in function x
    assert "a" == "a", "a is equal to a"
    assert "b" > "a" , "b is greater than a"
    assert "a".__eq__("a") , "a is equal to a"
    # assert 5 == 6, "5 is not equal to 6" # USED FOR PRINTING CUSTOM MESSAGE IF TEST FAILS OTHER WISE NOT PRINTcls

######################################### 2.FLAG IN PYTEST

# pytest -h FOR HELP INFORMATION ABOUT ALL FLAGS
# pytest -v FOR VERBOSE OUTPUT PROVIDE MORE DETAIL
# pytest -rA FOR PASSED AND FAILED TEST CASE OR PRINT 
# pytest -k FOR KEYWORD ALSO USE REGULAR EXPRESSION IN THIS LIKE ONE OR TWO , ONE AND TWO
# pytest -m FOR MARKER

########################################## 3.MARKERS

################ USER DEFINE MARKER :- SMOKE, REGRESSION , SANITY, INTEGRATION

@pytest.mark.skip(reason="skip this test learning")
def test_function_1():
    print("test_function_1")

age = 15
@pytest.mark.skipif(age < 18, reason="you are not eligible")
def test_function_2():
    print("test_function_2")

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_function_21():
    print("hello")
    assert True

@pytest.mark.xfail(reason="learning x fail")
def test_function_3():
    print("test_function_3")
    assert False

@pytest.mark.xfail(reason="test_user_defined_marker hyundai")
@pytest.mark.hyundai() #USER DEFINED MARKER
def test_function_6():
    print("test_function_6")
    assert True

@pytest.mark.smoke
def test_function_7():
    print("test_function_7")

@pytest.mark.regression # GROUP TESTING
@pytest.mark.smoke
def test_function_8():
    
    print("test_function_8")

@pytest.mark.regression # GROUP TESTING
@pytest.mark.smoke
def test_function_9():
    print("test_function_9")

######################################### 4.PARAMETRIZE IN PYTEST
# @pytest.mark.xfail(reason="learning x fail")
@pytest.mark.parametrize("a, b, expected",[(1, 2, 3), (2, 3 ,5), (3, 4, 7)])
def test_function_4(a, b, expected):
    print("test_function_4")
    assert a+b == expected

@pytest.mark.parametrize("a",[1, 2, 3, 4, 5])
def test_function_5(a):
    print("test_function_5", a)
    assert a > 0

@pytest.mark.parametrize('a,b', [(1, 2), (2, 3), (3, 4)])
def test_function_5(a, b):
    assert a + 1 == b


################################# 5.FIXTURES
# autouse = True AUTOMATICALLY USE IN ALL THE FUNCTION
# scope = module, class, function, package, session 
#     FUNCTION = DEFAULT, USED ONCE PER TEST FUNCTION
#     CLASS = USED ONCE PER TEST CLASS 
#     MODULE = USED ONCE PER TEST FILE 
#     PACKAGE = USED ONCE PER PACKAGE OR USED ONCE FOR ALL THE TESTS IN THE DIRECTORY
#     SESSION = USED ONCE PER TEST SESSION OR USED ONCE FOR ALL THE TESTS 

class Test_1:

    def test_login_with_valid_credentials(self):
        print("Testing_test_login_with_valid_credentials")

class Test_2:
    def test_login_with_valid_email_and_invalid_password(self):
        print("Testing_test_login_with_valid_email_and_invalid_password")


###################################### INTEGRATION TEST IN PYTHON


################################################## 6.PARALLEL EXECUTION OF TEST USING PYTEST -xdist

# import time
# from selenium import webdriver
# def test_google():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://google.com")
    # time.sleep(3)
#     driver.quit()
# def test_insta():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://instagram.com")
    # time.sleep(3)
#     driver.quit()
# def test_facebook():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://facebook.com")
    # time.sleep(3)
#     driver.quit()
# def test_google_2():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://google.com")
    # time.sleep(3)
#     driver.quit()
# def test_insta_2():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://instagram.com")
    # time.sleep(3)
#     driver.quit()
# def test_facebook_2():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://facebook.com")
#     # time.sleep(3)
#     driver.quit()

################################# 7.USING HOOK FUNCTION (WORKS SAME AS FIXTURES) (PACKAGE AND SESSION HOOK FUNCTIONS USED IN CONFTEST.PY)

############## FOR FUNCTIONS 
# def setup_function(function):
#     print("Function Setup")

# def teardown_function(function):
#     print("Function Teardown")

# def test_hook_1():
#     print("test_hook_1")

# def test_hook_2():
#     print("test_hook_1")


# ############## FOR CLASS 
# class TestLogin:
#     @classmethod
#     def setup_class(cls):
#         print("Class Setup")

#     @classmethod
#     def teardown_class(cls):
#         print("Class Teardown")

#     def test_hook_4(self):
#         print("test_hook_4")   


# ############## FOR MODULES 
# def setup_module(module):
#     print("Module Setup")

# def teardown_module(module):
#     print("Module Teardown")   


############################## 8.ASSERTIONS :- SOFT ASSERTIONS(execute all the code even after failure) AND HARD ASSERTIONS(not execute after failure)

from pytest_check import check

# @pytest.mark.xfail(reason="leaning soft assertions")
def test_assertion():
    check.equal(1, 1)
    print("testing_assertion \n \n \n \n \n \n ")
    check.equal(1, 1)

################### 9.CREATING FIXTURE IN CONFTEST.PY AND USE IT IN THE TEST

@pytest.mark.usefixtures("fixture_setup_and_teardown")
class Test_fixture_1:
    def test_fixture_1(self):
        driver = "i'm the driver"
        print("test_fixture_1")
        assert driver == self.driver

    def test_fixture_2(self):
        driver = "i'm the driver"
        print("test_fixture_2")
        assert driver == self.driver


################################### 10.GENERATING ALLURE REPORT
    # install java 
    # install node and npm
    # npm install -g allure-commandline
    # allure --version
    # pip install allure-pytest 
    # pytest --alluredir="./reports"
    # allure serve "./reports"

# ATACHING SCREENSHOT IN THE ALLURE REPORT
    # allure.attach(driver.get_screenshot_as_png(), name="test_allure_report", attachment_type=allure.attachment_type.PNG)

# import allure
# from selenium import webdriver

# @allure.severity(allure.severity_level.BLOCKER) # SEVERITY LEVEL BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL WORK ON BOTH CLASS AND TEST LEVEL
# def test_allure_report():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://google.com")
#     print("test_allure_report")
#     allure.attach(driver.get_screenshot_as_png(), name="test_allure_report", attachment_type=allure.attachment_type.PNG)


# FOR SHARING ALLURE REPORTS WITH OTHER OPEN NETLIFY THEN DRAG AND THE REPORT THAT IS TEMPERORY(C:\Users\vansh\AppData\Local\Temp\10490575193620440160\allure-report) THAT WILL LIKE THIS AND DEPLOY THAT AFTER THAT YOU CAN SHARE 