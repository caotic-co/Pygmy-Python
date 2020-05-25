package com.pygmypython.stdlib;

import java.util.HashMap;

public class PigmyPythonObject {
    private HashMap<String, Object> attributes = new HashMap<String, Object>();

    public void addAttribute(String name, Object value){
        this.attributes.put(name, value);
    }

    public Object getAttribute(String name){
        return this.attributes.get(name);
    }
}
