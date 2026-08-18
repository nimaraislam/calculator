import  pytest 
from calculator.calculation import add, subtract, multiply, divide 


class  TestAdd :
    def  test_positive_numbers ( self ):
         assert  add ( 2 , 3 ) ==  5 

    def  test_negative_numbers ( self ):
         assert  add ( - 1 , - 1 ) ==  - 2 

    def  test_zero ( self ):
         assert  add ( 0 , 5 ) ==  5 


class  TestSubtract :
    def  test_simple ( self ):
         assert  subtract ( 10 , 3 ) ==  7 

    def  test_negative_result ( self ):
         assert  subtract ( 3 , 10 ) ==  - 7 


class  TestMultiply :
    def  test_simple ( self ):
         assert  multiply ( 4 , 5 ) ==  20 

    def  test_with_zero ( self ):
         assert  multiply ( 100 , 0 ) ==  0 


class  TestDivide :
    def  test_simple ( self ):
         assert  divide ( 10 , 2 ) ==  5.0 

    def  test_division_with_zero ( self ):
         with  pytest . raises ( ValueError ):
             divide ( 5 , 0 )