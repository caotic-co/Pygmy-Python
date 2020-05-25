package com.pygmypython.tests;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class PygmyPythonTestSuiteRunner {
    public static void main(String[] args) {

        Result result = JUnitCore.runClasses(PygmyPythonTestSuite.class);
        for (Failure fail : result.getFailures()) {
            System.out.println(fail.getTrace());
            System.exit(1);
        }
        if (result.wasSuccessful()) {
            System.exit(0);
        }else{
            System.exit(1);
        }
    }
}
