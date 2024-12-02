package org.aoc.model.year2024;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

class D1P2Test {
    @Test
    public void test_count_occurences() {
        ArrayList<Integer> l = new ArrayList<>();
        D1P2 cut = new D1P2();

        l.add(1);
        l.add(2);
        l.add(3);
        l.add(4);
        l.add(5);
        l.add(2);

        Assertions.assertEquals(2, cut.countOccurences(l, 2));
        Assertions.assertEquals(0, cut.countOccurences(l, 18));
        Assertions.assertEquals(0, cut.countOccurences(new ArrayList<>(), 18));
        Assertions.assertEquals(1, cut.countOccurences(l, 5));
    }

    @Test public void test_run() {
        D1P2 cut = new D1P2();

        Assertions.assertEquals(31, cut.run());
    }
}