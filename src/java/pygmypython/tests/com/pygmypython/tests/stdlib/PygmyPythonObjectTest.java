package com.pygmypython.tests.stdlib;

import com.pygmypython.stdlib.PygmyPythonObject;
import org.junit.Test;

import static org.junit.Assert.*;

public class PygmyPythonObjectTest {

    @Test
    public void addAttribute() {
        PygmyPythonObject obj = new PygmyPythonObject();
        obj.addAttribute("name", "John Doe");
        assertEquals("John Doe", obj.getAttribute("name"));

    }
}