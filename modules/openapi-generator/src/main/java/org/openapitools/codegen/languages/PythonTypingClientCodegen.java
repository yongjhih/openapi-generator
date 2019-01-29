package org.openapitools.codegen.languages;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;
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

public class PythonTypingClientCodegen extends PythonClientCodegen implements CodegenConfig {
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

        modelTestTemplateFiles.clear(); // not support yet
        apiTestTemplateFiles.clear(); // not support yet
        modelDocTemplateFiles.clear(); // not support yet
        apiDocTemplateFiles.clear(); // not support yet
        supportingFiles.clear(); // not support yet

        outputFolder = "generated-code" + File.separator + "python-typing";
        modelTemplateFiles.put("model.mustache", ".py");
        apiTemplateFiles.put("api.mustache", ".py");
        embeddedTemplateDir = templateDir = "python-typing-client";
        supportingFiles.add(new SupportingFile("README.mustache", "", "README.md"));

        languageSpecificPrimitives.add("List");
        languageSpecificPrimitives.add("Dict");
        typeMapping.put("array", "List");
        typeMapping.put("map", "Dict");
    }

    @Override
    public void processOpts() {
    }

    @Override
    public CodegenOperation fromOperation(String path,
                                          String httpMethod,
                                          Operation operation,
                                          Map<String, Schema> definitions,
                                          OpenAPI openAPI) {
        final CodegenOperation op = super.fromOperation(path, httpMethod, operation, definitions, openAPI);
        op.vendorExtensions.put("lower_http_method", httpMethod.toLowerCase(Locale.ROOT));
        op.vendorExtensions.put("hasPathParams", !op.pathParams.isEmpty());

        for (CodegenParameter param : op.allParams) {
            param.vendorExtensions.put("lower_http_method", httpMethod.toLowerCase(Locale.ROOT));
        }

        return op;
    }

}
