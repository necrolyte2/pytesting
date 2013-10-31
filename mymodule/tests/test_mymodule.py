from nose.tools import eq_,raises

from .. import mymodule

class TestMyModule( object ):
    def test_addtwoints( self ):
        result = mymodule.add_numbers( 1, 2 )
        eq_( 3, result )

    def test_addtwofloats( self ):
        result = mymodule.add_numbers( 1.0, 2.0 )
        eq_( 3.0, result )

    def test_addintfloat( self ):
        result = mymodule.add_numbers( 1, 2.0 )
        eq_( 3.0, result )

    def test_addintlists( self ):
        result = mymodule.add_numbers( [1,2], [3,4] )
        eq_( [4,6], result )

    def test_addfloatlists( self ):
        result = mymodule.add_numbers( [1.0,2.0], [3.0,4.0] )
        eq_( [4.0,6.0], result )

    @raises(ValueError)
    def test_notlists( self ):
        # All of these need to raise Exceptions
        mymodule.add_numbers( [1], 1 )
        mymodule.add_numbers( 1, [1] )
        mymodule.add_numbers( [1], 1.0 )
        mymodule.add_numbers( 1.0, [1] )
