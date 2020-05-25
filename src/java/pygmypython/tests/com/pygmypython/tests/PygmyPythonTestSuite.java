package com.pygmypython.tests;

import com.pygmypython.tests.stdlib.*;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        // PygmyPython Stdlib
        PigmyPythonObjectTest.class,
})
public class PygmyPythonTestSuite { }
