package org.aoc;
import org.aoc.model.year2024.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Main {
    public static Logger logger = LoggerFactory.getLogger("AOC_MAIN");

    public static void main(String[] args) {
        logger.info("2024_DAY1_PART1: {}", new D1P1().run());
        logger.info("2024_DAY1_PART2: {}", new D1P2().run());
    }
}