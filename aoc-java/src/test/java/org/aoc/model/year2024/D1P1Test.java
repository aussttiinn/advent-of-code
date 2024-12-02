package org.aoc.model.year2024;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class D1P1Test {
    @Test
    public void test_run_1() {
        D1P1 cut = new D1P1();

        int expected = 11;
        int result = (int) cut.run();

        Assertions.assertEquals(expected, result);
    }
}
