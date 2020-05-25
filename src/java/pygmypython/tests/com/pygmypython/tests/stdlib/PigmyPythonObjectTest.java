package com.pygmypython.tests.stdlib;

import com.pygmypython.stdlib.PigmyPythonObject;
import org.junit.Test;

import static org.junit.Assert.*;

public class PigmyPythonObjectTest {

    @Test
    public void addAttribute() {
        PigmyPythonObject obj = new PigmyPythonObject();
        obj.addAttribute("name", "John Doe");
        assertEquals("John Doe", obj.getAttribute("name"));

    }
}