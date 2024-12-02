package org.aoc.model;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public abstract class Solution {
    protected final int year;
    protected final int day;
    protected final int part;
    protected final Logger logger = LoggerFactory.getLogger(getClass());

    protected Map<String, Object> jsonInput;
    protected List<String> txtInput;

    public Solution(int year, int day, int part) {
        this.year = year;
        this.day = day;
        this.part = part;
        loadInput();
    }

    private void loadInput() {
        Path resourcePath = Paths.get("year", String.valueOf(year), "day", String.valueOf(day), "part", String.valueOf(part));
        try {
            resourcePath = Paths.get(Objects.requireNonNull(getClass().getClassLoader().getResource(resourcePath.toString())).toURI());
        } catch (Exception e) {
            logger.error("Error locating resource: {}", resourcePath, e);
            return;
        }

        try {
            List<Path> inputFiles = Files.list(resourcePath)
                    .filter(Files::isRegularFile)
                    .filter(path -> path.getFileName().toString().contains("input.json") || path.getFileName().toString().endsWith("input.txt"))
                    .toList();

            if (inputFiles.size() != 1) {
                throw new IllegalStateException("Expected exactly one input file, but found: " + inputFiles.size());
            }

            Path inputFile = inputFiles.getFirst();
            logger.info("loading {}", inputFile);
            String fileExtension = getFileExtension(inputFile.toString());

            if ("json".equalsIgnoreCase(fileExtension)) {
                ObjectMapper objectMapper = new ObjectMapper();
                jsonInput = objectMapper.readValue(inputFile.toFile(), new TypeReference<>() {});
                logger.info("JSON file loaded successfully for year {} and day {}", year, day);
            } else if ("txt".equalsIgnoreCase(fileExtension)) {
                txtInput = Files.readAllLines(inputFile);
                logger.info("Text file loaded successfully for year {} and day {}", year, day);
            } else {
                logger.error("Unsupported file type: {}", fileExtension);
            }
        } catch (IOException | UnsupportedOperationException e) {
            logger.error("Error reading file for year {}, day {}", year, day, e);
        } catch (IllegalStateException e) {
            logger.error("Input file validation failed: {}", e.getMessage());
            throw e;
        }
    }

    private String getFileExtension(String fileName) {
        int lastDotIndex = fileName.lastIndexOf('.');
        if (lastDotIndex == -1) {
            throw new UnsupportedOperationException("No file type found.");
        }
        return fileName.substring(lastDotIndex+1);
    }

    public abstract Object run();
}
