package org.aoc.model.year2024;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class D1Test {
    @Test
    public void test_run_1() {
        D1 cut = new D1();

        int expected = 11;
        int result = (int) cut.run();

        Assertions.assertEquals(expected, result);
    }
}
