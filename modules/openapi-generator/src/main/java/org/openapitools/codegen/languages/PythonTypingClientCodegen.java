package org.openapitools.codegen.languages;

import org.openapitools.codegen.*;
import io.swagger.models.properties.ArrayProperty;
import io.swagger.models.properties.MapProperty;
import io.swagger.models.properties.Property;
import io.swagger.models.parameters.Parameter;

import java.io.File;
import java.util.*;

import org.apache.commons.lang3.StringUtils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PythonTypingClientCodegen extends DefaultCodegen implements CodegenConfig {
    public static final String PROJECT_NAME = "pythonTypingClient";

    static Logger LOGGER = LoggerFactory.getLogger(PythonTypingClientCodegen.class);

    public CodegenType getTag() {
        return CodegenType.CLIENT;
    }

    public String getName() {
        return "python-typing";
    }

    public String getHelp() {
        return "Generates a python-typing client.";
    }

    public PythonTypingClientCodegen() {
        super();

        outputFolder = "generated-code" + File.separator + "python-typing";
        modelTemplateFiles.put("model.mustache", ".py");
        apiTemplateFiles.put("api.mustache", ".py");
        embeddedTemplateDir = templateDir = "python-typing-client";
        apiPackage = File.separator + "Apis";
        modelPackage = File.separator + "Models";
        supportingFiles.add(new SupportingFile("README.mustache", "", "README.md"));
        // TODO: Fill this out.
    }
}
